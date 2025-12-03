'''
Title:Camel to Snake
Date:2025-12-3
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-02
Description:
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).

Examples:
1. to_snake("helloWorld") should return "hello_world".
Waiting:2. to_snake("myVariableName") should return "my_variable_name".
Waiting:3. to_snake("freecodecampDailyChallenges") should return "freecodecamp_daily_challenges".
'''

def to_snake(camel):
    result = ""
    for ch in camel:
        if ch >= 'a' and ch <= 'z':
            result += ch
        elif ch >= 'A' and ch <= 'Z':
            result +='_'+ch.lower()
    return result

to_snake("helloWorld")
to_snake("myVariableName")
to_snake("freecodecampDailyChallenges")