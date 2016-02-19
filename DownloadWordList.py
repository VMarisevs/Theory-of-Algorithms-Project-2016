# This script will download and parse word list into lowercase, line separated words
#

def downloadWordList(link):
	# urllib2 example
	# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
	
	# show download status
	# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
	
	import urllib2
	
	file_name = link.split('/')[-1]
	
	txtfile = urllib2.urlopen(link)
	output = open('test.txt.zip','wb')
	
	meta = txtfile.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)
    
	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = txtfile.read(block_sz)
		if not buffer:
			break
    
		file_size_dl += len(buffer)
		output.write(buffer)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,
	
	output.close()
	
	
def parseFile(filename):
	#
	# Reading allwords.txt file
	# parsing and saving into words.txt file
	#
	fileRead = open(filename, 'r')
	
	fileWrite = open('words.txt','wb')
	
	counter = 0;
	for line in fileRead:
		if counter != 0:
			fileWrite.write(line.replace(" ", "\n").lower())
		else:
			print line
		counter+=1
	
	fileWrite.close()
	fileRead.close()
	
	
if __name__ == "__main__":
	#downloadWordList("http://www.bestwordlist.com/allwords.txt")
	#downloadWordList("http://www-01.sil.org/linguistics/wordlists/english/")
	parseFile("allwords.txt")