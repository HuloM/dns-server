from dataclasses import dataclass
from app.dns.record_data import RecordClass, RecordType
import ipaddress

@dataclass
class Answer:

    """
    https://www.rfc-editor.org/rfc/rfc1035#section-3.2.1
     0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                                               |
    /                                               /
    /                      NAME                     /
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TYPE                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                     CLASS                     |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      TTL                      |
    |                                               |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                   RDLENGTH                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--|
    /                     RDATA                     /
    /                                               /
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    """

    url: bytes

    record_type: RecordType

    record_class: RecordClass

    ttl: int

    length: int

    rdata: str

    answer: bytes = b''

    def construct_answer(self):
        self.answer = (self.url
                       + b'\x00'
                       + self.record_type.to_bytes(2, byteorder='big')
                       + self.record_class.to_bytes(2, byteorder='big')
                       )

        self.answer += self.ttl.to_bytes(4, byteorder='big')
        self.answer += self.length.to_bytes(2, byteorder='big')

        ip = ipaddress.ip_address(self.rdata)
        self.answer += int(ip).to_bytes(4, byteorder='big')

        return self.answer
