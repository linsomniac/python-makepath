#!/usr/bin/env python
#
#  Python module that recursively creates a set of directories.  This is
#  similar to the Unix "mkdir -p" shell command, and is largely done as
#  a programming exercise with a friend to compare how he did it in bash.
#
#  See the README.markdown or https://github.com/linsomniac/python-makepath
#  for more information.
#
#  Author: Sean Reifschneider <jafo@tummy.com>

import os


def makepath(*args):
	for directory_name in args:
		if not directory_name or os.path.exists(directory_name):
			continue
		makepath(os.path.dirname(directory_name))
		os.mkdir(directory_name)
