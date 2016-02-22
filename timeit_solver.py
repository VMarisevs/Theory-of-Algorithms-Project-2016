def timeitWithPre():
	import solver
	import GenerateChars
	chars = GenerateChars.generate()
	
	wordmap = solver.preprocessing()
	result = solver.solve(wordmap, chars)	
	

if __name__ == '__main__':
	import timeit
	# 0.555812973801 sec is to build complete map, run the function and get the result
	# The result will be pseudo random, because it could reach the goal at 9 letters
	# and exit from a loop or it could explore lower and number of visited nodes will
	# grow exponentionally
	print(timeit.timeit("timeitWithPre()", setup="from __main__ import timeitWithPre", number=1))