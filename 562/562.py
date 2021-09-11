allCoins = []
cache = []

#Using python own max was doing time out.
def my_max(a,b):
	if a > b:
		return a
	#
	return b

def knapsack(n, weight):
	global allCoins,cache
	i = 1 
	
	while i <= n:
		j = weight
		while j > 0:
			if allCoins[i] <= j:
				cache[j] = my_max(cache[j], allCoins[i] + cache[j - allCoins[i]])
			#
			j-=1
		#
		i+=1
	#
	return cache[weight]
#

def main():
	global allCoins,cache
	n = int(input())
  
	for problem in range(n):	
		sum = 0		
		coinsAmount = int(input())
		coins = input().split()
		allCoins = [0]*(coinsAmount + 1)
		for i in range(coinsAmount):
			coin = int(coins[i])
			allCoins[i + 1] = coin
			sum+=coin
		#	
		cache = [0]*((sum//2) + 1)
		print(sum - 2 * knapsack(coinsAmount, sum//2)) 
	#

	return 0
main()
