import unittest
from sample.sample_input_txt import SampleInputTXT

class TestHelp(unittest.TestCase):

	def test_help(self):
		self.assertEqual(SampleInputTXT().generate_sample(), True)

unittest.main()
