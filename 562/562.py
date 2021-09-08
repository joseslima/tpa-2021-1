allCoins = []
mat = []

def my_max(a,b):
	if a > b:
		return a
	return b

def knapsack(n, weight):
	global allCoins,mat
	i = 1 
	while i <= n:
		j = weight
		while j > 0:
			if allCoins[i] <= j:
				mat[j] = my_max(mat[j], allCoins[i] + mat[j - allCoins[i]])
			j-=1
		i+=1
	return mat[weight]


def main():
	global allCoins,mat
	n = int(input())
  
	for problem in range(n):
		
		sum = 0		
		coinsAmount = int(input())
		coins = input().split()
		allCoins = [0]*(coinsAmount+5)
		for i in range(coinsAmount):
			coin = int(coins[i])
			allCoins[i + 1] = coin
			sum+=coin
			
		
		mat = [0]*((sum//2) + 5)
		print(sum - 2 * knapsack(coinsAmount, sum//2)) 

	return 0
main()
