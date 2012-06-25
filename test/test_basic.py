#!/usr/bin/env python
#
#  Run basic tests of makepath.

import sys
sys.path.append('.')
sys.path.append('..')
import os
import makepath

import unittest

class Test(unittest.TestCase):
	@classmethod
	def setUp(self):
		self.testdir = os.path.join('/tmp/makepath-test.%s' % os.getpid())
		if os.path.exists(self.testdir):
			os.system('rm -rf "%s"' % self.testdir)
		os.makedirs(self.testdir)
		os.chdir(self.testdir)
	
	@classmethod
	def tearDown(self):
		if os.path.exists(self.testdir):
			os.system('rm -rf "%s"' % self.testdir)
	
	def test_basic(self):
		'''Test basic makepath function calls.'''
		self.assertFalse(os.path.exists('a'))
		makepath.makepath('a')
		self.assertTrue(os.path.exists('a'))

		self.assertFalse(os.path.exists('a/b/c/d'))
		makepath.makepath('a/b/c/d')
		self.assertTrue(os.path.exists('a/b/c/d'))

print unittest.main()
