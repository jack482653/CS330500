from collections import defaultdict,Counter
from itertools import izip

ciphertext = ("MPYIGOBSRMIDBSYRDIKATXAILFDFKXTPPSNTTJIGTHDELT\n"
			"TXAIREIHSVOBSMLUCFIOEPZIWACRFXICUVXVTOPXDLWPENDHPTS\n"
			"DDBXWWTZPHNSOCLOUMSNRCCVUUXZHHNWSVXAUHIK\n"
			"LXTIMOICHTYPBHMHXGXHOLWPEWWWWDALOCTSQZELT")

# Help for Frequency analysis
text_dict = defaultdict(Counter)
for line in ciphertext.split('\n'):
	for i, c in enumerate(line):
		print i, c
		text_dict[i % key_size].update(c)

print "<< Counting..."
for k in text_dict:
	print str(k+1) + " sum: "
	print text_dict[k].most_common()

def to_ngrams(unigrams, length):
	return izip(*[unigrams[i:] for i in range(length)])

# Help for Kasiski test

tri = Counter()

for line in ciphertext.split('\n'):
	for word in to_ngrams(line, 3):
		tri.update([''.join(word)])

print tri.most_common(10)