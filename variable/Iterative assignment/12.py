##12.Write a Python program Factors of 24 using while loop
n=int(input("Enter a Number:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
        i=i+1
