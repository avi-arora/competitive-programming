"""
	Problem description - Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation).
	Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ).
	Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).

	input: t [the number of expressions <= 100]
			expression [length <= 400]
			[other expressions]
    output: The expressions in RPN form, one per line.

@author: Avishek Arora
"""
def is_expression_balanced(inputstr):
	stack = []
	for i in inputstr:
		if i == '(':
			stack += i
		elif i == ')':
			if stack.pop() == '(':
				continue
			else:
				return False
	if len(stack) > 0:
		return False
	return True

cases = int(raw_input())
assert cases < 100, "cases <= 100."
inputs = []
for t in range(0,cases):
	expression = raw_input()
	assert len(expression) <= 400, "Input expression <= 400."
	inputs += [expression]

for t in inputs:	
	if is_expression_balanced(t): #if the expression is not balanced, skip 
		output = ""
		stack = []
		precedence = {'^': 0, '*': 1, '/': 1, '+': 2, '-': 2} # smaller the number higher the precedence
		for i in t:
			ch = ord(i)
			if 97 <= ch <= 122: #if operand output it
				output += i
			elif i == ')':
				while True:
					ch = stack.pop()
					if ch == '(':
						break
					else:
						output += ch
			elif i in precedence.keys() or i == '(':
				while True:
					if len(stack) == 0:
						break
					elif stack[-1] == '(' or i == '(':
						break
					elif precedence[stack[-1]] > precedence[i]:
						break
					else:
						output += stack.pop()
				stack += i
		while len(stack) > 0:
			output += stack.pop()
		print output
