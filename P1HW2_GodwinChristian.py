# Christian Godwin
# 03/01/2026
# P1HW2 - Travel Budget
# This program calculates travel expenses and shows the remaining balance 
# after subtracting gas, accommodation, and food costs from the budget.

"""
Pseudocode:

1. Display program title
2. Ask user to enter budget
3. Ask user to enter travel destination
4. Ask user to enter amount for gas
5. Ask user to enter amount for accommodation
6. Ask user to enter amount for food
7. Add gas, accommodation, and food to get total expenses
8. Subtract total expenses from budget to get remaining balance
9. Display formatted results
"""

# Display program title
print("This program calculates and displays travel expenses\n")

# Get user inputs
budget = float(input("Enter Budget: $"))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? $"))
accommodation = float(input("How much will you spend on accommodation? $"))
food = float(input("How much will you spend on food? $"))

# Calculate expenses
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"\nFuel: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print(f"\nTotal Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
