Approach:

For the given problem, I first read the file line by line, one word at a time.
I am using a HashMap to store the anagrams of a given string. The HashMap has the sorted string as
the key and its anagrams stored as the value. I use a set to store the set of anagrams, to avoid storage of duplicate anagrams
and hence save memory.

For each read word read from the file, I first sort the word, remove spaces and then I check if the HashMap has an entry for this string.
If the Map has an entry, i.e. the dictionary had anagrams of this string, I return the List of anagrams (not displaying duplicates),
else I return 'Does not exist'.

As Wikipedia says, I took care of spaces as well, as spaces should not be considered in anagrams, so words like 'New York', 'YORK NEW', 
'NEWYORK', 'newyork', 'yronekw' will all be anagrams of each other. So I took this into account too.

I have tried to handle test cases as follows:
1. If the number of arguments is less than 2 ( the file name and dictionary), print the Usage.
2. If there is an error reading the file, display error and exit.
3. Use a set to store anagrams, to avoid storing duplicate strings.

Time Complexity:

The time complexity to construct the dictionary is O(number of words in dictionary)
The time complexity to search for anagrams of a word is O(1).

Hence the total time complexity is :
O(number of words in dictionary) + O(number of input words)


Instructions to run the program:

The file takes in two arguments, each seperated by a space, and can be run as:

python find_anagrams.py <dictionary file>
<word1>
<word2>
<word3>
.
.
.
.
<wordn>


The user enters a word by typing in the word and pressing an enter, and the system keeps printing out the
anagrams of the entered word.
Once the user presses an Enter key without anything typed before it, the program exits.

