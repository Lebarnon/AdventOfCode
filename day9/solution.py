SURROUNDING_COORDINATES = {
  (1,-1),  (1,0),  (1,1),
  (0,-1),  (0,0),  (0,1),
  (-1,-1), (-1,0), (-1,1),
}
DIAGONALS = {(1,-1), (1,1), (-1,-1), (-1,1)}
NON_DIAGONALS = {(1,0), (0,1), (-1,0), (0,-1)}

def isTouching(hPos, tPos):
  hX, hY = hPos
  tX, tY = tPos
  coorDiff = (tX-hX, tY-hY)
  return True if coorDiff in SURROUNDING_COORDINATES else False

def move(pos, dir):
  if(dir == "U"):
    pos[1] += 1
  elif(dir == "R"):
    pos[0] += 1
  elif(dir == "D"):
    pos[1] -= 1
  else:
    pos[0] -= 1
  return pos

def catchUp(hPos, tPos):
  hX, hY = hPos
  tX, tY = tPos
  if(hX != tX and hY != tY):
    for (x,y) in DIAGONALS:
      tempTPos = [tPos[0]+x, tPos[1]+y]
      if(isTouching(hPos, tempTPos)):
        return tempTPos
  else:
    for (x,y) in NON_DIAGONALS:
      tempTPos = [tPos[0]+x, tPos[1]+y]
      if(isTouching(hPos, tempTPos)):
        return tempTPos

def part1(motions):
  tPosHistory= set([(0,0)]) #add starting pos
  hPos = [0,0]
  tPos = [0,0]
  for motion in motions:
    dir, times = motion.split(" ")
    times = int(times)
    while(times>0):
      hPos = move(hPos, dir)
      if(not isTouching(hPos, tPos)):
        tPos = catchUp(hPos, tPos)
        tPosHistory.add(tuple(tPos))
      times -=1
  print(len(tPosHistory))

def part2(motions):
  knotsPos = [[0,0] for _ in range(10)]
  lastKnotHistory = set([(0,0)])
  for motion in motions:
    dir, times = motion.split(" ")
    times = int(times)
    while(times>0):
      knotsPos[0] = move(knotsPos[0], dir)
      for i in range(9):
        frontKnot = knotsPos[i]
        backKnot = knotsPos[i+1]
        if(not isTouching(frontKnot, backKnot)):
          knotsPos[i+1] = catchUp(frontKnot, backKnot)
      lastKnotHistory.add(tuple(knotsPos[9]))
      times -=1
  print(len(lastKnotHistory))

input = open('day9/input.txt').read()
motions = input.splitlines()
part1(motions)
part2(motions)


    

