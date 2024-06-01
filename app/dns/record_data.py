from enum import Enum


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
    # https://www.rfc-editor.org/rfc/rfc1035#section-3.2.4

    IN = 1 # the Internet
    CS = 2 # the CSNET class (Obsolete - used only for examples in some obsolete RFCs)
    CH = 3 # the CHAOS class
    HS = 4 # Hesiod [Dyer 87]