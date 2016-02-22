def run():
	import solver
	import GenerateChars
	
	print "Loading words into map..."
	wordmap = solver.preprocessing()
	
	chars = GenerateChars.generate()
	print "\n\tGenerated string for countdown game: ", "".join(chars)
	
	
	result = solver.solve(wordmap, chars)
	print "\nresult ", result

if __name__ == '__main__':
	run()