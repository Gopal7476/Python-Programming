# Find the Factors of a Number.

num = int(input())
for i in range(2, num//2 + 1):
    if(num % i == 0):
        print(i, end = " ")