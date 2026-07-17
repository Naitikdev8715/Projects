print("Inventory Stock counter")
print("Dispensing stock for customers one at a time\n")
stocks = [500,200, 100, 50, 20, 10]
customers_served = 0
total_dispensed = 0
log = []
serving = True
while serving:
    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}! Enter your stock amount: "))
    if amount <= 0:
        print("Invalid stock! please enter a positive stock\n")
        continue
    print(f"\n Dispensing {amount} units for {name}")
    remaining = amount
    i = 0
    used = {}
    while i < len(stocks):
        count = remaining//stocks[i]
        if count > 0:
            print("Unit notes= ", count*stocks[i])
            used[stocks[i]]= count
            remaining = remaining-(count*stocks[i])
        i = i + 1
    customers_served += 1
    total_dispensed += amount
    print("Transaction complete! Please collect your stocks", name)
    again = input("Next item? (1)yes (2)no: ").strip().lower()
    if again != "yes":
        serving= False
print("\n Daily denomination report")
for note in stocks:
    total_stocks = 0
    for entry in log:
        total_stocks += entry["used"].get(note,0)
    if total_stocks > 0:
        print(f"{note} unit notes dispensed today: {total_stocks}")
print("Customers served", customers_served)
print("Total dispensed units", total_dispensed)
print("Inventory session closed. Goodbye!")