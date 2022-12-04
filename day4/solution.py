# part 1
data = None
with open('./input.txt') as f:
    data = f.read().splitlines()

count = 0
for d in data:
    pairRange = d.split(',')
    for i in range(len(pairRange)):
        pairRange[i] = [int(x) for x in pairRange[i].split('-')]
    
    if(pairRange[0][1] - pairRange[0][0] > pairRange[1][1] - pairRange[1][0]): #left range larger than right
        if(pairRange[1][0] >= pairRange[0][0] and pairRange[1][1] <= pairRange[0][1]):
            count += 1
    else:
        if(pairRange[0][0] >= pairRange[1][0] and pairRange[0][1] <= pairRange[1][1]):
            count += 1
print(count)

# part 2
count = 0
for d in data:
    pairRange = d.split(',')
    for i in range(len(pairRange)):
        pairRange[i] = [int(x) for x in pairRange[i].split('-')]
    
    if(pairRange[0][0] <= pairRange[1][1]): #left min smaller than right max
        if(pairRange[0][1] >= pairRange[1][0]): # left max larger than right min
            count += 1
print(count)