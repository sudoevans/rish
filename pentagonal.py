#! python3
# Code to display first 100 pentagonal numbers Withoud using Math Module

n = 1
while n <= 100:
    print(int(n*(3*n-1)/2), end = " ")
    n = n + 1
    if n % 10 == 0:
        print()
