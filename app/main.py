import socket
from app.dns import dns_packet


def main():
    # Uncomment this block to pass the first stage

    response = dns_packet.construct_dns('codecrafters.io')
    print(response)

    # udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp_socket.bind(("127.0.0.1", 2053))
    #
    # while True:
    #     try:
    #         buf, source = udp_socket.recvfrom(512)
    #
    #         response = dns_packet.construct_dns()
    #
    #         udp_socket.sendto(response, source)
    #     except Exception as e:
    #         print(f"Error receiving data: {e}")
    #         break


if __name__ == "__main__":
    main()
