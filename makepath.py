#!/usr/bin/env python
#
#  Python module that recursively creates a set of directories.

import os


def makepath(*args):
	for directory_name in args:
		if not directory_name or os.path.exists(directory_name):
			continue
		makepath(os.path.dirname(directory_name))
		os.mkdir(directory_name)
