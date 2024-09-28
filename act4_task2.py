income = float(input("Enter your annual income in PHP: "))

if income <= 250000:
    tax = 0.00
elif income <= 400000:
    tax = income * 0.20
elif income <= 800000:
    tax = 30000 + (income * 0.25)
else:
    tax = 130000 + (income * 0.30)

print(f"Tax Amount: {tax:.2f} PHP")
