#!/usr/bin/env python3

import socket
import quickpack

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 10020        # Port to listen on (non-privileged ports are > 1023)
DIR = r"download"


def main():
	print("host:", HOST, "port:", PORT, "file:", DIR)

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
		ser.bind((HOST, PORT))
		ser.listen()
		s, addr = ser.accept()
		with s:
			print('Connected by', addr)
			print("receiving", DIR)

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
