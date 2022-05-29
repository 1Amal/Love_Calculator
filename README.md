# Amal Kariyawasam 29/05/2022
# Fun little program to learn coding 
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# Based on an article on https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love 


Instructions

This is a fun little program that tries to test the compatibility between two people.

To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you guys are meant to be !"

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Jones"

name2 = "Jack Reacher"

T occurs 0 times

R occurs 1 time

U occurs 0 times

E occurs 4 times

Total = 5

L occurs 1 time

O occurs 1 times

V occurs 0 times

E occurs 5 times

Total = 7

Love Score = 57

Print: "Your score is 57, you are alright together."


Hint

    The lower() function changes all the letters in a string to lower case.

https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

    The count() function will give you the number of times a letter occurs in a string.

https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string