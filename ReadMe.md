### Vladislavs Marisevs
#### G00305490
##### Theory of Algorithms Project 2016
##### Due: 5pm Thursday, March 31st 2016

# Countdown Letters Game Solver

[GitHub](https://github.com/VMarisevs/Theory-of-Algorithms-Project-2016)
[Gist](https://gist.github.com/VMarisevs/1f5341e9376eacef7658)

## How to run

 1. cd into repo folder
 1. run DownloadWordList.py file, this will create "words.txt" that holds all possible words.
 1. run solver.py it will generate and display random string and prints the best solution set for this string.
 1. timeit_solver_without.py displays time taken for looking for solution. 
 Note that it is approximate time, because it all depends from various factors such as dictionary size, randomly generated string.


## Game part
This project contains GenerateChars.py file that implements random character generation. 
 - Max string length is 9 
 - It should contain atleast 3 vowels
 - And 4 consonants
 
 GenerateChars.py :
	This file contains 3 for loops that generates random character list.
	1. Loop iterates only 3 times and appends randomly generated vowels to result list.
	1. Loop iterates only 4 times and appends 4 randomly generated consonants to result list.
	1. Loop iterates only 2 times and uses 4 random generations, first generator chooses between vowel and consonant and second chooses a character from vowel or consonant list.

## Game Solver
When we start the game, computer generates random string and this process is done in GenerateChars.py. For example it generated array of characters: 
> chars = ['i', 'u', 'e', 'z', 't', 'w', 'd', 'j', 'u']

To solve this game we need some sort of word list to choose from. I have created DownloadWordList.py script that downloads the .zip file and parses it into more readable word list file. And solver.py file uses .txt file to load all available words into memory. In very first example (master branch) I tried to do more robust algorithm with minimal BigO. To achieve that I made a map(dictionary in python) with key - sorted(chars) and value - list of words. For example if we are getting word *'auctioned'* from word list we are creating a new record in map as:
```javascript
{
	'acdeinotu' // "".join(sorted('auctioned'))
	: ['auctioned']
}
```
In next step if we are getting word 'cautioned', we inserting new value into list with same key:
``` javascript
{
	'acdeinotu' // "".join(sorted('cautioned'))
	: ['auctioned','cautioned']
}
```
#### Best case scenario
So in this case if we will receive shuffled *'acdeinotu'* string we just have to sort the string and it is the key to the result.

```python
	def hashkey(word):
		key = "".join(sorted(word))
		return key

	...
	key = hashkey("".join(chars))
	if key in map:
		result.update(map[key])
	...
``` 
This can only happen in the best case scenario. 

#### Average case scenario
Best case scenario will happen rarely, because chanses are very low to get randomly generated string from which you can get a 9 letter word or your dictionary must be very large.
If we don't have any 9 letter words in our map that match *sorted(chars)* we have to generate all possible combinations out of generated string. For example we have generated random string:
```python
	chars = ['i', 'u', 'e', 'z', 't', 'w', 'd', 'j', 'u']
	"".join(sorted(chars)) // = 'deijtuuwz'
```

There is no 9 letter word with *'deijtuuwz'* key, so it will generate set of combinations without repetition where order doesn't matter. We are interested in longest word so we would start from 8 letters. Lets look at (combinations formula)[https://www.mathsisfun.com/combinatorics/combinations-permutations.html].
> n! / r!(n-r)!
Where **n** is the number of things to choose from, and we choose **r** of them. In our case **n** is constant length of randomly generated string = *9*. But if we don't find any word with length *8* which is **r**, we decrease **r** by one. So in this round we are getting:
> (9!)/((8!)*(9-8)!) = 362880 / 40320 = 9
When we receive these combinations we have to use them as keys, to do that I am using hashkey function, that simply sorts the characters and polls the map and if there is one or more sets of words, it simply merges them into one list and returns result.
```
Note that I am using set of combinations called *combkey*. It might save me some iterations in case we have a duplicate letter in the random string.
```
In current case we have just 8 combinations, because we have duplicate in the string ('u')
```
1   deijtuuw
2   dijtuuwz
3   dejtuuwz
4   deituuwz
5   deijtuuz
6   deijuuwz
7   eijtuuwz
8   deijtuwz
```
There is no words with length of 8, going lower:
```
9    eijtuwz
10   deijuuw
	...
36   djtuuwz
37   eijtuuz
```
We have generated 36 combinations, but there was a duplicate so it was reduced by 7 and received 29.
> (9!)/((7!)*(9-7)!) = 362880 / 10080 = 36

```
38   dijuuw
39   ijtuuz
	...
99   jtuuwz
100   deijuz
```
We have generated 84 combinations, but there was a duplicate and received 62.
> (9!)/((6!)*(9-6)!) = 362880 / 4320  = 84

```
101   iuuwz
102   ituwz
	...
107   deitw
	...
190   eijuz
191   diuuz
```
We have generated 126 combinations, but there was a duplicate and received 91.
> (9!)/((5!)*(9-5)!) = 362880 / 2880  = 126
In this set of combinations we have found a result set *'wited'* with key *'deitw'*, but we continued to find all posible sets with this length. Unfortunately it was the only one and we quit the loop.

##### Result calculation
For this particular example we have tried to visit map where words length was 9,8,7,6,5. If all characters would be unique we would get:
| Length | with unique letters                       | in our case |
|--------|-------------------------------------------|-------------|
|    9   |  Not found with length 9. Iteration =   1 |           1 |
|    8   | (9!)/((8!)*(9-8)!) = 362880 / 40320 =   9 |           8 |
|    7   | (9!)/((7!)*(9-7)!) = 362880 / 10080 =  36 |          29 |
|    6   | (9!)/((6!)*(9-6)!) = 362880 / 4320  =  84 |          62 |
|    5   | (9!)/((5!)*(9-5)!) = 362880 / 2880  = 126 |          91 |
| Total  |                                       256 |         191 |

In this particular case we poll the map 191 time. This combination generation with current algorithm can't be avoided. We sorted the string 191 time, to improve the speed we could change hashkey function to another. It will be described in *Game Solver v2* section.

#### Worse case scenario
As we already seen how this algorithm works in the average scenario, we can assume that there is no such word with generated letters and all letters are unique. In this case we will loop until length = 0 without any result.

| Length |           Worse case scenario          |     |
|:------:|:--------------------------------------:|-----|
|      9 | Not found with length 9. Iteration     |   1 |
|      8 | (9!)/((8!)*(9-8)!) = 362880 / 40320  = |   9 |
|      7 | (9!)/((7!)*(9-7)!) = 362880 / 10080  = |  36 |
|      6 | (9!)/((6!)*(9-6)!) = 362880 / 4320   = |  84 |
|      5 | (9!)/((5!)*(9-5)!) = 362880 / 2880   = | 126 |
|      4 | (9!)/((4!)*(9-4)!) = 362880 / 2880   = | 126 |
|      3 | (9!)/((3!)*(9-3)!) = 362880 / 4320   = |  84 |
|      2 | (9!)/((2!)*(9-2)!) = 362880 / 10080  = |  36 |
|      1 | (9!)/((1!)*(9-1)!) = 362880 / 2880   = |   9 |
|  Total |                                        | 511 |

## Game Solver v2
#### Code name ascii-sum
I made another branch of this solver to compare one of the ideas from (my previous anagram conundrum projects)[https://gist.github.com/VMarisevs/8eb0437668cbad54aab7]. The idea is to save time on the hashkey algorithm. Instead of using native *sorted()* function I will sum the ascii codes *(ord() function returns ascii code)* of the string and use it as a key to the list of results. As I have tested before cost of this operation is less that sorting a string. 
Unfortunately this algorithm doesn't guarantee the 100% correct result. See example:
| ASCII | LETTER |
|:-----:|:------:|
|   97  |    a   |
|   98  |    b   |
|   99  |    c   |
|  100  |    d   |
|  101  |    e   |
|  102  |    f   |

If we have 2 words 'dad' and 'fab'
```
	ord('d') + ord('a') + ord('d') = 100 + 97 + 100 = 297
	ord('f') + ord('a') + ord('b') = 102 + 97 + 98  = 297
```
In this case we will have some words in the result set that are not similar to generated string. To fix this problem we need a function that will double check the result. I have also separated words by their length into different Maps this will avoid getting result with same hashkey but random length. I wrote 2 functions that will validate the result:
```python 
def errorcombchecking(combinations, resultset):
	# sorting all possible combinations
	result = set()
	sortedcombinations = dict()
	for comb in combinations:
		sortedcombinations["".join(sorted(comb))] = None
	
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
```
These functions will verify if the result is correct, if not we will keep on searching. In this project it didn't work out really good you can see in the Tests chapter. 
The reason that it didn't work out so good, because there was a lot of words with same sum of ascii codes and error checking was looping through each to verify the result too many times.

## Game Solver v2 updated
#### Code name ascii-sum-square
I made another branch that will significantly improve this algorithm. Instead of just sum the ascii codes we will square them, this will add them more uniqueness. For example:

| ASCII | LETTER |
|:-----:|:------:|
|   97  |    a   |
|   98  |    b   |
|   99  |    c   |
|  100  |    d   |
|  101  |    e   |
|  102  |    f   |

If we have 2 words 'dad' and 'fab'
```
	ord('d')*ord('d') + ord('a')*ord('a') + ord('d')*ord('d') = 
	100*100 + 97*97 + 100*100 = 29409
	
	ord('f')*ord('f') + ord('a')*ord('a') + ord('b')*ord('b') = 
	102*102 + 97*97 + 98*98  = 29417
```

These generated keys are unique, but still close enough and doesn't guarantee that will be 100% unique. So we have to keep error check.

## Tests
Tests were made with:
- Intel(R) Core(TM) i7-4720HQ Processor (Quad-Core, 6MB Cache, up to 3.6GHz w/ Turbo Boost) 1 SR
- 16GB Dual Channel DDR3L 1600MHz (2x8GB)
- 256GB m2.80 NGFF TLC SSD
- Windows 8.1 (64Bit) English

|                            Algorithm | Time it with preprocessing (20 times) | Time it without preprocessing (100 times) |
|-------------------------------------:|:-------------------------------------:|:-----------------------------------------:|
| 1. Using native python functionality |          *10.9651252465 sec*          |            *0.110005339702 sec*           |
|                1. Sum of ASCII codes |          *6.18407626118 sec*          |            *3.05906537489 sec*            |
|        1. Sum of Squared ASCII codes |          *7.62646127534 sec*          |            *0.217732144018 sec*           |

## Conclusion
I have implemented 3 solutions, with similar algorithm. To improve the speed I was changing key hash algorithm. As we can determine from Tests chapter they all can be used but to get best out of them we should choose one that best fits for our requirements. 
Algorithm Nr 1 has very slow running time with preprocessing, but very fast without. It will best fit for loading this into server and allow polling the map as many times as you like.
Algorithm Nr 2 has very fast running time with preprocessing and significantly slow without. So it is very useful when we are using it just once and terminating the script.
Algorithm Nr 3 is quite optimal, it is twice slower than Nr 1 without preprocessing but for a ~1/4 faster with preprocessing. 

## Appendix

#### Create Dictionary
At the start I was wring the script that uses 'beautifulsoup4' module to open a web page determine set of words and add them into list.

This script is specifically prepared for http://www.oxfordlearnersdictionaries.com website. To use it user should specify a link to a word dictionary and based on the dictionary it will automatically explores the paging and letter range.
```python
	for link in links:	
		page = urllib.urlopen(link).read()
		soup_page = BeautifulSoup(page, "html.parser").find('div', id='paging')
		tags_with_url = soup_page.find_all('a')
		for tag in tags_with_url:
			links[link].append(tag['href'])	
```
[Gist](https://gist.github.com/VMarisevs/041bb381c9b80044cbc5)
[GitHub repo](https://github.com/VMarisevs/Get-the-Oxford-Dictionary)

#### Download the gzip
After exploring oxford learners dictionaries website I had just 7726 words, which I found not enough to do countdown game. Some student posted in project forum a larger word list with 267751 items. I wrote another script that downloads the file, extracts it and parses into words separated with new line format.

## References
1. [Project GitHub repository](https://github.com/VMarisevs/Theory-of-Algorithms-Project-2016)
1. [Project Gist repository](https://gist.github.com/VMarisevs/1f5341e9376eacef7658)
1. [Some code and structure was taken from my Anagram project](https://gist.github.com/VMarisevs/8eb0437668cbad54aab7)
1. [Combination and Permutation theory](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
1. [Combination generation implementation](http://stackoverflow.com/a/17996834)
1. [Online solver example](http://wineverygame.com/wbg.php)
