#!/usr/bin/env python
#
#  Python module that recursively creates a set of directories.

import os


def makepath(directory_name):
	if not directory_name or os.path.exists(directory_name):
		return
	makepath(os.path.dirname(directory_name))
	os.mkdir(directory_name)
