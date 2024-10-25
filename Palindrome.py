#palindrome is a number which gives same value when we read from start to end or end to start

a = input("Enter a number :   ")
 # we need to take slicing method here for reverse the value
reverse = a[::-1]  #slicing methos [start point,end point, -1s]
if (a==reverse):
    print(a, " is a Palindrome number")
else : 
    print(a , "it is not a palindrome number")