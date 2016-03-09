
def timeitWithoutPre():	
	result = solver.solve(wordmap, chars)	
	

if __name__ == '__main__':
	
	# Preprocess is creating a map of words, and populating it with words from txt file
	# This file shows amount of time taken to solve the Count Down game.
	# In best case it will do just one iteration:
	#    - It will hash the sequence of chars
	#    - And if this key exists in the map, that would be the result O(1)
	#
	# Prepocessing is done here:
	#
	import solver
	import GenerateChars
	
	chars = GenerateChars.generate()
	chars = ['i', 'u', 'e', 'z', 't', 'w', 'd', 'j', 'u']
	wordmap = solver.preprocessing()
	
	import timeit
	print(timeit.timeit("timeitWithoutPre()", setup="from __main__ import timeitWithoutPre", number=100))
	
	# 0.109441814001
	# 0.110005339702
	# 0.110512118758