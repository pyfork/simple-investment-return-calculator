# PEMDAS applies. Left-side gets priority.

# Investment return calculator
entry_price = input("Enter buy price\n")
exit_price = input("Enter sell price\n")

# Turn string from input to decimals/float
entry_price_integer = float(entry_price)
exit_price_integer = float(exit_price)

# Calculate investment return %
roi = (exit_price_integer / entry_price_integer - 1) * 100

# Show return %
print(roi) 