#odd or even
number= int(input("Enter a number to check: "))
if number%2==0:
    print("The number is even")
else:
    print("The nuumber is odd")


#BMI calculator
height= float(input("Enter your height in cm: "))
weight= float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is: ", BMI)

if BMI<=18.4:
    print("You are underweight")
elif BMI <=24.9:
    print("You are healthy")
elif BMI <= 34.9:
    print("You are over wight")
elif BMI <= 39.9:
    print("You are severely over wight")
else:
    print("You are severely obese")