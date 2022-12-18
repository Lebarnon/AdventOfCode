def initHill(input):
  input = input.splitlines()
  hillGrid = []
  start = highest = (0,0)

  for i,line in enumerate(input):
    hillRow = []
    for j,c in enumerate(line):
      if(c == "S"):
        start = (i,j)
        hillRow.append('a')
        continue
      elif(c == "E"):
        highest = (i,j)
        hillRow.append('z')
        continue
      hillRow.append(c)
    hillGrid.append(hillRow)
  return [hillGrid, start, highest]

def printGrid(input):
  grid = ""
  for r in range(len(input)):
    for c in range(len(input[0])):
      grid += input[r][c]
    grid += "\n"
  grid += "\n"
  print(grid)

def part1(hillGrid, allStartPos, highest):
  DIRECTION = [(0,1), (1,0), (0,-1), (-1,0)]  

  def canClimb(hillGrid, curPos, nextPos):
    curR, curC = curPos
    nextR, nextC = nextPos
    
    if(ord(hillGrid[curR][curC])-ord(hillGrid[nextR][nextC]) < 2):
      return True
    else:
      return False

  queue = []
  visited = set()
  rows, cols = len(hillGrid), len(hillGrid[0])
  steps = -1

  visualGrid = [["-" for x in range(len(hillGrid[0]))] for x in range(len(hillGrid))]

  queue.append(highest)
  visited.add(highest)

  while len(queue) > 0:
    numOfNodes = len(queue)
    steps +=1
    for i in range(numOfNodes):
      curPos = queue.pop(0)
      
      visualGrid[curPos[0]][curPos[1]] = "X"
      printGrid(visualGrid)

      if curPos in allStartPos:
        print(steps)
        return steps
      
      for r,c in DIRECTION:
        nextR, nextC = curPos[0]+r, curPos[1]+c
        if(nextR>=0 and nextR<rows and nextC>=0 and nextC<cols and (nextR, nextC) not in visited and canClimb(hillGrid, curPos, (nextR, nextC)) ):
          visited.add((nextR, nextC))
          queue.append((nextR, nextC))
  
  print("Cant find path")
  return float("inf")

def part2(hillGrid, highest):
  rows, cols = len(hillGrid), len(hillGrid[0])
  # find all possible starting positions
  allStartPos = set()
  for r in range(rows):
    for c in range(cols):
      if hillGrid[r][c] == 'a':
        allStartPos.add((r,c))
  part1(hillGrid, allStartPos, highest)
  

# main
input = open('day12/input.txt').read()
hillGrid, start, highest = initHill(input)
part1(hillGrid,{start},highest)
part2(hillGrid,highest)