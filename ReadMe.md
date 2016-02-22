### Vladislavs Marisevs
#### G00305490
##### Theory of Algorithms Project 2016
##### Due: 5pm Thursday, March 31st 2016

# Countdown Letters Game Solver

## Game part
This project contains GenerateChars.py file that implements random character generation. 
 - Max character list length is 9 
 - It should contain atleast 3 vowels
 - And 4 consonants
 
 GenerateChars.py :
	This file contains 3 for loops that generates random character list.
	1. Loop iterates only 3 times and appends randomly generated vowels to result list.
	1. Loop iterates only 4 times and appends 4 randomly generated consonants to result list.
	1. Loop iterates only 2 times and uses 4 random generations, first generator chooses between vowel and consonant and second chooses a character from vowel or consonant list.

## Game Solver
To solve the game we definitely need some sort of word dictionary that will hold the values in memory (so it would be very efficient) and returns the result constantly. (Note that in this case list would be less efficient, because to get the goal we have to loop through whole list.) Word list will be described in Word list section.

### Preprocessing
In this section I am creating a map with key as sorted word characters and a list of words. To do that:
- Looping through all words in txt file and creating new record in map if it doesn't exists
- If it exists - populates the list

### Solver
- To get the result I am getting a hashcode of generated 9 letter string and checking if it exists in the map, if yes - return result. This is the best case scenario. Getting result in one iteration.
- In case there is no 9 letter hashcode in the map, starting count down with combination generation. And if it will find the result with 6 letters length it will continue until all combinations with length 6 completed and all result set combined. Then it will exit the loop. This will save us from iterating other combinations, because we already found the longest words with this key.