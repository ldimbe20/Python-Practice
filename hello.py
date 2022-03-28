
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 5 to 10, print Weird



def conditional_test(n):
    if n % 2 != 0:
        return "Weird"
    if (n % 2 == 0) and (n in range(2, 5)):
        return "Not Weird"
    if (n % 2 == 0) and (n in range(5, 10)):
        return "Weird"
    else:
        return "Number is not within range"
    

print(conditional_test(26))
