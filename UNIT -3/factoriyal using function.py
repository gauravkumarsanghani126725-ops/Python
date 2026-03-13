# Write a program to print factorial number using function
# Roll Number : 92400527141 Name : Gaurav

def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact * i
    return fact
        
n = int(input("Enter the number :"))


f= factorial(n)
print(f"FACTORIYAL of {n} is {f}")
