#!/usr/bin/env python
#
#  Python module that recursively creates a set of directories.

import os


def makepath(directory_name):
	os.mkdir(directory_name)
