import time
'''
Any live incell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
'''
#reading in coordinates from a provided file
#list of lists to store all of the cells. False/True
#printing grid
#function checks what a cell should be changed to and Counts neighbors 
#while loop to keep the game running forever
filename = input("Type in the the file you would like to start with: ")
f = open(filename)
inputReadLines = f.readlines()
stripped = [l.strip() for l in inputReadLines]
#print(stripped)

c = []
for pair in stripped:
  c.append(pair.split())
#print(c)

status = [] 
for i in range(30):
  y = []
  for j in range(50):
    y.append(False)
  status.append(y)
  
for pair in c:
  status[int(pair[0])][int(pair[1])] = True
#print(status)

def myprint(lst):
  for x in lst:
    new = ''
    for y in x:
      if y == True:
        new +="o"
      else:
        new += "-"
    print(new)
##myprint(status)

def count_neighbors(r, c, celltype, board): #returns wether cell lives or dies
  alive = 0  
  if r-1 >= 0 and c-1 >= 0 and board[r-1][c-1]:
    alive+=1
  if r-1 >= 0 and board[r-1][c]:
    alive+=1
  if r-1 >= 0 and c+1 < len(board[0]) and board[r-1][c+1]:  
    alive+=1
  if c-1 >= 0 and board[r][c-1]:
    alive+=1
  if c+1 < len(board[0]) and board[r][c+1]:
    alive+=1
  if r+1 < len(board) and c-1 >=0 and board[r+1][c-1]:
    alive+=1
  if r+1 < len(board) and board[r+1][c]:
    alive+=1
  if r+1 < len(board) and  c+1 < len(board[0]) and board[r+1][c +1]:
    alive+=1
    
#Any live incell with fewer than two live neighbours dies, as if by underpopulation.

  if celltype == True and (alive < 2):
    return False
    
  if celltype == True and (alive == 2 or alive ==3):
    return True
    
  if celltype == True and (alive > 3):
    return False
    
  if celltype == False and (alive == 3):
    return True
  
  return celltype
  
  
  
print("Welcome to Conway's Game of Life. We start with a 30 x 50 grid of cells, either alive or dead. Here are the rules: \n 1) Any live cell with fewer than two live nieghbors dies, as if by underpopulation. \n 2) Any live cell with two or three live neighbors lives on to the next generation. \n 3) Any live cell with more than three live neighbors dies, as if by overpopulation. \n 4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.")
input("press Enter to continue: ")

while True:
  new = [] 
  for i in range(30):
    y = []
    for j in range(50):
      y.append(False)
    new.append(y)
  
  for i in range(len(status)):
    for j in range(len(status[i])):
      new[i][j] = count_neighbors(i, j, status[i][j], status)
      
  status = new
  myprint(status)
  
  input(" ")
