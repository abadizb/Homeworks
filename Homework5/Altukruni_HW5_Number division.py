#Abdulhalim Altukruni
#Python programming
#Homework5
#program 2


from random import randrange

print("\nINTEGER DIVISIONS")

try:
	playagain = "yes"
	while (playagain == "yes"):
		x = randrange(5)
		y = randrange(5)
		answer = x // y 
		print ( str(x)+"/" + str(y))
		guess = input ("")
		if answer == int(guess):
			print ("\nCORRECT!")
			
		else:
			print("\nINCORRECT!")
		playagain = input("Do you want to try again?: ")
	else:
		print("Good bye!")
		

except ValueError:
    print(" Please enter Integers Only!")
    pass

except ZeroDivisionError:
    pass
