#!/usr/bin/env python3

import socket
import quickpack

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 10020        # Port to listen on (non-privileged ports are > 1023)
DIR = r"lxfs.py"


def main():
	print("host:", HOST, "port:", PORT, "file:", DIR)

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
		ser.bind((HOST, PORT))
		ser.listen()
		s, addr = ser.accept()
		with s:
			print('Connected by', addr)
			print("sending", DIR)

			data = quickpack.pickle_dir(DIR)
			s.sendall(data)

			print("done")


if __name__ == '__main__':
	main()
