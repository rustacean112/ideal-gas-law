#!/usr/bin/env python

from fractions import Fraction as fr
from math import sqrt

def igl_1():
	loop = True

	while loop:
		try:
			num1 = float(input("Enter the first atom's mass number: "))
			break
		except ValueError:
			print("Please enter the numbers")
			loop1 = True

	loop = True

	while loop:	
		try:
			num2 = float(input("Enter the second atom's mass number: "))
			break
		except ValueError:
			print("Please enter the numbers")
			loop = True

	loop = True

	while loop:

		try:	
			num3 = float(input("Enter the length of pipe (in cm): "))
			break
		except ValueError:
			print("Please enter the numbers")
			loop = True

	loop = True

	while loop:

		try:
			tempQ = str(input("Are their temperatures equal? (yes/no): "))
		except ValueError:
			print("Please answer the question with only 'yes' or 'no' words.")
			loop = True

		if tempQ == "yes":
			temp = 1
			break

		elif tempQ == "no":
			miniloop = True

			while miniloop:
				try:
					temp = float(input("Enter the temperature: "))
					break
				except ValueError:
					print("Please enter numbers.")
					miniloop = True
			break

		else:
			print("Please answer the question with only 'yes' or 'no' words.")
			loop = True

	calculationOfCoefficientNum1 = round(sqrt(num1 * temp))
	calculationOfCoefficientNum2 = round(sqrt(num2 * temp))

	ratioOfNums = str(fr(calculationOfCoefficientNum2, calculationOfCoefficientNum1))

	coefficientOfNum1 = int(ratioOfNums[0])
	coefficientOfNum2= int(ratioOfNums[2])

	totalCoefficient = coefficientOfNum1 + coefficientOfNum2
	steps = num3 / totalCoefficient

	stepsOfFirstElement = int(steps * coefficientOfNum1)
	stepsOfSecondElement = int(steps * coefficientOfNum2)

	if stepsOfFirstElement > stepsOfSecondElement:
		verdict = stepsOfFirstElement
	elif stepsOfSecondElement == stepsOfFirstElement:
		verdict = stepsOfSecondElement
	else:	
		verdict = stepsOfSecondElement

	result = f"They will meet on {verdict} centimeters."

	print(result)

