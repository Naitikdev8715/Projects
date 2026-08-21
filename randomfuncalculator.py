import random
import time

print("🤖 Welcome to the CHAOS CALCULATOR 3000! 🤖")
time.sleep(1)

# Get user input
try:
    num1 = float(input("Enter your first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter your second number: "))
except ValueError:
    print("That's not even a number! Error 404: Brain not found.")
    exit()

# Add random chaos factor
chaos = random.randint(-5, 5)

# Perform operations with a twist
if op == "+":
    result = num1 + num2 + chaos
    msg = f"Adding {num1} and {num2}... Plus a secret chaos bonus of {chaos}!"
elif op == "-":
    result = num1 - num2 - chaos
    msg = (
        f"Subtracting {num2} from {num1}... I also took away a random {chaos}"
        " just for fun!"
    )
elif op == "*":
    # Multiply by a funny multiplier if they try to multiply by 0
    mult = random.randint(1, 10) if num2 == 0 else num2
    result = num1 * mult
    msg = f"Multiplying... wait, I changed your second number to {mult} because I felt like it!"
elif op == "/":
    if num2 == 0:
        result = "infinity and beyond 🚀"
        msg = "Dividing by zero? Breaking the laws of physics!"
    else:
        result = (num1 / num2) + (chaos / 10)
        msg = f"Dividing... adjusted slightly by a vibe check of {chaos / 10}."
else:
    msg = "I do not know this operator. You broke my feelings."
    result = "❌ ERROR"

print("\nCalculating...")
time.sleep(1.5)
print(msg)
print(f"✨ Final Answer: {result} ✨")
