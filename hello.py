
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

def newCode(a,b):
        return a+b, a-b, a*b

print(newCode(3,5))
