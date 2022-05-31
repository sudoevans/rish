#Copy n from N 
s1=input("Enter the 1st string:")
s2=input("Enter the 2nd string:")
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
l1=list(s1)
l2=list(s2)
for i in range(n):
    l2[m+i]=l1[i]
print("".join(l2))