'''
Title:Markdown Ordered List Item Converter  
Date:2025-12-4
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-03
Description:
Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

Start with zero or more spaces, followed by
A number (1 or greater) and a period (.), followed by
At least one space, and then
The list item text.
If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

Examples:
Waiting:1. convert_list_item("1. My item") should return "<li>My item</li>".
Waiting:2. convert_list_item(" 1.  Another item") should return "<li>Another item</li>".
Waiting:3. convert_list_item("1 . invalid item") should return "Invalid format".
Waiting:4. convert_list_item("2. list item text") should return "<li>list item text</li>".
Waiting:5. convert_list_item(". invalid again") should return "Invalid format".
Waiting:6. convert_list_item("A. last invalid") should return "Invalid format".
'''

def convert_list_item(markdown):
    str = markdown.lstrip()
    number_str = ""
    index = 0
    while index < len(str) and str[index].isdigit():
        number_str += str[index]
        index += 1
    if not number_str or int(number_str) < 1:
        return "Invalid format"
    if index >= len(str) or str[index] != '.':
        return "Invalid format"
    
    index += 1

    if index >= len(str) or str[index] != ' ':
        return "Invalid format"
    
    while index < len(str) and str[index] == " ":
        index += 1
        
    text = str[index:]
    return "<li>" + text + "</li>"

print(convert_list_item("1. My item"))               # <li>My item</li>
print(convert_list_item(" 1.  Another item"))        # <li>Another item</li>
print(convert_list_item("1 . invalid item"))         # Invalid format
print(convert_list_item("2. list item text"))        # <li>list item text</li>
print(convert_list_item(". invalid again"))          # Invalid format
print(convert_list_item("A. last invalid"))          # Invalid format

