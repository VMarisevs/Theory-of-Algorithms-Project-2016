#
# This is a random nine letter generator for Countdown game
# it generates list of letters:
#  - three vowels
#  - four consonants
#

def generate():
	import random
	
	result = []
	
	max_letters = 9
	min_vowels = 3
	min_consonants = 4
	
	vowels = ['a', 'e', 'i', 'o', 'u']	
	
	consonants = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	
	# generating 3 random vowels
	for vowel in xrange(min_vowels):
		result.append(vowels[random.randint(0, len(vowels)-1)])
	
	# generating 4 random consonants
	for consonant in xrange(min_consonants):
		result.append(consonants[random.randint(0, len(consonants)-1)])
	
	# generating 2 more random characters 
	for letter in xrange(max_letters - (min_vowels + min_consonants)):
		if (random.randint(0,1) != 1):
			# generating vowel
			result.append(vowels[random.randint(0, len(vowels)-1)])
		else:
			# generating consonant
			result.append(consonants[random.randint(0, len(consonants)-1)])
			
	return result


if __name__ == '__main__':
	print generate()