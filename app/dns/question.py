from dataclasses import dataclass
from app.dns.record_data import RecordClass, RecordType, name
from io import BytesIO

@dataclass
class Question:

    url: str

    record_type: RecordType

    record_class: RecordClass

    question: bytes = b''

    def construct_question(self):
        self.question = name(self.url, self.record_type, self.record_class)

        return self.question

    @classmethod
    def from_bytes(cls, received_body):
        reader = BytesIO(received_body)
        print(reader.read(4))