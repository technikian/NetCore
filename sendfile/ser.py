#!/usr/bin/env python3

import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)

# 1.Gets the local ip/ip over LAN.
HOST = socket.gethostbyname(socket.gethostname())


PORT = 10020        # Port to listen on (non-privileged ports are > 1023)

FILE = r"/opt/buddy/remote/server/default/logs/~root.html"

print("host:", HOST, "port:", PORT, "file:", FILE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ser:
	ser.bind((HOST, PORT))
	ser.listen()
	cli, addr = ser.accept()
	with cli:
		print('Connected by', addr)
		print("sending", FILE)
		with open(FILE, "rb") as fd:
			cli.sendall(fd.read())
		print("done")


if __name__ == '__main__':
	pass
