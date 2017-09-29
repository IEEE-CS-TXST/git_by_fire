###FIX ME!!!###
counter = 1
divisors = 0
while divisors < 500:
	divisors = 0
	triNumber = sum(range(1, counter + 1))
	for divisor in range(1, int(triNumber / 2)):
  		if (triNumber % divisor == 0): 
  				divisors += 1
  				print(triNumber)
  				counter += 1

#### MY BAD GUYS!!!!