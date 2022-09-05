#6. Write a python script which takes a three digit number from the user and displays only its middle digit.

a=int(input("enter a three digit number"))
a=a//10
a=a%10
print(a)