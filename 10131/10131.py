cache = {}
elems = []

def walk(pos):
	global cache,elems
	id = elems[pos][2]

	if (id in cache):
		return cache[id]

	size = 1
	for j in range(pos+1,len(elems)):
		if elems[j][0] > elems[pos][0] and elems[j][1] < elems[pos][1]:
			size = max(size, 1 + walk(j))
	cache[id] = size	
	return size

def getBigger(pos,bigger,n):
	id = elems[pos][2]
	print(id)
	for i in range(pos+1,n):
		id = elems[i][2]
		if bigger == cache[id]:
			getBigger(i,bigger-1,n)
			return

def main():
	global cache,elems
	while True:
		try:
			id = 1
			inpu = input().split()
			while len(inpu) == 2:
				inpu[0] = int(inpu[0])
				inpu[1] = int(inpu[1])
				inpu.append(id)
				elems.append(inpu)
				inpu = input().split()
				id+=1

		except EOFError:
			elems.sort(key=lambda x: (x[0],-x[1]))
			n = len(elems)
			if n == 0:
				return 0
			bigger = 0
			for i in range(n):
				size = walk(i)
				if size > bigger:
					bigger = size

			print(bigger)
			for i in range(0,n):
				id = elems[i][2]
				if bigger == cache[id]:
					getBigger(i,bigger-1,n)
					return 0
			break
	return 0


main()
