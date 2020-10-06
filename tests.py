import unittest

import temp


class TestMethods(unittest.TestCase):
	def test_add(self):
		self.assertEqual(temp.smile(), ":)")


if __name__ == '__main__':
	unittest.main()
