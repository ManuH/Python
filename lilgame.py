
import random

#Set the number to guess first time
NUMBER = random.randint(1, 11)

#Set some variables
tries = 0
score = 0
high_score = 0

while True:
	if tries < 3:
		guess = int(input("Guess the number: "))

		#Control answer
		if guess == NUMBER:
			print("Congratulations!! You earned 10 points") 
			score += 10
			if score > high_score:
				high_score = score

			#Control if user wants to continue
			while True:
				try:
					again = raw_input("Continue? Yes/No: ")
					again = again.lower().strip()
					if again == "yes" or again == "no":
						tries = 0
						NUMBER = random.randint(1, 11)
						break
					else:
						print("Please enter 'Yes' or 'No' e.g.: Yes")
				except (NameError, TypeError, ValueError):
					print("Please enter 'Yes' or 'No' e.g.: Yes")

		else:
			if score > 0:
				print("Try again, you lost 2 points")
				again = "yes"
				tries += 1
				score -= 2
			else:
				print("Sorry, try again")
				again = "yes"
				tries += 1

	#Exit if user ran out of tries
	else:
		print("Sorry, you ran out of tries")
		break
	#Exit if usser doesn't want to continue
	if again == "no":
		break

#Final message
print("Final score: {}".format(score))
print("High score: {}".format(high_score))