'''
Title:Character Count
Date:2025-11-22
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-23
Description:
Given a sentence string, return an array with a count of each character in alphabetical order.
    Treat upper and lowercase letters as the same letter when counting.
    Ignore numbers, spaces, punctuation, etc.
    Return the count and letter in the format "letter count". For instance, "a 3".
    All returned letters should be lowercase.
    Do not return a count of letters that are not in the given string.

Examples:
1. count_characters("hello world") 
should return ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"].

Waiting:2. count_characters("I love coding challenges!") 
should return ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"].

Waiting:3. count_characters("// TODO: Complete this challenge ASAP!") 
should return ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"].
'''
def count_characters(sentence):
    counts = {}
    for char in sentence.lower():
        if char.isalpha():
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
    sort_letter = sorted(counts.keys())
    result = [f"{letter} {counts[letter]}"for letter in sort_letter]
    return result
print(count_characters("hello world"))  
# ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]
print(count_characters("I love coding challenges!")) 
 # ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"]
print(count_characters("// TODO: Complete this challenge ASAP!"))
# ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"]