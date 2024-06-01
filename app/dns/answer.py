from dataclasses import dataclass
from app.dns.record_data import RecordClass, RecordType, name


@dataclass
class Answer:

    url: str

    record_type: RecordType

    record_class: RecordClass

    ttl: int

    length: int

    rdata: str

    answer: bytes = b''

    def construct_answer(self):
        self.answer = name(self.url, self.record_type, self.record_class)

        self.answer += self.ttl.to_bytes(4, byteorder='big')
        self.answer += self.length.to_bytes(2, byteorder='big')

        split_rdata = self.rdata.split('.')

        for i in split_rdata:
            self.answer += int(i).to_bytes(1, byteorder='big')

        return self.answer
