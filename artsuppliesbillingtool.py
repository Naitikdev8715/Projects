def greet_customer():
    print("Welcome to Naitik Art Store!")
    print("Providing art and craft supplies for you!")
greet_customer()
price_per_supply = float(input("Enter the number of items bought: "))
cost_per_supply = int(input("Enter the price per item: "))
def calculate_price(price, supplies):
    total = price * supplies
    return total
total_cost = calculate_price(price_per_supply, cost_per_supply)
round_total = round(total_cost, 2)
print("The total cost is ", round_total)

amount_paid = int(input("Enter the amount paid by the customer: "))
def calculate_supply(paid, total):
    change = paid - total
    return change
change_due = calculate_supply(amount_paid, round_total)
def thank_you_message(supplies):
    if supplies >= 5:
        return "Wow! Big order! Thank you so much for your order."
    else:
        return "Thank you for your order"
closing_statement = thank_you_message(cost_per_supply)
print("")
print("=====NAITIK'S ART STORE RECIEPT=====")
print("Total items: ", price_per_supply)
print("Price per item:", cost_per_supply)
print("Total price: ", round_total)
print("Amount paid: ", amount_paid)
print("Change due: ", change_due)
print(closing_statement)
print("================")