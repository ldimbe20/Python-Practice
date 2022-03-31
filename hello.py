
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 5 to 10, print Weird



# def conditional_test(n):
#     if n % 2 != 0:
#         return "Weird"
#     if (n % 2 == 0) and (n in range(2, 5)):
#         return "Not Weird"
#     if (n % 2 == 0) and (n in range(5, 10)):
#         return "Weird"
#     else:
#         return "Number is not within range"
    

# print(conditional_test(26))

# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division, a //b . The second line should contain the result of float division,  a/b .

# No rounding or formatting is necessary.

# def division_integer(a, b):
#     return a//b
   
# def division_float(a, b):
#     return a/b
   
# print(division_float(10, 3))   
    
# print(division_integer(10, 2))

# def newCode(a,b):
#         return a+b, a-b, a*b

# print(newCode(3,5))

#lists can store different data types arrays [] can only store one data type

#Creating a for in loop with using range

# def square_number(n):
#     squares = []
#     for i in range(n +1):
#         squares.append(i * i)
#     return squares
        
        
# print(square_number(10))

# def range_number(n,b):
#     squares = []
#     for i in range(n, b+1):
#         squares.append(i * i)
#     return squares

# print(range_number(10,12))




# new_list=[ x for x in range(10)]

# print(new_list)

# #filtered_list = [ x for x in range(50) if x % 2 == 0 if x % 5 == 0]
# #print(filtered_list)

#!Using List comprehensions

from asyncore import loop


names=["lauren", "Ally", "Kirstin", "Tina"]

# # l_names= [name for name in names if name.startswith("l")] 

# print(l_names)

def L_names(name):
    lnames = []
    for i in name:
        if i.startswith("l"):
                lnames.append(i)
        return lnames
    
    

print(L_names(names))

# def new_number(b):
#         numbers_10 = [x for x in range(b) if x > 3]
#         return (numbers_10)
               
# print (new_number(7))

# #Turn below into list comprehension
# j=[0,1,2,3,4,5]
# # 

# def loopFunction(list):
#     plus_six=[]
#     # iterates through the list, the range is set to the length of the list
#     for x in range(len(list)):
#         if x < 3:
#             x += 6 
#             plus_six.append(x)
#     return plus_six  
# print(loopFunction(j))


j=[0,1,2,3,4,5]



# # 
def loopFunction(list):
        plus_six = [number for number in list if number < 3 ]
        return plus_six

print(loopFunction(j))