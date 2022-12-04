# Part 1
def judgeRound(i, j):
  iOffset = ord(i) - ord('A')
  jOffset = ord(j) - ord('X')
  # check if draw
  if(iOffset == jOffset):
    return jOffset+1 + 3
  # check if won
  if((iOffset+1)%3 == jOffset):
    return jOffset+1 + 6
  # means lose
  return jOffset+1 + 0

# Part 2
def judgeRoundV2(i, j):
  iOffset = ord(i) - ord('A')
  jOffset = ord(j) - ord('X')

  # need to lose
  if(jOffset == 0):
    return (iOffset-1)%3+1 + 0
  # need to draw
  if(jOffset == 1):
    return iOffset+1 + 3
  # need to win
  if(jOffset == 2):
    return (iOffset+1)%3+1 + 6

## main
data = None
with open('./input.txt') as f:
  data = f.read().splitlines()

# part 1
total = 0
for d in data:
  total += judgeRound(d[0], d[2])
print(total)

# part 2
total2 = 0
for d in data:
  total2 += judgeRoundV2(d[0], d[2])
print(total2)






  
  