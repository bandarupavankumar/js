##2. Write a program to calculate the sum of the first 10 natural numbers using for Loop- for loop and While loop?
n=int(input("Enter a Number:"))
sum=0
for num in range(1,n+1,1):
    sum=sum+num
    print("sum of first",n,"number is:" ,sum)
    