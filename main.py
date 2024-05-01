print("BMI Calculator")
try:
    height = float(input("Enter Your Height (in meters): "))
    weight = float(input("Enter Your Weight (in kilograms): "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi}")
except ValueError:
    print("Invalid input. Please enter a valid number.")


