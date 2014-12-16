import sys

def main():

	#If the number of arguments is less than 2, print Usage and exit
	if len(sys.argv) < 2:
		print 'Usage: python find_anagrams.py <dictionary_file_name> press enter key and enter the words '
		exit()
	
	try:
		f = open(sys.argv[1], 'r') #Open the given file
	except:
		print 'Cannot read the file/ File not found' # Display this error if there was an error opening the file
		exit()
	
	
	words = {} #dictionary 
	for line in f:
		line = line.strip() #read line by line
		sorted_line = ''.join(sorted(line.lower())).replace(' ','') #sort this string and remove spaces
		try:
			words[sorted_line].add(line) #if the string has been seen before, add this string as an anagram to the set
		except:
			words[sorted_line] = set([line]) #if the string has not been seen before, add a new set with this string as an anagram

	f.close() #done reading the file
	
	if len(words)==0:
		print 'Dictionary is empty'
		exit()


	"""The code below takes in each word as the user types in and presses enter
	and keeps displaying teh word's anagrams, when an Enter key is pressed. 
	To exit, the user can just press another Enter Key."""

	
	while True:
		word = sys.stdin.readline().replace('\n','') #iterate through the input words
		if not word:
			break
		word = word.strip()
		sorted_word = ''.join(sorted(word.lower())).replace(' ','') #sort the input word and remove all spaces
		try:
			print list(words[sorted_word]) #if the word has anagrams, print them
		except:
			print "Does not exist" #word does not have an anagram in the dictionary
	

if __name__ == "__main__":
		main()
