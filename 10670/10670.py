agencies = []
cInitial = 0
cTarget = 0
available_agencies = 0
cache = {}

def minCost():



def main():
	global agencies, cInitial, cTarget, availableAgencies

	problems = input()

	for problem in problems:
		newLine = input().split()

		cInitial = newLine[0]
		cTarget = newLine[1]

		availableAgencies = newLine[2]
		agencies = []

		for i in range(available_agencies):
			agencyLine = input().split(":")

			agencyName = agencyLine[0]

			agencyCosts =  agencyLine.split(',')

		#
	#
	return 0
#


main()
