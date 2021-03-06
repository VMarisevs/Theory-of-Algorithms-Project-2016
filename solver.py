# Vladislavs Marisevs
# G00305490
# Date March 31st 2016

#
# For the start I will implement very basic algorithm:
#	- Creating a Map with sorted(word) as a key 
#	- and list of existing words as value
# This will allow me to get result in the best case scenario in first iteration
# In worse case I will be looping down with different combinations
#

# some code was taken from my gist
# https://gist.github.com/VMarisevs/8eb0437668cbad54aab7


def hashkey(word):
    key = "".join(sorted(word))
    return key

def preprocessing(filename="words.txt"):
	# creating a word map with key based on hashkey function
	# and value of list of words
	# reading file and populating the map
	wordmap = {}
	
	file = open(filename, 'r')
	
	for word in file:
		# removing /n character
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
	# result set will be populated with goal words
	result = set()
	
	# checking if the given char sequence exists in the map
	# to do that, apply hash algorithm and polling the map
	# if not going to else statement
	key = hashkey("".join(chars))
	
	# for iteration calculation:
	iteration_counter = 0
	
	if key in map:
		result.update(map[key])
	
	else:
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
			
			combinations("", key, i,combkey)
			
			for combination in combkey:
				iteration_counter += 1
				print iteration_counter, " ", combination
				# checking if this combination exits in the map
				# populating result set
				comb = "".join(sorted(combination))
				if comb in map:
					result.update(map[comb])
			
			# early exit from for loop
			if len(result) > 0:
				return result
		
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

def mainFull():
	import GenerateChars
	
	chars = GenerateChars.generate()
	#chars = ['i', 'u', 'e', 'z', 't', 'w', 'd', 'j', 'u']
	#chars = ['a','a','r','d','v','a','r','k','s']
	
	#chars = ['a','u','c','t','i','o','n','e','d']
	
	# They both the same, but second is sorted
	#chars = ['i', 'a', 'u', 'm', 'z', 'm', 'b', 'e', 'n']
	#chars = ['a', 'b', 'e', 'i', 'm', 'm', 'n', 'u', 'z']
	
	# This is a worse case, when it will go through all iterations
	# and won't find the goal
	
	#chars = ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']
	chars = ['z', 'f', 'w', 'r', 'b', 'p', 'd', 'g', 'h']
	
	print "Generated char sequence: ","".join(chars)

	wordmap = preprocessing()
	
	result = solve(wordmap, chars)
	
	print result

if __name__ == '__main__':
	mainFull()
