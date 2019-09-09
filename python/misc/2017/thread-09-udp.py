#!/usr/bin/env python
import socket
import threading

port = 52526


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def sent_msg(udp_socket):
    while True:
        send_data = input('input data: ')
        udp_socket.sendto(send_data.encode('utf-8'), ('127.0.0.1', port))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', port))

    T_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    T_send = threading.Thread(target=sent_msg, args=(udp_socket,))

    T_recv.start()
    T_send.start()


if __name__ == '__main__':
    main()
