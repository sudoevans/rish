import math
def isPentagonalNumber(n):
    if (1 + math.sqrt(1 + 24 * n)) % 6 == 0:
        return True
    else:
        return False

def main():
    for i in range(1, 101):
        if isPentagonalNumber(i):
            print(i, end = " ")
        if i % 10 == 0:
            print()
main()