import calendar

print("📅 All Month Names:")

# Loop through month numbers 1 to 12
for month_index in range(1, 13):
    # calendar.month_name is an array-like object where index 1 is January
    print(f"- {calendar.month_name[month_index]}")
