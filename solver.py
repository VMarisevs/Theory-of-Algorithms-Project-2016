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
	

wordmap = preprocessing()

print wordmap["".join(sorted('axle'))]

#if __name__ == '__main__':
#	import timeit
#	
#	# testing preprocessing method:
#	print(timeit.timeit("preprocessing()", setup="from __main__ import preprocessing", number=100))
#	