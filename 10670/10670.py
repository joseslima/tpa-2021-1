agencies = []
cInitial = 0
cTarget = 0
availableAgencies = 0

def minCost(c, costA ,costB):
	cost = 100001

	half = c/2

	aux = ( c - half ) *  costA

	if (half >= cTarget and aux > costB):
		cost = min(cost, minCost(half, costA, costB) + costB )

	if (cost == 100001):
		cost = costA * (c - cTarget)

	return cost
#

def main():
	global agencies, cInitial, cTarget, availableAgencies

	cases = input()

	for case in cases:
		newLine = input().split()

		cInitial = int(newLine[0])
		cTarget = int(newLine[1])

		availableAgencies = int(newLine[2])
		agencies = []

		for i in range(availableAgencies):

			agencyLine = input().split(":")

			agencyName = agencyLine[0]
			
			agencyCosts =  agencyLine[1].split(',')

			costA = int(agencyCosts[0])
			costB = int(agencyCosts[1])

			agencies.append({ "name": agencyName, "cost": minCost(cInitial, costA, costB) })
		#

		print(agencies)
	#
	return 0
#


main()
