from app.dns.header import Header, OpCode, RCode
from app.dns.question import Question
from app.dns.answer import Answer
from app.dns.record_data import RecordClass, RecordType


def construct_dns(query_url: str):
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
        an_count = 1,
        ns_count = 0,
        ar_count = 0,
    ).to_bytes()

    dns_pkt += Question(url          = query_url,
                        record_type  = RecordType.A,
                        record_class = RecordClass.IN
                        ).construct_question()

    dns_pkt += Answer(url          = query_url,
                      record_type  = RecordType.A,
                      record_class = RecordClass.IN,
                      ttl          = 60,
                      length       = 4,
                      rdata        = '8.8.8.8'
                      ).construct_answer()

    return dns_pkt
