##8. Write a Python Program to print the greatest number in given three numbers?
a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
c=int(input("Enter a Third number:"))
largest=0
if a>b and a>c:
    largest=a
if b>a and b>c:
    largest=b
if c>a and c>b:
    largest=c
print("is the largest of three numbers:",largest)            
    


