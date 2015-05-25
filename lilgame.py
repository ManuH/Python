def discounts(answer, total):
	if answer == "Y":
		total *= 0.10
		discount = total
	return total


test = discounts("Y", 10)

print(test)