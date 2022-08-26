#!/usr/bin/env python3

import socket
import quickpack

HOST = 'localhost'  # The server's hostname or IP address
PORT = 10020        # The port used by the server
DIR = "lxfs.py"


def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))

		data = quickpack.pickle_dir(DIR)
		s.sendall(data)

		print("done")


if __name__ == '__main__':
	main()
