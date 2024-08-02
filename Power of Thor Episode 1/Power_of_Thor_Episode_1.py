"""
Name        : Power of Thor - Episode 1
Date        : 30/07/2024
Author      : Noureddine Bouyguir
Description : A basic problem to go a little bit further 
              with conditions and variables: your program 
              must allow Thor to reach the coordinates of 
              the light of power in a 2D field.
"""

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
x,y=initial_tx, initial_ty

while True:
    remaining_turns = int(input()) 

    res_x=""
    res_y=""
    if x<light_x:
        res_x="E"
        x+=1
    elif x>light_x:
        res_x="W"
        x+=1
    if y<light_y:
        res_y="S"
        y+=1
    elif y>light_y:
        res_y="N"
        y+=1

    print(res_y+res_x)
