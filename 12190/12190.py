consumptionRange  = [ 100, 9900, 990000 ]
prices = [2, 3, 5, 7]

dp = {}

def getTEnergy(price):
	global consumptionRange, prices
	
	tEnergy = 0

	if (price in dp):
		return dp[price]
	#

	if (price == 0):
		return tEnergy
	#

	for i in range(len(consumptionRange)):
		tEnergy += min( max(0 , price / prices[i]), consumptionRange[i])
		price -= prices[i]*consumptionRange[i]
	#

	tEnergy += max(0, price/prices[3])
	
	dp[price] = tEnergy

	return tEnergy

def cost(energy):
	global consumptionRange, prices

	price = 0

	if (energy == 0):
		return price
	#

	for i in range(len(consumptionRange)):
		price += min(max(0, energy*prices[i]), prices[i]*consumptionRange[i]) 
		energy -= consumptionRange[i]
	#

	price += max(0, energy*prices[3])

	return price

def main():
	newLine = input()
	while ( newLine ) :
		splitedInput = newLine.split()
		
		together_price = int(splitedInput[0])
		
		difference_price = int(splitedInput[1])
		
		if (not together_price or  not difference_price):
			break
		#

		tEnergy = getTEnergy(together_price)
		start = 0
		end = tEnergy

		aux = 1
		
		# TO DO
		# IF I HAVE TIME TRY TO MAKE THIS CODE SNIPPET RECURSIVELY
		while (start < end and aux):
			half = (start + end) // 2
			
			a = cost(tEnergy - half)
			b = cost(half)
			
			diff = a - b;
			
			if (diff == difference_price):
				print(int(cost(half)))
				aux = 0
			else:
				if ( diff > difference_price):
					start = half
				else:
					end = half
			#
		#
		newLine = input()
	return 0
	
main()
