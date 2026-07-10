num = int(input("Enter your number: "))
sum = 0
temporary = num
while temp > 0:
    number = temporary%10
    sum = sum + number**3
    temp = temporary//10
if num == sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")