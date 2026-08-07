def greet_customer():
    print("Welcome to Shopping discount calculator by Amazon")
    print("Helping you calculate discount of a product")
greet_customer()
valid = False
while not valid:
    try:
        num = int(input("Enter the price of your product: "))
        num1 = int(input("Enter the dicount percentage: "))
        discount =  num1/100 * num
        final_price = num - discount
    except ValueError:
        print("Please enter a valid price or discount percentage")
    else:
        valid = True 
        print("No exception")
        print("Your discount is ", discount)
        print("Your final price is ", final_price)
    finally:
        print("Thank you")