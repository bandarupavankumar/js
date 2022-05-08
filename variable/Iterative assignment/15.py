##15.Write a Python program to print Fibonacci number series upto a given number
n=int(input("Enter the number:"))
a=0
b=1
sum=0
count=1
while count<=n:
    print(sum)
    count=count+1
    a=b
    b=sum
    sum=a+b
    print("fibonacci series :",end="")