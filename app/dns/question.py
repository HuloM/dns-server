import struct
from dataclasses import dataclass
from app.dns.record_data import RecordClass, RecordType, name
from io import BytesIO

@dataclass
class Question:

    url: bytes

    record_type: RecordType

    record_class: RecordClass

    question: bytes = b''

    def construct_question(self):
        self.question = name(self.url, self.record_type, self.record_class)

        return self.question

    @classmethod
    def from_bytes(cls, received_body: bytes):
        reader = BytesIO(received_body)
        url = cls.decode_name_simple(reader)
        data = reader.read(4)
        record_type, record_class = struct.unpack('>HH', data)

        return cls(url, record_type, record_class)

    @staticmethod
    def decode_name_simple(reader: BytesIO) -> bytes:
        parts = []
        while (length := reader.read(1)[0]) != 0:
            parts.append(reader.read(length))
        return b'.'.join(parts)
