# Vladislavs Marisevs
# G00305490
# Date March 31st 2016

#
# In this branch I will use different hash algorithm for map
# I will create sum of ascii codes as key. Ofcourse I would 
# have to do some error checking before I am adding word into result set
# and also to avoid errors with length, I will use different maps:
# Map with 9 letter words, key = sum(ascii); value = list of words, which has to be double checked before posting
# Map with 8 letter words,
# ...
# 
# Using this algorithm I might save some time on the sorting algorithm
# some code was taken from my gist
# https://gist.github.com/VMarisevs/8eb0437668cbad54aab7


def hashkey(word):
    key = 0
    
    for letter in word:
       key += ord(letter)

    return key

def preprocessing(filename="words.txt"):
	# Creating list of dictionaries (maps) 0-8
	# This dictionaries corresponds to word length
	# wordmap[0] -> dictionary with word length = 1
	# wordmap[1] -> dictionary with word length = 2
	# ...
	# https://docs.python.org/2/tutorial/datastructures.html#dictionaries
	wordmap = [dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict()]

	file = open(filename, 'r')
	
	for word in file:
		# removing /n character
		word = word.strip()
		
		# insert words only if their length less or equals than 9 letters
		if len(word) <= len(wordmap):
			key = hashkey(word)
			
			if key not in wordmap[len(word)-1]:
				wordmap[len(word)-1][key] = set()
				
			wordmap[len(word)-1][key].add(word)
	
	return wordmap
	
def solve(listmaps, chars):
	# result set will be populated with goal words
	result = set()
	
	# checking if the given char sequence exists in the map
	# to do that, apply hash algorithm and polling the map
	# if not going to else statement
	key = hashkey("".join(chars))
	
	# for iteration calculation:
	#iteration_counter = 0
	
	if key in listmaps[8]:
		result = listmaps[8][key]
		result = errorchecking(chars, result)
	if len(result) == 0:
		# in else statement we are looping down from 8 characters to 1
		# generating combinations with downgrading the length
		# then looping through all combinations to get the result
		# if any of the combinations exists in the map, it will populate
		# result set. If result set is populated it exits from loop
		# and returns the result
		
		# https://www.mathsisfun.com/combinatorics/combinations-permutations.html
		for i in reversed(xrange(9)):
			
			# this key combination set will allow to eliminate duplicates
			# that might save some steps while polling the map
			combkey = set()
			
			combinations("", chars, i,combkey)
			
			for combination in combkey:
				#iteration_counter += 1
				#print iteration_counter
				# checking if this combination exits in the map
				# populating result set
	
				key = hashkey("".join(combination))
				if key in listmaps[i-1]:
					result.update(listmaps[i-1][key])
			
			# early exit from for loop
			if len(result) > 0:
				#print result
				# before we exit from function,
				# we have to check if all words match the charset, because we are using sum function which is not precise
				result = errorcombchecking(combkey,result)
				if len(result) > 0:	
					return result
		
	return result

def errorcombchecking(combinations, resultset):
	#print resultset
	# sorting all possible combinations
	result = set()
	sortedcombinations = dict()
	for comb in combinations:
		sortedcombinations["".join(sorted(comb))] = None
	
	#print sortedcombinations
	
	for word in resultset:
		if "".join(sorted(word)) in sortedcombinations:
			result.add(word)
	return result

def errorchecking(chars, resultset):
	result = set()
	
	sortedchars = "".join(sorted(chars))
	
	for word in resultset:
		if sortedchars == "".join(sorted(word)):
			result.add(word)
	
	return result
	
# if the solution won't be found in first iteration (with 9 letters)
# then it will generate set of combinations with 8 letters,
# if no solution found, it will go lower with 7 letters and so on...
# combination generator code was taken from this post:
# http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
# this answer was the key:
# http://stackoverflow.com/a/17996834

def combinations(combination, key, length, combination_list):
	if length == 0:
		combination_list.add(combination)
	else:
		for i in range(len(key)):
			combinations(combination + key[i], key[i+1:], length-1, combination_list)


			
# THIS code is for Testing:
def main():
	wordmaps = preprocessing()
	print wordmaps

def mainFull():
	import GenerateChars
	
	chars = GenerateChars.generate()
	
	#chars = ['a','a','r','d','v','a','r','k','s']
	#chars = ['e', 'd', 'i', 'j', 'u', 't', 'w', 'z']
	#chars = ['i', 'u', 'e', 'z', 't', 'w', 'd', 'j', 'u']
	
	#chars = ['a','u','c','t','i','o','n','e','d']
	
	# They both the same, but second is sorted
	#chars = ['i', 'a', 'u', 'm', 'z', 'm', 'b', 'e', 'n']
	#chars = ['a', 'b', 'e', 'i', 'm', 'm', 'n', 'u', 'z']
	
	# This is a worse case, when it will go through all iterations
	# and won't find the goal
	
	#chars = ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']
	#chars = ['z', 'f', 'w', 'r', 'b', 'p', 'd', 'g', 'h']
	
	print "Generated char sequence: ","".join(chars)

	wordmap = preprocessing()
	
	result = solve(wordmap, chars)
	
	print result

if __name__ == '__main__':
	mainFull()
