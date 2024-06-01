from enum import Enum
import struct
from dataclasses import dataclass


class OpCode(int, Enum):
    QUERY   = 0 # a standard query (QUERY)
    I_QUERY = 1 # an inverse query (IQUERY)
    STATUS  = 2 # a server status request (STATUS)


class RCode(int, Enum):
    """
    No error condition
    """
    NO_ERROR       = 0

    """
    Format error - The name server was
    unable to interpret the query.
    """
    FORMAT_ERROR   = 1

    """
    Server failure - The name server was
    unable to process this query due to a
    problem with the name server.
    """
    SERVER_FAILURE = 2

    """
    Name Error - Meaningful only for
    responses from an authoritative name
    server, this code signifies that the
    domain name referenced in the query does
    not exist.s
    """
    NAME_ERROR     = 3

    """
    Not Implemented - The name server does
    not support the requested kind of query.

    """
    NOT_IMPL       = 4

    """
    Refused - The name server refuses to
    perform the specified operation for
    policy reasons.  For example, a name
    server may not wish to provide the
    information to the particular requester,
    or a name server may not wish to perform
    a particular operation (e.g., zone
    """
    REFUSED        = 5


@dataclass()
class Header:
    """
    https://datatracker.ietf.org/doc/html/rfc1035#section-4.1

     0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      ID                       |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    QDCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ANCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    NSCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ARCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    """

    """
    A 16 bit identifier assigned by the program that
    generates any kind of query.  This identifier is copied
    the corresponding reply and can be used by the requester
    to match up replies to outstanding queries.
    """
    id: int

    """
    A one bit field that specifies whether this message is a
    query (0), or a response (1).
    """
    qr: bool

    """
    A four bit field that specifies kind of query in this
    message.  This value is set by the originator of a query
    and copied into the response.  The values are:
    """
    op_code: OpCode

    """
    Authoritative Answer - this bit is valid in responses,
    and specifies that the responding name server is an
    authority for the domain name in question section.
    """
    aa: bool

    """
    TrunCation - specifies that this message was truncated
    due to length greater than that permitted on the
    transmission channel.
    """
    tc: bool

    """
    Recursion Desired - this bit may be set in a query and
    is copied into the response.  If RD is set, it directs
    the name server to pursue the query recursively.
    Recursive query support is optional.
    """
    rd: bool

    """
    Recursion Available - this be is set or cleared in a
    response, and denotes whether recursive query support is
    available in the name server.
    """
    ra: bool

    """
    Reserved for future use.  Must be zero in all queries
    and responses.
    """
    z: int

    """
    Response code - this 4 bit field is set as part of responses.
    """
    r_code: RCode

    """
    an unsigned 16 bit integer specifying the number of
    entries in the question section.
    """
    qd_count: int

    """
    an unsigned 16 bit integer specifying the number of
    resource records in the answer section.
    """
    an_count: int

    """
    an unsigned 16 bit integer specifying the number of name
    server resource records in the authority records
    section.
    """
    ns_count: int

    """
    an unsigned 16 bit integer specifying the number of
    resource records in the additional records section
    """
    ar_count: int

    def to_bytes(self):
        # https://docs.python.org/3/library/struct.html
        return struct.pack(
            ">HHHHHH",
            self.id,
            (self.qr << 15)
            | (self.op_code.value << 11)
            | (self.aa << 10)
            | (self.tc << 9)
            | (self.rd << 8)
            | (self.ra << 7)
            | (self.z << 4)
            | self.r_code.value,
            self.qd_count,
            self.an_count,
            self.ns_count,
            self.ar_count,
            )