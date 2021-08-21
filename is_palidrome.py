# A palidrome is a word, or sentence, or number, etc that reads the same backward and forward
# This method takes in a string word and returns true if the word is a palidrome,
# false otherwise.




##### SOLUTION 1

# def is_palidrome(word):
#     # converts the word into a list - this can be done in two ways: 
#     # wordList = list(word)
#     wordList = word.split()
#     # reverse the order of the list 
#     wordList.reverse()
#     # convert the list back into a string
#     reversedWord = ''.join(wordList)
#     return reversedWord == word

# print(is_palidrome("racecar"))



##### SOLUTION 2

# def is_palidrome(word):
#     # reversing a string using a slice statement
#     # this means start at the end of the string and end at index 0, while going -1 through the string
#     return word == word[::-1]

# print(is_palidrome("rawecar"))



##### SOLUTION 3

# importing modules - this can be done in two ways

# import functools - therefore, the reduce function would have to be called like, e.g. functools.reduce(..) 
# OR
# from functools import reduce 
# # if import is done like this then the reduce function can be called on its own. e.g. reduce(..)

# def is_palidrome(word):
#     wordList = []
#     reversedList = []

#     length = len(word)
#     # converting string to list using iteration
#     for i in range(length):
#         wordList.append(word[i])

#     # reversing contents of a list using iteration
#     while length > 0:
#         reversedList.append(wordList[length -1])
#         length -= 1
#     # converting list to string using the reduce function, which takes up a lambda function as an argument
#     joinedWord = reduce(lambda a , b : a + b , reversedList)
#     return joinedWord == word

# print(is_palidrome("racecar"))