def part1(input):
  seq = []
  for (i,c) in enumerate(input):
    if(c in seq):
      seq = seq[seq.index(c)+1:]
    seq.append(c)
    if(len(seq) == 4):
      return i+1
  return None

def part2(input):
  seq = []
  for (i,c) in enumerate(input):
    if(c in seq):
      seq = seq[seq.index(c)+1:]
    seq.append(c)
    if(len(seq) == 14):
      return i+1
  return None

with open('input.txt') as f:   
  input = f.read()
  print(part1(input))
  print(part2(input))


