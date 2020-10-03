
class operations:
	
	def adds(self):
		try:
			print("Addition Continues...")
			print()
			x = int(input("Enter first addition no."))
			y = int(input("Enter second addition no."))
			print()
			print("Solution for addition between " ,end = "")
			print(x ,"and", y,"is", end = " ")
			print(x+y)
			print()
		except Exception as e:
			print("You have entered non-integer no.", e)
			print("Please reopen application and try to input a valid number")
			print()



	def sub(self):
		try:
			print("Subtraction Continues further...")
			print()
			x = int(input("Enter first subtraction no."))
			y = int(input("Enter second subtraction no."))
			print()
			print("Solution for subtraction between " ,end = "")
			print(x ,"and", y,"is",end = " ")
			print(x-y)
			print()
		except Exception as e:
			print("You have entered non-integer no.", e)
			print("Please reopen application and try to input a valid number")
			print()


	def mul(self):
		try:
			print("Multiplication continues further...")
			print()
			x = int(input("Enter first multiplication no."))
			y = int(input("Enter second multiplication no."))
			print()
			print("Solution for multiplication between " ,end = "")
			print(x ,"and", y,"is", end = " ")
			print(x*y)
			print()
		except Exception as e:
			print("You have entered non-integer no.", e)
			print("Please reopen application and try to input a valid number")
			print()



	def div(self):
		try:
			print("Division continues further...")
			print()
			x = int(input("Enter first division no."))
			y = int(input("Enter second division no."))
			print()
			print("Solution for division between " ,end = "")
			print(x ,"and", y,"is", end = " ")
			print(x/y)
			print()
		except Exception as e:
			print("You have entered non-integer no.", e)
			print("Please reopen application and try to input a valid number")
			print()



addition = operations()
subtraction = operations()
multiplication = operations()
division = operations()


addition.adds()
subtraction.sub()
multiplication.mul()
division.div()
