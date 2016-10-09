import unittest
import io
import sys
from subprocess import PIPE, Popen

from qtools import __version__ as VERSION

class TestHelp(unittest.TestCase):
    def test_math(self):
            self.assertEqual(1+1, 2)

    # Coming soon!


#     def test_returns_usage_information(self):
#         output = Popen(['qtools', '--help'], stdout=PIPE).communicate()[0]
#         self.assertTrue('Usage:' in output)
#
#         output = Popen(['qtools', '-h'], stdout=PIPE).communicate()[0]
#         self.assertTrue('Usage:' in output)
#
# class TestVersion(TestCase):
#     def test_returns_version_information(self):
#         output = Popen(['qtools', '--version'], stdout=PIPE).communicate()[0]
#         self.assertEqual(output.strip(), VERSION)
#
#         output = Popen(['qtools', '-v'], stdout=PIPE).communicate()[0]
#         self.assertEqual(output.strip(), VERSION)
