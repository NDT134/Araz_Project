import argparse
import sys
import socket
import struct

###########################################################
####################### YOUR CODE #########################
###########################################################


# send data to server with little endian
def send_data(server_ip, server_port, data):
    """
    Send data to server in address (server_ip, server_port).
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, server_port))
        client_socket.send(struct.pack("<I", len(data)))
        client_socket.sendall(data.encode("utf-8"))


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description="Send data to server.")
    parser.add_argument("server_ip", type=str, help="the server's ip")
    parser.add_argument("server_port", type=int, help="the server's port")
    parser.add_argument("data", type=str, help="the data")
    print(parser.parse_args())
    return parser.parse_args()


def main():
    """
    Implementation of CLI and sending data to server.
    """
    args = get_args()
    send_data(args.server_ip, args.server_port, args.data)
    """
    try:
        send_data(args.server_ip, args.server_port, args.data)
        print("Done.")
    except Exception as error:
        print(f"ERROR: {error}")
        return 1
    # """


if __name__ == "__main__":
    sys.exit(main())
