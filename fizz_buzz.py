# This method takes in  number max and returns an array containing
# all numbers greater than 0 and less than max that are divisible
# by either 4 or 6, but not both



##### SOLUTION 1

# def fizz_buzz(max):
#     newList = []
#     for i in range(1, max):
#         if (i % 6 == 0) or (i % 4 == 0):
#             newList.append(i)
#         if (i % 6 == 0) and (i % 4 == 0):
#             newList.remove(i)
        
#     return newList

# print(fizz_buzz(100))




##### SOLUTION 2

# def fizz_buzz(max):
#     newList = []
#     i = 1
#     while i < max:
#         if (i % 6 == 0) or (i % 4 == 0):
#             if not (i % 6 == 0) and (i % 4 == 0):
#               newList.append(i)
#         i += 1
#     return newList

# print(fizz_buzz(100))
