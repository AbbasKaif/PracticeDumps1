"""1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
input number.
Vending Machine:
1.water = $1.00
2.cola = $1.50
3.gatorade = $2.00"""

"""2.After placing an order, the user should be prompted to enter inputs 4 times:
1.The first time, the user should be prompted to enter the number of quarters they put in the machine. Assign this
number to a variable as an integer.
2.The second time, the user should be prompted to enter the number of dimes they put in the machine. Assign this
number to a variable as an integer.
3.The third time, the user should be prompted to enter the number of nickles they put in the machine. Assign this
number to a variable as an integer.
4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine. Assign this
number to a variable as an integer."""

"""4.Use flow control statements to print the user's change or output a message asking the user to try again depending
on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.
New knowledge for this problem:
1.%f format specifier
2.import sys and sys.exit()
3.int()"""


num=int(input("Enter an integer either 1, 2, or 3  "))
if(num!=1 and num!=2 and num!=3):
	print ("Invalid Input \a")
else:
	if(num==1):
		print ("Price of water is $1.00")
		m=1.00
	elif(num==2):
		print ("Price of cola is $1.50")
		m=1.50
	else:
		print ("Price of gatorade is $2.00")
		m=2.00
	q=int(input("Enter number of quarters "))
	d=int(input("Enter number of dimes "))
	n=int(input("Enter number of nickles "))
	p=int(input("Enter number of pennies "))
	total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
	if(total>=m):
		print("Your change is %s. Thanks!" %(total-m))
	else:
		print("Invalid input")