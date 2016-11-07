"""
	Problem description: One part of the new WAP portal is also a calculator computing expressions with very long numbers. 
	To make the output look better, the result is formated the same way as is it usually used with manual calculations.

	Your task is to write the core part of this calculator. 
	Given two numbers and the requested operation, you are to compute the result and print it in the form specified below. 
	With addition and subtraction, the numbers are written below each other. 
	Multiplication is a little bit more complex: first of all, we make a partial result for every digit of one of the numbers,
	 and then sum the results together.

	Input: There is a single positive integer T on the first line of input (equal to about 1000). 
	 It stands for the number of expressions to follow. Each expression consists of a single line containing a positive integer number,
	 an operator (one of +, - and *) and the second positive integer number. 
	 Every number has at most 500 digits. There are no spaces on the line. If the operation is subtraction, 
	 the second number is always lower than the first one. No number will begin with zero.

	Output: For each expression, print two lines with two given numbers, 
	the second number below the first one, last digits (representing unities) must be aligned in the same column. 
	Put the operator right in front of the first digit of the second number. 
	After the second number, there must be a horizontal line made of dashes (-).

	for each addition or subtraction, put the result right below the horizontal line, 
	with last digit aligned to the last digit of both operands.

	For each multiplication, multiply the first number by each digit of the second number.
 	Put the partial results one below the other, starting with the product of the last digit of the second number. 
 	Each partial result should be aligned with the corresponding digit. 
 	That means the last digit of the partial product must be in the same column as the digit of the second number. 
 	No product may begin with any additional zeros. If a particular digit is zero, the product has exactly one digit -- zero. 
 	If the second number has more than one digit, print another horizontal line under the partial results, and then print the sum of them.

	There must be minimal number of spaces on the beginning of lines, with respect to other constraints. 
	The horizontal line is always as long as necessary to reach the left and right end of both numbers (and operators) directly
	below and above it. 
	That means it begins in the same column where the leftmost digit or operator of that two lines (one below and one above) is.
	 It ends in the column where is the rightmost digit of that two numbers. The line can be neither longer nor shorter than specified.

	Print one blank line after each test case, including the last one.



	@author: Avishek Arora
"""
def add(num1, num2):
	result = ""
	carry, partial = 0, 0
	num1 , num2 = num1[::-1], num2[::-1]
	l1, l2 = len(num1), len(num2)
	for (n1, n2) in zip(num1, num2):
		partial = int(n1) + int(n2) + carry
		if partial < 10:
			result += str(partial)
			carry = 0
		else:
			carry = partial // 10
			result += str(partial % 10)
	if l1 == l2 and carry != 0:
		result += str(carry)
	elif l1 <  l2:
		result += str(int(num2[l1]) + carry) + num2[l1+1:]
	elif l1 > l2:
		result += str(int(num1[l2]) + carry) + num1[l2+1:]

	return result	

def sub(num1, num2):
	result = ""
	borrow, partial = 0, 0
	num1, num2 = num1[::-1], num2[::-1]
	l1, l2 = len(num1), len(num2)
	i = 0
	while i < min(l1,l2):
		if num1[i] >= num2[i]:
			result += str(int(num1[i]) - int(num2[i]))
		else:
			x = i+1
			while num1[x] < '1':
				x += 1
			tempnum1 += '0'
			for z in range(i+1, x):
				tempnum1 += '9'
			result += int('1'+ num1[i]) - int(num2[i])
			tempnum1 += str(int(num1[x]) - 1) + num1[x+1:]
			num1 = tempnum1
		i += 1
	if l1 > l2:
		result += num1[(l1-l2)+1:]

	print result[::-1]

def add_from_start(num1, num2):
	l1, l2 = len(num1), len(num2)
	result = ""
	carry, partial = 0, 0
	for (n1, n2) in zip(num1, num2):
		partial = int(n1) + int(n2) + carry
		if partial < 10:
			result += str(partial)
			carry = 0
		else:
			carry = partial // 10
			result += str(partial % 10)

	return result

def multiply(num1, num2):
	num1, num2 = num1[::-1], num2[::-1]
	l1, l2 = len(num1), len(num2)
	result1 = ""
	finalresult = ""
	carry , partial = 0, 0
	for n in range(len(num1)):
		partial = int(num1[n]) * int(num2[0]) + carry
		carry = partial // 10
		result1 += str(partial % 10)
	if l2 > 1:
		result2 = ""
		carry = partial = 0
		displacement = 0
		for number in range(1,len(num2)):
			for n in range(len(num1)):
				partial = int(num1[n]) * int(num2[number]) + carry
				carry = partial // 10
				result2 += str(partial % 10)
			displacement += 1
			result2 = '0' * displacement + result2
			result1 = result1 + '0' * ((displacement + l2) - l1)
			result1 = add_from_start(result1, result2)
			result2 = ""
	print result1[::-1]		


			



		
def run():
	testcases = input() 
	assert testcases <= 500, "Invalid No of test cases."
	for i in range(testcases):
		expression = raw_input()
		operator = find("+")
		if expression[operator] == "+":
			num1, num2 = expression[:operator], expression[operator+1:]
			add(num1, num2)
