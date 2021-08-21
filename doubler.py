# This method takes up a list of numbers and returns a new list 
# where every element of the original list is multiplied by 2


##### SOLUTION 1

# def doubler(numbers):
#     # declare an empty list
#     doubledList = []
#     # iterate through the numbers list
#     for i in range(len(numbers)):
#         # at every stage in the iteration, multiply the iteration position number by 2
#         doubledList.append(numbers[i] * 2)
#     return doubledList

# print(doubler([1,2,3,4,5]))


##### SOLUTION 2 

# def doubler(numbers):
#     doubledList = list(map(lambda x : x * 2 , numbers))
#     return doubledList
    
# print(doubler([1,2,3,4,5]))
