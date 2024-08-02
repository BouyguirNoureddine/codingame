"""
Name        : Onboarding
Date        : 30/07/2024
Author      : Noureddine Bouyguir
Description : A tutorial mission for all newcomers: your program
              must find which of the two targets is the closest.
"""

while True:
    enemy_1 = input()
    dist_1 = int(input()) 
    enemy_2 = input() 
    dist_2 = int(input())

    res=enemy_2 if dist_1>dist_2 else enemy_1 if dist_1<dist_2 else enemy_1

    print(f"{res}")
