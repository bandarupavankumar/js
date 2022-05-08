##13.Write a Python program to print the reverse of digits of numbers
n=int(input("Enter the integer number:"))
revs_number=0
while n>0:
    remainder=n%10
    revs_number=(revs_number*10)+remainder
    n=n//10
    print("reverse number is:",revs_number)
