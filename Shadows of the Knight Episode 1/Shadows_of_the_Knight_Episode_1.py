"""
Name        : Shadows of the Knight - Episode 1
Date        : 01/08/2024
Author      : Noureddine Bouyguir
Description : You will look for the hostages on a given 
              building by jumping from one window to 
              another using your grapnel gun. Your goal
              is to jump to the window where the hostages
              are located in order to disarm the bombs. 
              Unfortunately, you have a limited number of 
              jumps before the bombs go off
"""


w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]
min_x,min_y,max_x,max_y=0,0,w,h
while True:
    bomb_dir = input()
    min_x= x0 if "R" in bomb_dir else min_x
    max_x= x0 if "L" in bomb_dir else max_x
    min_y= y0 if "D" in bomb_dir else min_y
    max_y= y0 if "U" in bomb_dir else max_y
    x0,y0=((max_x+min_x)//2),((max_y+min_y)//2)
    print(x0,y0)