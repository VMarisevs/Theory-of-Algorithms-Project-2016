def timeitWithPre():
	import solver
	import GenerateChars
	chars = GenerateChars.generate()
	chars = ['i', 'u', 'e', 'z', 't', 'w', 'd', 'j', 'u']
	
	wordmap = solver.preprocessing()
	result = solver.solve(wordmap, chars)	
	

if __name__ == '__main__':
	import timeit
	print(timeit.timeit("timeitWithPre()", setup="from __main__ import timeitWithPre", number=20))
	

	# 6.11212466922
	# 6.10481538622
	# 6.18407626118