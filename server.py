import socket
import argparse
import sys
import struct


# print the massages from the server
def run_server(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip, port))
        server_socket.listen()

        while True:
            connection, address = server_socket.accept()
            msg = connection.recv(4)
            num = struct.unpack("I", msg)[0] + 2**16 * struct.unpack("I", msg)[1]
            message = ""
            while len(message) < num:
                message += connection.recv(num - len(message)).decode("utf-8")

            print("Received data: ", message)
            connection.close()


def get_args():
    parser = argparse.ArgumentParser(description="Listen to server...")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    return parser.parse_args()


def main():
    """
    Implementation of CLI and sending data to server.
    """
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
        print("Done.")
    except Exception as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
