def initHill(input):
  input = input.splitlines()
  rows = len(input)
  cols = len(input[0])
  hillGrid = []
  start = highest = (0,0)

  for j,line in enumerate(input):
    hillRow = []
    for i,c in enumerate(line):
      if(c == "S"):
        start = (i,j)
      elif(c == "E"):
        highest = (i,j)
      hillRow.append(c)
    hillGrid.append(hillRow)
  return [hillGrid, start, highest]

def part1(hillGrid, start, highest):
  DIRECTION = [(0,1), (1,0), (0,-1), (-1,0)]  
  visited = set()

  def canClimb(hillGrid, curPos, nextPos):
    curX, curY = curPos
    nextX, nextY = nextPos
    if(abs(ord(input[curX][curY])-ord(input[nextX][nextY])) <=1):
      return True
    else:
      return False

  def climb(hillGrid, curPos, highest):
    if(curPos in visited):
      return float("inf")
    elif(curPos == highest):
      return 1
    
    rows = len(hillGrid)
    cols = len(hillGrid[0])
    visited.add(curPos)
    minStep = float("inf")
    for x,y in DIRECTION:
      nextX, nextY = curPos[0]+x, curPos[1]+y
      if(nextX>=0 and nextX<rows and nextY>=0 and nextY<cols):
        if(canClimb(hillGrid, curPos, (nextX, nextY))):
          steps = climb(hillGrid, (nextX, nextY), highest)
          minStep = min(minStep, steps)
    visited.remove(curPos)
    return minStep+1

  minStep = climb(hillGrid, start, highest)
  print(minStep)

# main
input = open('day12/test.txt').read()
hillGrid, start, highest = initHill(input)
part1(hillGrid,start,highest)