import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_number(self):
		self.assertEqual(FizzBuzz(1), 1)
		self.assertEqual(FizzBuzz(2), 2)
		self.assertEqual(FizzBuzz(4), 4)

	def test_fizz(self):
		self.assertEqual(FizzBuzz(3), "fizz")
		self.assertEqual(FizzBuzz(9), "fizz")

	def test_buzz(self):
		self.assertEqual(FizzBuzz(5), "buzz")
		self.assertEqual(FizzBuzz(10), "buzz")
	
	def test_fizzbuzz(self):
		self.assertEqual(FizzBuzz(15), "fizzbuzz")
		self.assertEqual(FizzBuzz(30), "fizzbuzz")
		

if __name__ == '__main__':
	unittest.main()


