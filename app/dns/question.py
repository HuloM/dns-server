from dataclasses import dataclass
from enum import Enum
import struct


class RecordType(int, Enum):
    # https://www.rfc-editor.org/rfc/rfc1035#section-3.2.2

    A     = 1  # host address
    NS    = 2  # n authoritative name server
    MD    = 3  # mail destination (Obsolete - use MX)
    MF    = 4  # mail forwarder (Obsolete - use MX)
    CNAME = 5  # he canonical name for an alias
    SOA   = 6  # arks the start of a zone of authority
    MB    = 7  # mailbox domain name (EXPERIMENTAL)
    MG    = 8  # mail group member (EXPERIMENTAL)
    MR    = 9  # mail rename domain name (EXPERIMENTAL)
    NULL  = 10 # a null RR (EXPERIMENTAL)
    WKS   = 11 # a well known service description
    PTR   = 12 # a domain name pointer
    HINFO = 13 # host information
    MINFO = 14 # mailbox or mail list information
    MX    = 15 # mail exchange
    TXT   = 16 # text strings


class RecordClass(int, Enum):
    IN = 1 # the Internet
    CS = 2 # the CSNET class (Obsolete - used only for examples in some obsolete RFCs)
    CH = 3 # the CHAOS class
    HS = 4 # Hesiod [Dyer 87]


@dataclass
class Question:

    record_type: RecordType

    record_class: RecordClass

    question: bytearray = b''

    def name(self, url):
        split_url = url.split('.')

        site_len = len(split_url[0])
        self.question += site_len.to_bytes(1, byteorder='big')

        self.question += bytes(split_url[0], 'utf-8')

        domain_len = len(split_url[1])
        self.question += domain_len.to_bytes(1, byteorder='big')
        self.question += bytes(split_url[1], 'utf-8')

        self.question += b'\x00'

        self.question += self.record_type.to_bytes(2, byteorder='big')
        self.question += self.record_class.to_bytes(2, byteorder='big')

        return self.question
