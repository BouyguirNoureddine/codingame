"""
Name        : The Descent
Date        : 30/07/2024
Author      : Noureddine Bouyguir
Description : A simple problem to try out the CodinGame platform: your program
              must find the highest mountain out of a list of mountains.
"""

while True:
    maxs=0
    for i in range(8):
        mountain_h = int(input())
        if mountain_h>=0 and mountain_h<=9:
            if mountain_h>maxs:
                maxs=mountain_h
                y=i

    print(y)
