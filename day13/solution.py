def initSignals(input):
  signalsInput = input.split("\n\n")
  signals = []
  for sInput in signalsInput:
    l, r = sInput.splitlines()
    signals.append([l, r])
  return signals

def stringToQueue(input):
  # remove outer brackets
  input = input[1:-1]
  bracketQueue = []
  resultQ = []
  i=0
  cur = ""
  while(i<len(input)):
    if(input[i] == ","):
      resultQ.append(cur)
      cur = ""
    elif(input[i] == "["):
      bracketQueue.append("[")
      cur += input[i]
      while(len(bracketQueue)>0):
        i += 1
        cur += input[i]
        if(input[i] == "["):
          bracketQueue.append("[")
        if(input[i] == "]"):
          bracketQueue.pop()
    else:
      cur += input[i]
    i += 1
  if len(cur) > 0:
    resultQ.append(cur)
  return resultQ
def checkList(leftList, rightList):
  # init queues
  leftQ = []
  rightQ = []
  # populate queues
  leftQ.extend(stringToQueue(leftList))
  rightQ.extend(stringToQueue(rightList))

  while len(leftQ) > 0 and len(rightQ) > 0:
    left = leftQ.pop(0)
    right = rightQ.pop(0)
    decision = 0 # 0=continue, -1=wrong, 1=right
    if(left[0] == '[' or right[0] == '['):
      if(left[0] != '['):
        left = '[' + left + ']'
      elif(right[0] != '['):
        right = '[' + right + ']'
      decision = checkList(left, right)
    else:
      if(left>right):
        decision = -1
      elif(left == right):
        decision = 0
      else:
        decision = 1
    #check decision
    if(decision == 0):
      continue
    else:
      return decision

  if(len(leftQ) < len(rightQ)):
    return 1
  elif(len(leftQ) > len(rightQ)):
    return -1
  else:
    return 0

def part1(signals):
  results = []
  for signal in signals:
    results.append(checkList(signal[0], signal[1]))
  print(results)
  indicesSum = 0
  for i,r in enumerate(results):
    if r==1:
      indicesSum += i+1
  print(indicesSum)
  

# main
input = open("day13/input.txt").read()
signals = initSignals(input)
part1(signals)
