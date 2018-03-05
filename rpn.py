#!/usr/bin/env python3

import operator
import math

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'.': operator.floordiv,
	'!': math.factorial,
	'&': operator.and_,
	'|': operator.or_,
	'~': operator.invert,
}


def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			if(token ==  '!'):
				function = operators[token]
				arg1 = stack.pop()
				result = function(arg1)
				stack.append(result)
			elif(token == '%'):
				value = stack.pop()/100
				secondValue = stack.pop()
				stack.append(secondValue)
				value = value*secondValue
				stack.append(value)
			elif(token == '~'):
				function = operators[token]
				arg1 = stack.pop()
				result = function(arg1)
				stack.append(result)			 
			else:
				function = operators[token]
				arg2 = stack.pop()
				arg1 = stack.pop()
				result = function(arg1, arg2)
				stack.append(result)			
	
		print(stack)
	if len(stack) != 1:
		raise TypeError

	return stack.pop()

def main():
	while True:
		print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
	main()


