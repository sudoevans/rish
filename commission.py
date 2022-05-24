# def computeComission(salesAmount):
#     if salesAmount <= 5000:
#         return salesAmount * 0.08
#     elif salesAmount >= 5000 and salesAmount <=10000:
#         return salesAmount * 0.1
#     else:
#         return salesAmount * 0.12

# # Test cases:
# value1=computeComission(10000)
# value2=computeComission(15000)
# value3=computeComission(95000)
# value4=computeComission(100000)
# print(value1,value2,value3,value4)
n = 1
while n <= 100:
    print(int(n*(3*n-1)/2), end = " ")
    n = n + 1
    if n % 10 == 0:
        print()
