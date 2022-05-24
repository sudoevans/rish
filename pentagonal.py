# import math
# def isPentagonalNumber(n):
#     if (1 + math.sqrt(1 + 24 * n)) % 6 == 0:
#         return True
#     else:
#         return False

# def main():
#     for i in range(1, 101):
#         if isPentagonalNumber(i):
#             print(i, end = " ")
#         if i % 10 == 0:
#             print()
# main()


# The expected code:

n = 1
while n <= 100:
    print(int(n*(3*n-1)/2), end = " ")
    n = n + 1
    if n % 10 == 0:
        print()
