"""
Name        : There is no Spoon - Episode 1
Date        : 04/08/2024
Author      : Noureddine Bouyguir
Description : The game is played on a rectangular grid with a given size. 
              Some cells contain power nodes. The rest of the cells are empty.
              The goal is to find, when they exist, the horizontal and vertical
              neighbors of each node
"""

lines=[]
grid=[]
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line= input()  # width characters, each either 0 or .
    lines.append(list(line))
for line in lines:
    l= [line[i] for i in range(len(line)) if line[i] !=" "]
    grid.append(l)

for y in range(height):
    for x in range(width):
        #Checking Cell
        if grid[y][x]=="0":
            x1,y1=x,y
            x2=y2=x3=y3=-1
            #Checking Right Neighbour
            for j in range(width-1,x1,-1):
                if grid[y1][j]=="0":
                    x2=j
                    y2=y
            #Checking Left Neighbour
            for k in range(height-1,y1,-1):
                if grid[k][x1]=="0":
                    x3=x1
                    y3=k
            print(x1,y1,x2,y2,x3,y3)






