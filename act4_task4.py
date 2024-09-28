weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    advice = "You need to gain weight for better health."
elif bmi < 24.9:
    advice = "You are maintaining a healthy weight. Keep it up!"
elif bmi < 29.9:
    advice = "Consider adopting a healthier lifestyle."
else:
    advice = "It is advisable to consult a healthcare provider."

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Health Advice: {advice}")
