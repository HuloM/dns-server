import socket
from app.dns import dns_packet


def main():
    # Uncomment this block to pass the first stage

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 2053))

    while True:
        try:
            buf, source = udp_socket.recvfrom(512)

            received_header = buf[:12]
            received_body = buf[12:]
            print(received_header)
            print(received_body)
            response = dns_packet.construct_dns(received_header, received_body)

            udp_socket.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break


if __name__ == "__main__":
    main()
