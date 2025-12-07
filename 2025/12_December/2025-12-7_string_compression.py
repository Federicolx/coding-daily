'''
Title:String Compression
Date:2025-12-7
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-07
Description:
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".
Examples:
1. compress_string("yes yes yes please") 
should return "yes(3) please".
Waiting:2. compress_string("I have have have apples") 
should return "I have(3) apples".
Waiting:3. compress_string("one one three and to the the the the") 
should return "one(2) three and to the(4)".
Waiting:4. compress_string("route route route route route route tee tee tee tee tee tee") 
should return "route(6) tee(6)".
'''

def compress_string(sentence):
    words = sentence.split()
    result = []
    count = 1
    current_word = words[0]

    for i in range(1,len(words)):
        if words[i] == current_word:
            count += 1
        else:
            if count == 1:
                result.append(current_word)
            else:
                result.append(f"{current_word}({count})")

            current_word = words[i]
            count = 1

    if count == 1:
        result.append(current_word)
    else:
        result.append(f"{current_word}({count})")
    
    return " ".join(result)

print(compress_string("yes yes yes please"))
print(compress_string("I have have have apples"))
print(compress_string("one one three and to the the the the"))
print(compress_string("route route route route route route tee tee tee tee tee tee"))
