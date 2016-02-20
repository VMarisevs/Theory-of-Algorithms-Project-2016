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
		
		result = recursionSolution(chars, map)
		
		#if len(result) == 0:
		#	print "running"
		#	result = recursionSolution(chars[-1], map)
		
	return result

	
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

if __name__ == '__main__':
	import GenerateChars
	
	chars = GenerateChars.generate()
	
	#chars = ['a','a','r','d','v','a','r','k','s']
	
	#chars = ['a','u','c','t','i','o','n','e','d']
	
	print "".join(chars)

	wordmap = preprocessing()
	
	result = solve(wordmap, chars)
	
	print result
	
#
#	print wordmap["".join(sorted('axle'))]
#	import timeit
#	
#	# testing preprocessing method:
#	print(timeit.timeit("preprocessing()", setup="from __main__ import preprocessing", number=100))
#	