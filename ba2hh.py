def hammingDistance(S, T): #S und T sind die zu vergleichenden Strings
	ham = 0
	for x, y in zip(S, T):
		if x != y: #x ungleich y
			ham += 1
	return ham

def distanceBetweenPatternAndString(pattern, dna):
	k = len(pattern)
	distance = 0
	for x in dna:
		hamming = k+1 #ausreichend große Hamming Distance zum Anfang definieren
		for i in range(len(x) - k + 1):
			z = hammingDistance(pattern, x[i:i+k])
			if hamming > z:
				hamming = z #bestes (kleinstes) Ergebnis wird übernommen/gespeichert
		distance += hamming
	return distance

dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
pattern = "AAA"
print(distanceBetweenPatternAndString(pattern, dna))