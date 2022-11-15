import random

def flip():
	flip = random.random()
	if (flip>=.5):
		return True
	else:
		return False

def main(num):
	heads = 0
	tails = 0
	resultString = ""

	for i in range(int(num)):
		if (flip()):
			heads+=1
			resultString += "H"
		else:
			tails+=1
			resultString += "T"
	
	print "Number of Heads: %i" % (heads)
	print "Number of Tails: %i" % (tails)
	print resultString

userInput = input("Please enter a number of flips: ")
main(userInput)
.
