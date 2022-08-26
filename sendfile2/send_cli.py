#!/usr/bin/env python3

import socket
import quickpack

HOST = 'localhost'  # The server's hostname or IP address
PORT = 10020        # The port used by the server
DIR = "download"


def main():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))

		packets = []

		while True:
			data = s.recv(1024)
			if not data:
				break
			print("recv packet", )
			packets.append(data)

		data = bytearray(quickpack.cat(*packets))
		quickpack.unpickle_dir(DIR, data)

		print("done")


if __name__ == '__main__':
	main()
