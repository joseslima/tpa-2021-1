dp = []
elems = []

def percorrer(pos):
	global dp,elems
	id = elems[pos][2]
	if (dp[id] != -1):
		return dp[id]

	tam = 1
	for j in range(pos+1,len(elems)):
		if elems[j][0] > elems[pos][0] and elems[j][1] < elems[pos][1]:
			tam = max(tam, 1 + percorrer(j))
	dp[id] = tam	
	return dp[id]

def pega_maior(pos,maior,n):
	id = elems[pos][2]
	print(id)
	for i in range(pos+1,n):
		id = elems[i][2]
		if maior == dp[id]:
			pega_maior(i,maior-1,n)
			return

def main():
	global dp,elems
	while True:
		try:
			id = 1
			entrada = input().split()
			while len(entrada) == 2:
				entrada[0] = int(entrada[0])
				entrada[1] = int(entrada[1])
				entrada.append(id)
				elems.append(entrada)
				entrada = input().split()
				id+=1

		except EOFError:
			elems.sort(key=lambda x: (x[0],-x[1]))
			n = len(elems)
			if n == 0:
				return 0
			dp = [-1] * (n+1)
			maior = 0
			for i in range(n):
				tam = percorrer(i)
				if tam > maior:
					maior = tam

			print(maior)
			for i in range(0,n):
				id = elems[i][2]
				if maior == dp[id]:
					pega_maior(i,maior-1,n)
					return 0
			break
	return 0


main()
