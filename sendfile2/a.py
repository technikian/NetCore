
def cat(*its):
	for it in its:
		yield from it


if __name__ == '__main__':
	x = b"asdf", b"asdf"
	y = cat(*x)
	print(bytes(y))
