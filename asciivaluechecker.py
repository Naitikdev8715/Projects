print("ASCII Value Checker")
char = input("Enter a single character: ")
if type(char) is str and len(char)== 1:
    ascii_val = ord(char)
    print(f"ASCII Value: {ascii_val}")
    if ascii_val>= 48 and ascii_val<= 57:
        print("It is a number")
    elif ascii_val>= 65 and ascii_val<= 90:
        print("It is an Uppercase letter")
    elif ascii_val>= 97 and ascii_val<= 122:
        print("It is a lowercase letter")
    elif ascii_val == 32:
        print("It is a Space")
    else:
        print("It is a special character")
else:
    print("Enter character of length 1")