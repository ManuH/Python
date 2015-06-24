#Functions
def take_order(food):
	while True:
		try:
			number = int(input("How much {} would the client take?: ".format(food)))
			return number
			break
		except (NameError, TypeError, ValueError, SyntaxError):
			print("Please enter a number e.g.: 4")
def pay_option():
	while True:
		try:
			credit_card = raw_input("Client pays with credit card?: ").upper()
			if credit_card == "Y" or credit_card == "N":
				break
			else:
				print("Please enter Yes(Y) or No(N) e.g.: Y")
		except (NameError, TypeError, ValueError):
			print("Please enter Yes(Y) or NO(N) e.g.: Y")
	return credit_card
def discounts(answer, total):
	if answer == "Y":
		total *= 0.10
		discount = total
	return discount

#Constants
BEEF = 100
PIZZA = 40
WATER = 60
COKE = 45
SOUP = 60

#process sale
for i in range(5):
	if i == 0:
		number_of_beef = take_order("beef")
	elif i == 1:
		number_of_pizza = take_order("pizza")
	elif i == 2:
		number_of_water = take_order("water")
	elif i == 3:
		number_of_coke = take_order("coke")
	else:
		number_of_soup = take_order("soup")

order_cost = number_of_soup * SOUP + number_of_coke * COKE + number_of_water * WATER + number_of_pizza * PIZZA + number_of_beef * BEEF


#check credit card
answer = pay_option()
discount = discounts(answer, order_cost)
total = order_cost - discount

#final message
print("Total of the order: ${}".format(order_cost))

if answer == "Y":
	print("Discounts: Yes")
	print("Total discount: ${}".format(discount))
else:
	print("Discounts: No")

print("Total to pay: ${}".format(total))


