import random

answer = random.randint(1, 10)
while True:
	try:
		guess = int(input('guess a number from 0-10: '))
		if 0 < guess < 11:
			if guess == answer:
				print('u r a genius')
				break
		else:
		     print('hey dumb, 1 - 10')

    except ValueError:
    	print('plz enter number')
    	continue
