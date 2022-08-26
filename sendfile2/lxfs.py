import typing as _tp
from os import access, chdir, chmod, getcwd, link, listdir, lstat, mkdir, makedirs, \
	readlink, remove, removedirs, rename, renames, replace, rmdir, scandir, DirEntry, stat, stat_result, \
	symlink, truncate, unlink, utime, walk, \
	supports_dir_fd, supports_effective_ids, supports_fd, supports_follow_symlinks
from os.path import abspath, relpath, exists, lexists, \
	expanduser, expandvars, \
	getatime, getmtime, getctime, getsize, \
	isabs, isfile, isdir, islink, ismount, realpath, \
	samefile, sameopenfile, samestat, \
	supports_unicode_filenames
from shutil import copyfileobj, copyfile, SameFileError, copymode, copystat, copy, copy2, ignore_patterns, copytree, \
	rmtree, move, disk_usage, chown, which, Error
from collections.abc import Iterable, Sequence
from os import PathLike


BYTES_TS = bytes, bytearray
STR_TS = str, bytes, bytearray
STR_T = str
SEP_S = "/"
ALT_SEP_S = "\\"
STRIPS_CS = ' \t"<>'


def concat(*its):
	for it in its:
		yield from it


def normalize(s: STR_TS) -> STR_T:
	if isinstance(s, BYTES_TS):
		s = s.decode()
	return s.replace(ALT_SEP_S, SEP_S).strip(STRIPS_CS)


def partition(s: STR_T):
	def f(remaining, count):
		segment, separator, remaining = remaining.partition(SEP_S)
		# if count is 0, yield empty segment, as this causes '/' at start of path to be preserved
		# if segment or separator:  # this doesn't collapse // into /
		if segment or (count == 0 and separator):
			yield segment
		if remaining:
			yield from f(remaining, count + 1)
	return f(s, 0)


class PathSequence(PathLike, Sequence):
	pass


class BasePath(tuple, PathSequence):
	pass


def is_unix_root(self: BasePath):
	"""
	path sequence in this format: Path(('',)) -> "/"
	"""
	# handle case of Path(('',)) -> "/"
	return len(self) == 1 and not tuple.__getitem__(self, 0)


class Path(BasePath):
	def __new__(cls, path: (Iterable, PathLike, *STR_TS) = ()):
		if isinstance(path, cls):
			return path
		if isinstance(path, PathLike):
			path = partition(path.__fspath__())
		elif isinstance(path, STR_TS):
			path = partition(normalize(path))
		return tuple.__new__(cls, path)

	def __repr__(self):
		return f"{self.__class__.__name__}({tuple.__repr__(self)})"

	def __fspath__(self) -> STR_T:
		# handle case of Path(('',)) -> "/"
		if is_unix_root(self):
			return SEP_S
		return SEP_S.join(self)

	__str__ = __fspath__

	def __getitem__(self, item) -> (PathSequence, STR_T):
		r = tuple.__getitem__(self, item)
		if isinstance(item, slice):
			r = type(self)(r)
		return r

	def __add__(self, other) -> PathSequence:
		if isinstance(other, STR_TS):
			other = partition(other)
		return type(self)(concat(self, other))

	def __radd__(self, other) -> PathSequence:
		return type(self)(other) + self
