# Amal Kariyawasam 29/05/2022
# Fun little program to learn coding 
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# Based on an article on https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love 

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n") # Capture name 1
name2 = input("What is your partners name? \n") # Capture name 2
name_combined=name1.lower()+name2.lower() # Combine name1 and name2 and turn them into lower case using lower() function and assign them to variable name_combined

#First string to check the word "true"
#Following code will assign how many times letters in brackets " " occour in the variable "name_combined "and will assign to the variable on left
count_t=name_combined.count("t")
count_r=name_combined.count("r")
count_u=name_combined.count("u")
count_e=name_combined.count("e")
sentence1_count=count_t+count_r+count_u+count_e

#Second string to check "love"
#Following code will assign how many times letters in brackets " " occour in the variable "name_combined "and will assign to the variable on left

count_l=name_combined.count("l")
count_o=name_combined.count("o")
count_v=name_combined.count("v")
count_e=name_combined.count("e")
sentence2_count=count_l+count_o+count_v+count_e

#In order to conctanate sentence1_count to sentence2_count interger will be converted to an string and sting concatanation will be used and then the result will be converted back to a interger
sentence1_count=str(sentence1_count)
sentence2_count=str(sentence2_count)
final_score=sentence1_count+sentence2_count
final_score=int(final_score)

# Finally using if and else statements final results will be shown on the screen according the the listed conidtion below
if final_score <= 10 or final_score >= 90: #Condition For Love Scores less than 10 or greater than 90, the message should be:
    print(f"Your score is {final_score}, you guys are meant to be !")
elif 40 <= final_score <= 50 : #For Love Scores between 40 and 50, the message should be:
    print(f"Your score is {final_score}, you are alright together.")
else: #Otherwise, the message will just be their score
    print(f"Your score is {final_score}.")

