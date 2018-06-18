def hammingDistance(S, T):
	ham = 0
	for x, y in zip(S, T):
		if x != y:
			ham += 1
	return ham

def distanceBetweenPatternAndString(pattern, dna):
	k = len(pattern)
	distance = 0
	for x in dna:
		hamming = k+1
		for i in range(len(x) - k + 1):
			z = hammingDistance(pattern, x[i:i+k])
			if hamming > z:
				hamming = z
		distance += hamming
	return distance

def numberToPattern(x, k):
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)

def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

def medianString(dna, k):
	distance = (k+1) * len(dna) #wieder außreichend großen Anfangswert definieren 
	median = ""
	for i in range(4**k):
		currentpattern = numberToPattern(i, k)
		z = distanceBetweenPatternAndString(currentpattern, dna)
		if distance > z:
			distance = z #bestes (kleinstes) Ergebnis wird übernommen/gespeichert
			median = currentpattern
	return median

dna = ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
k = 3
print(medianString(dna, k))