#!/usr/bin/python3

for num in range(1,101):
    if num % 7 == 0 or num % 10 == 7 or num // 10 == 7 :
        continue
    else :
        print(num)

