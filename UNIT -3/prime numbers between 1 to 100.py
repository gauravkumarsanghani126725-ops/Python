# Write a program to print all prime numbers between 1 to 100
# Roll Number : 92400527141 Name : Gaurav

for num in range (1,101):
    if num > 1 :
        flag = 0

        for i in range (2,num):
            if num % i == 0:
                flag = 1
                break

        if flag == 0 :
            print(num , end= " ")
