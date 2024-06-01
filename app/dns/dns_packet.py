from app.dns.header import Header, OpCode, RCode
from app.dns.question import Question
from app.dns.answer import Answer
from app.dns.record_data import RecordClass, RecordType


def construct_dns(received_header: bytes, received_body: bytes):
    dns_pkt = b''

    header = Header.from_bytes(received_header)

    # preset values for testing
    dns_pkt += Header(
        id       = header.id,
        qr       = True,
        op_code  = OpCode(header.op_code),
        aa       = False,
        tc       = False,
        rd       = header.rd,
        ra       = False,
        z        = 0,
        r_code   = RCode.NO_ERROR if header.op_code == 0 else RCode.NOT_IMPL,
        qd_count = 1,
        an_count = 1,
        ns_count = 0,
        ar_count = 0,
    ).to_bytes()

    question = Question.from_bytes(received_body)

    dns_pkt += Question(url          = question.url,
                        record_type  = RecordType(question.record_type),
                        record_class = RecordClass(question.record_class)
                        ).construct_question()
    print(dns_pkt)
    dns_pkt += Answer(url          = question.url,
                      record_type  = RecordType(question.record_type),
                      record_class = RecordClass(question.record_class),
                      ttl          = 60,
                      length       = 4,
                      rdata        = '1.2.3.4'
                      ).construct_answer()

    return dns_pkt
