# Write a program to input age of person and display message as follows 
# Roll Number : 92400527141 Name : Gaurav

print(" input age of person and display message")

age = int(input("Enter age "))

if age < 12 :
    print("You are Kid ")
elif age >= 12 and age <= 17:
    print("You are teenager")
elif age >= 18 and age <= 60:
    print(" you are Adult ")
else :
    print("you are Senior Citizen ")
