1.	Scenario: You are developing a banking application that categorizes transactions based on the amount entered.
 Write logic to determine whether the amount is positive, negative, or zero.

Write Logic:
• Get the amount in input box from the Customer; Read the input amount.
• Check, If the amount is greater than 0, then print "The amount entered is Positive".
• Else if the amount is less than 0, print "The amount entered is Negative".
• Else, print "Zero".
    
****************************************************************************************************************************************************************
    
2.	Scenario: A digital locker requires users to enter a numerical passcode. As part of a security feature, the system checks the sum of the digits of the passcode. Write logic to compute the sum of the digits of a given number.

Write Logic:
•	Read the input number.
•	Initialize sum to 0
•	While the number is greater than 0, add the last digit to sum
•	Remove the last digit from the number.
•	Print the final sum.

****************************************************************************************************************************************************************
    
3.	Scenario: A mobile payment app uses a simple checksum validation where reversing a transaction ID helps detect fraud.
 Write logic to take a number and return its reverse.
    
Write Logic:
•	Read the input number.
•	Initialize reverse to 0.
•	While the number is greater than 0, take the last digit.
•	Add that digit to the reversed number.
•	Remove the last digit from the original number.
•	Print the reversed number.

****************************************************************************************************************************************************************
    
4.	Scenario: In a secure login system, certain features are enabled only for users with prime-numbered user IDs.
 Write logic to check if a given number is prime.
    
Write Logic:
•	Read the input number.
•	If the number is less than or equal to 1, print "Not Prime".
•	Else, check divisibility from 2 up to the square root of the number.
•	If any number divides it exactly, print "Not Prime".
•	Otherwise, print "Prime"

    
****************************************************************************************************************************************************************
    
5.	Scenario: A scientist is working on permutations and needs to calculate the factorial of numbers frequently.
 Write logic to find the factorial of a given number using recursion.
    
Write Logic:
•	Read the input number.
•	If the number is 0 or 1, return 1.
•	Otherwise, multiply the number by the factorial of the previous number.
•	Print the result.

****************************************************************************************************************************************************************

6.	Scenario: A unique lottery system assigns ticket numbers where only Armstrong numbers win the jackpot.
 Write logic to check whether a given number is an Armstrong number.
    
Write Logic
• Read the number.
• Count how many digits it has.
• Make a copy of the original number.
• Take one digit at a time from the number.
• Raise each digit to the power of the total number of digits.
• Add all those values.
• Compare the sum with the original number.
• If they are equal, it is an Armstrong number.
• Otherwise, it is not an Armstrong number.
    
****************************************************************************************************************************************************************

7.	Scenario: A password manager needs to strengthen weak passwords by swapping the first and last characters of user-generated passwords.
 Write logic to perform this operation on a given string.

Write Logic:
•	Take the string input.
•	Check if it has at least 2 characters.
•	Swap the first character with the last character.
•	Keep the middle characters the same.
•	Print the new string.

****************************************************************************************************************************************************************
    
8.	Scenario: A low-level networking application requires decimal numbers to be converted into binary format before transmission.
 Write logic to convert a given decimal number into its binary equivalent.
    
Write Logic
•	Take the decimal number.
•	Divide it by 2.
•	Save the remainder.
•	Divide the quotient again by 2.
•	Keep repeating until the quotient becomes 0.
•	Read all the remainders from bottom to top.
•	That gives the binary number.

****************************************************************************************************************************************************************
    
9.	Scenario: A text-processing tool helps summarize articles by identifying the most significant words.
 Write logic to find the longest word in a sentence.

Write Logic:
• Take the sentence as input.
• Split it into words.
• Keep the first word as the longest word for now.
• Compare each word with it.
• If a word is longer, replace the longest word.
• Print the longest word at the end.

****************************************************************************************************************************************************************

10.	Scenario: A plagiarism detection tool compares words from different documents and checks if they are anagrams (same characters but different order).
 Write logic to check whether two given strings are anagrams.

Write Logic:
• Take two strings as input.
• Remove spaces and convert both strings to lowercase.
• Check if both strings have the same length.
• Sort both strings or count their characters.
• Compare them.
• If they match, the strings are anagrams.
• Otherwise, they are not anagrams. 



