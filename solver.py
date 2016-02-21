# Vladislavs Marisevs
# G00305490
# Date

#
# For the start I will implement very basic algorithm:
#	- Creating a Map with sorted(word) as a key 
#	- and list of words as value
# This will allow me to get result best case scenario in first iteration
# In worse case I will be looping down with different combinations
#

# some code was taken from my gist
# https://gist.github.com/VMarisevs/8eb0437668cbad54aab7

def hashkey(word):
    key = "".join(sorted(word))
    return key

def preprocessing(filename="words.txt"):
	
	wordmap = {}
	
	file = open(filename, 'r')
	
	for word in file:
		word = word.strip()
		
		key = hashkey(word)
		
		if key in wordmap:
			#populate
			wordmap[key].append(word)
		else:
			#insert
			wordmap[key] = [word]
	
	return wordmap
	
def solve(map, chars):
	result = []

	key = hashkey("".join(chars))
	
	if key in map:
		result = map[key]
	else:
		print 'no 9 letter word'
		
		# loops back from 8 - 0
		for i in reversed(xrange(9)):
			#print i
			combkey = []
			
			combinations("", key, i,combkey)
			
			for combination in combkey:
				comb = "".join(sorted(combination))
				if comb in map:
					result += map[comb]
			
			if len(result) > 0:
				return result
			#print combkey
		
		#result = recursionSolution(chars, map)
		
		#if len(result) == 0:
		#	print "running"
		#	result = recursionSolution(chars[-1], map)
		
	return result

# if the solution won't be found in first iteration (with 9 letters)
# then it will generate set of combinations with 8 letters,
# if no solution found, it will go lower with 7 letters and so on...
# combination generator code was taken from:
#http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n

def combinations(combination, key, length, combination_list):
	if length == 0:
		combination_list.append(combination)
		#print combination
		#return combination
	else:
		for i in range(len(key)):
			combinations(combination + key[i], key[i+1:], length-1, combination_list)
	
def recursionSolution(chars, map):
	result = []
	
	for x in xrange(len(chars)):		
		newchars = chars[:x] + chars[(x+1):]
#		print chars
#		del newchars[x]
#		word = ""
#		for letter in xrange(len(chars)):
#			if x != letter:
#				word += chars[letter]
		
#		print newchars
		key = hashkey(newchars)
		
		if key in map:
			result += map[key]
	
	if len(result) == 0:
		for x in xrange(len(chars)):		
			newchars = chars[:x] + chars[(x+1):]
			result = recursionSolution(newchars, map)
	
	return result

def mainFull():
	import GenerateChars
	
	chars = GenerateChars.generate()
	
	#chars = ['a','a','r','d','v','a','r','k','s']
	
	#chars = ['a','u','c','t','i','o','n','e','d']
	
	print "".join(chars)

	wordmap = preprocessing()
	
	result = solve(wordmap, chars)
	
	print result
	
def mainWithoutPre(wordmap):
	import GenerateChars
	
	chars = GenerateChars.generate()
	
	#chars = ['a','a','r','d','v','a','r','k','s']
	
	#chars = ['a','u','c','t','i','o','n','e','d']
	
	#print "".join(chars)
	
	result = solve(wordmap, chars)
	
	#print result
	
if __name__ == '__main__':
	mainFull()
	
#import timeit

# testing including preprocessing method:
#print(timeit.timeit("main()", setup="from __main__ import main", number=100))

# testing without preprocessing:
#wordmap = preprocessing()
#t = timeit.Timer(stmt="solver.mainWithoutPre(solver.wordmap)", setup="import solver")  
#print t.timeit(100)
	
	#print(timeit.timeit("mainWithoutPre(wordmap)", setup="from __main__ import mainWithoutPre", number=100))
	