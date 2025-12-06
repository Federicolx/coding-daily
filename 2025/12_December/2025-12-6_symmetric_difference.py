'''
Title:Symmetric Difference
Date:2025-12-6
Source: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-12-06
Description:
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.

Examples:
Waiting:1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
Waiting:2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
Waiting:3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
Waiting:4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].
'''
def difference(arr1, arr2):
    result = []
    for n1 in arr1:
        if n1 not in arr2:
            result.append(n1)
    for n2 in arr2:
        if n2 not in arr1:
            result.append(n2)
    return result

difference([1, 2, 3], [3, 4, 5])
difference(["a", "b"], ["c", "b"])
difference([1, "a", 2], [2, "b", "a"])
difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
