data = None
with open('input.txt') as f:
  data = f.read().splitlines()

# Part 1
# initialise stacks
stacks = [[] for i in range(9)]

for (i,n) in enumerate(data[8]): # stack numbers
  if(n.isnumeric()):
    for d in data[7::-1]:
      if(d[i] != " "):
        stacks[int(n)-1].append(d[i])

# execute moving instructions (inst)
for d in data[10:]:
  inst = [int(x) for x in d.split(" ") if x.isnumeric()]
  for i in range(inst[0]):
    temp = stacks[inst[1]-1].pop()
    stacks[inst[2]-1].append(temp)

answer = ""
for stack in stacks:
  if (len(stack) > 0):
    answer += stack.pop()
print(answer)


# part 2
# initialise stacks
stacks = [[] for i in range(9)]

for (i,n) in enumerate(data[8]): # stack numbers
  if(n.isnumeric()):
    for d in data[7::-1]:
      if(d[i] != " "):
        stacks[int(n)-1].append(d[i])

# execute moving instructions (inst)
for d in data[10:]:
  inst = [int(x) for x in d.split(" ") if x.isnumeric()]
  source = stacks[inst[1]-1]
  stacks[inst[2]-1].extend(source[-1 * inst[0]:])
  stacks[inst[1]-1] = source[:-1*inst[0]]

answer = ""
for stack in stacks:
  if (len(stack) > 0):
    answer += stack.pop()
print(answer)