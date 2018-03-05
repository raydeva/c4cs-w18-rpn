import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_percent(self):
		result = rpn.calculate('45 3 % +')
		self.assertEqual(46.35, result)
	def testpercent2(self):
		result = rpn.calculate('65 2 % -')
		self.assertEqual(63.7, result)
	def test_percent3(self):
		result = rpn.calculate('7 5  % *')
		self.assertEqual(2.45, result)
	def test_percent4(self):
		result = rpn.calculate('100 2 % /')
		self.assertEqual(50, result)
	def test_power(self):
		result = rpn.calculate('5 2 ^')
		self.assertEqual(25, result)
	#def test_intdiv(self):
	#	result = rpn.calculate('16 3 .')
	#	self.assertEqual(6, result)
 
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_adds(self):
		result = rpn.calculate('1 1 + 2 +')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3, result)
	#def test_toomany(self):
	#	with self.assertRaises(TypeError):
	#	result = rpn.calculate('1 2 3 +')
	def test_mul(self):
		result = rpn.calculate('2 3 *')
		self.assertEqual(6, result)
	def test_div(self):
		result = rpn.calculate('15 5 /')
		self.assertEqual(3, result)
	def test_fact(self):
		result = rpn.calculate('4 !')
		self.assertEqual(24, result)

#Exponentiation operator test
	def test_power(self):
		result = rpn.calculate('5 2 ^')
		self.assertEqual(25, result)
	
