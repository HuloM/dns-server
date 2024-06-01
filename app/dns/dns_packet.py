from app.dns.header import Header, OpCode, RCode
from app.dns.question import Question, RecordType, RecordClass


def construct_dns(query_url):
    dns_pkt = b''

    # preset values for testing
    dns_pkt += Header(
        id       = 1234,
        qr       = True,
        op_code  = OpCode.QUERY,
        aa       = False,
        tc       = False,
        rd       = False,
        ra       = False,
        z        = 0,
        r_code   = RCode.NO_ERROR,
        qd_count = 1,
        an_count = 0,
        ns_count = 0,
        ar_count = 0,
    ).to_bytes()

    dns_pkt += Question(record_type  = RecordType.A,
                        record_class = RecordClass.IN
                        ).name(query_url)

    return dns_pkt
