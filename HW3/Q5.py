from collections import defaultdict,Counter
from itertools import izip, cycle
ciphertext = ("MPYIGOBSRMIDBSYRDIKATXAILFDFKXTPPSNTTJIGTHDELT\n"
			"TXAIREIHSVOBSMLUCFIOEPZIWACRFXICUVXVTOPXDLWPENDHPTSI\n"
			"DDBXWWTZPHNSOCLOUMSNRCCVUUXZHHNWSVXAUHIK\n"
			"LXTIMOICHTYPBHMHXGXHOLWPEWWWWDALOCTSQZELT")
key_size = 5

chr_int_map = lambda c: ord(c) - 65 # convert [A-Z] to [0-25]
int_chr_map = lambda i: chr(i + 65) # convert [0-25] to [A-Z]

# key generator
def key_range(size):
	first_key = ''.join('A' for _ in xrange(size))
	key = first_key
	while True:
		yield key
		# Get next key
		key_map = map(chr_int_map, key)
		key_map.reverse()
		for i in xrange(size):
			key_map[i] = (key_map[i] + 1) % 26
			if key_map[i] > 0:
				break
		key_map.reverse()
		key = ''.join(map(int_chr_map, key_map))
		if key == first_key:
			return

# decrypt
def decrypt(key, ciphertext):
	key_map = map(chr_int_map, key)
	ct_map = map(chr_int_map, ciphertext)
	pt_map = []
	for sub_key, cipher_chr in zip(cycle(key_map), ct_map):
		pt_map.append((cipher_chr - sub_key) % 26)
	return ''.join(map(int_chr_map, pt_map))

# check if plaintext is readable
dictionary = set()
with open('dictionary.txt', 'r') as file:
	for word in file:
		dictionary.add(word.strip().lower())

def to_ngrams(unigrams, length):
	return izip(*[unigrams[i:] for i in range(length)])

def is_readable(text_list, word_size):
	for line in text_list:
		for word in to_ngrams(line, word_size):
			w = ''.join(word).lower()
			if w in dictionary:
				return True
	return False

# main function
for key in key_range(key_size):
	plaintext = []
	for line in ciphertext.split('\n'):
		plaintext.append(decrypt(key, line))
	if is_readable(plaintext, 5) and is_readable(plaintext, 6) and is_readable(plaintext, 7):
		print 'Possible key: ' + key
		print 'Plaintext: '
		print plaintext