#!/usr/bin/env python3

import socket
import time

HOST = '125.236.211.85'  # The server's hostname or IP address
PORT = 10020        # The port used by the server
FILE = "test4.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))

	packets = []

	while True:
		data = s.recv(1024)
		if not data:
			break
		print("recv packet", )
		packets.append(data)

	with open(FILE, "wb") as fd:
		for packet in packets:
			fd.write(packet)

	print("done")


if __name__ == '__main__':
	pass
