def part1(signals):
  targetCycle = {20,60,100,140,180,220}
  totalStrength = 0
  clockCycle = 0
  regX = 1
  def incrementClock():
    nonlocal totalStrength
    nonlocal clockCycle
    clockCycle+=1
    if(clockCycle in targetCycle):
      totalStrength += clockCycle*regX

  for signal in signals:
    inst = signal.split(" ")
    if(inst[0] == "noop"):
      incrementClock()
      continue
    if(inst[0] == "addx"):
      incrementClock()
      incrementClock()
      regX += int(inst[1])
  print(totalStrength)

def part2(signals):
  targetCycle = {40,80,120,160,200,240}
  clockCycle = 0
  offSet = 0
  regX = 1
  def incrementClock():
    nonlocal regX
    nonlocal clockCycle
    nonlocal offSet
    clockCycle+=1

    print("#", end="") if clockCycle-offSet-1 in {regX-1, regX, regX+1} else print(".", end="")

    if(clockCycle in targetCycle):
      offSet = clockCycle
      print("")

  for signal in signals:
    inst = signal.split(" ")
    if(inst[0] == "noop"):
      incrementClock()
      continue
    if(inst[0] == "addx"):
      incrementClock()
      incrementClock()
      regX += int(inst[1])
input = open('day10/input.txt').read()
signals = input.splitlines()
# part1(signals)
part2(signals)
