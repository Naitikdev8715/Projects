def palindrome(x):
    end = len(x)-1
    start = 0
    while (start<end):
        if (x[start]!=x[end]):
            return False
        start = start + 1
        end = end - 1
    return True
x = (1,2,1)
#palindrome is a number that is same when read from both left and right
if (palindrome(x)):
    print("The tuple is a palindrome number")
else:
    print("The number is not a palindrome number")