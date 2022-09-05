n=int(input("enter a number"))
ct=0
if n<0:
    n=-1*n
if n==0:
    ct=1
while n!=0:
    n=n//10
    ct+=1
print("number of digit:",ct)