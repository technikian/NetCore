import pickle
import lxfs as fs


def cat(*its):
	for it in its:
		yield from it


def load_dir(path):
	path = fs.Path(path)

	def _dir():
		for root, dirs, files in fs.walk(path):
			root = fs.Path(root)
			for file in files:
				file = root + file
				with open(file, "rb") as fd:
					data = fd.read()
				yield file[len(path):], data

	def _file():
		with open(path, "rb") as fd:
			data = fd.read()
		yield path[-1:], data

	if fs.isdir(path):
		return list(_dir())
	else:
		return list(_file())


def dump_dir(root, items):
	root = fs.Path(root)
	for path, data in items:
		path = root + path
		fs.makedirs(path[:-1], exist_ok=True)
		with open(path, "wb") as fd:
			fd.write(data)


def pickle_dir(root):
	items = load_dir(root)
	data = pickle.dumps(items)
	return data


def unpickle_dir(root, data):
	items = pickle.loads(data)
	dump_dir(root, items)


def main():
	data = b"asdf"
	o = pickle.dumps(data)
	print(o)
	P = r"D:\users\das\Mega\Project\Auto\Farm\NetCore\sendfile2"
	q = r"D:\users\das\Mega\Project\Auto\Farm\NetCore\sendfile3"
	x = load_dir(P)
	for y in x:
		print(y)

	dump_dir(q, load_dir(P))


def main2():
	p = r"D:\users\das\Mega\Project\Auto\Farm\NetCore\sendfile2/lxfs.py"
	q = r"D:\users\das\Mega\Project\Auto\Farm\NetCore\sendfile3"
	data = pickle_dir(p)
	print(len(data), data)
	unpickle_dir(q, data)


if __name__ == '__main__':
	main2()
