import struct
from dataclasses import dataclass
from app.dns.record_data import RecordClass, RecordType
from io import BytesIO

@dataclass
class Question:

    url: bytes

    record_type: RecordType

    record_class: RecordClass

    question: bytes = b''

    def construct_question(self):
        self.question = (self.url
                         + b'\x00'
                         + self.record_type.to_bytes(2, byteorder='big')
                         + self.record_class.to_bytes(2, byteorder='big')
                         )

        return self.question

    @classmethod
    def from_bytes(cls, received_body: bytes):
        reader = BytesIO(received_body)
        url = cls.decode_name_simple(reader)

        split_url = url.decode('utf-8').split('.')

        labels = b''.join([bytes([len(label)]) + bytes(label, 'utf-8') for label in split_url])

        data = reader.read(4)
        record_type, record_class = struct.unpack('>HH', data)

        return cls(labels, record_type, record_class)

    @staticmethod
    def decode_name_simple(reader: BytesIO) -> bytes:
        parts = []
        while (length := reader.read(1)[0]) != 0:
            parts.append(reader.read(length))
        return b'.'.join(parts)
