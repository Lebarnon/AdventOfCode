# Part 1
def getPriority(a):
  if(a.isupper()):
    return ord(a) - ord('A') + 27
  else:
    return ord(a) - ord('a') + 1


with open('input.txt') as f:
    data = f.read().splitlines()
    total = 0
    for d in data:
      inLeft = set()
      inRight = set()
      common = set()
      i=0
      j=int(len(d)/2)
      while(j<len(d)):
        inLeft.add(d[i])
        inRight.add(d[j])

        if(d[j] in inLeft):
          common.add(d[j])
        if(d[i] in inRight):
          common.add(d[i])
        i += 1
        j += 1

      for c in common:
        total += getPriority(c)

    print(total)
        

with open('input.txt') as f:
    data = f.read().splitlines()
    total = 0
    for (i,d) in enumerate(data):
      if(i%3 == 0):
        elf1 = set()
        for c in d:
          elf1.add(c)
        continue
      if(i%3 == 1):
        elf2 = set()
        for c in d:
          if c in elf1:
            elf2.add(c)
        continue
      if(i%3 == 2):
        elf3 = set()
        for c in d:
          if c in elf2:
            elf3.add(c)
        for c in elf3:
          total += getPriority(c)

    print(total)
      