with open("input.txt") as file:
    text = file.read()
    lines = text.split('\n')
    treeMap = [[] for i in range(len(lines))]
    print(treeMap)
    for y in range(len(lines)):
        row = lines[y]
        for x in range(len(row)):
            treeMap[y].append(row[x])
    
    print(treeMap)

#searches in all 4 directions and returns number of directions it can be seen from
def directionalSearch(treeMap,x,y):
    # print("for coordinates",x,y,treeMap[y][x])
    y_length = len(treeMap)
    x_length = len(treeMap[0])

    treeHeight = treeMap[y][x]

    count = 0
    #search up
    north = True
    for n in range(y-1,-1,-1):
        # print("NORTH")
        # print(treeMap[n][x])
        if treeMap[n][x] >= treeHeight:
            # print("ye")
            north = False

    
    #search right
    east = True
    for e in range(x+1,x_length):
        # print("EAST")
        # print(treeMap[y][e])
        if treeMap[y][e] >= treeHeight:
            # print("ye")
            east = False
    
    
  

    #search down
    south = True
    for s in range(y+1,y_length):
        # print("SOUTH")
        # print(treeMap[s][x])
        if treeMap[s][x] >= treeHeight:
            # print("ye")
            south = False
  
    

    #search left
    west = True
    for w in range(x-1,-1,-1):
        # print("WEST")
        # print(treeMap[y][w])
        if treeMap[y][w] >= treeHeight:
            # print("ye")
            west = False
    
    if north or south or east or west:
        count += 1

    # print("count is", count)
    
    return count

totalSeen = 0

for y in range(len(treeMap)):
    row = treeMap[y]
    if y != 0 and y != len(treeMap)-1:
        for x in range(len(row)):
            if x != 0 and x != len(treeMap[0])-1:
                totalSeen += directionalSearch(treeMap,x,y)
                

totalSeen += len(treeMap)*2 + len(treeMap[0])*2 -4

#part one
print(totalSeen)


def directionalSearchForViewing(treeMap,x,y):
    # print("for coordinates",x,y,treeMap[y][x])
    y_length = len(treeMap)
    x_length = len(treeMap[0])

    treeHeight = treeMap[y][x]

    count = 0
    #search up
    north = 0
    for n in range(y-1,-1,-1):
        # print("NORTH")
        # print(treeMap[n][x])
        if treeMap[n][x] >= treeHeight:
            area = y-n
            north = area 
            print("area is ",area)
            break
        
    if north == 0:
        north = y

    
    #search right
    east = 0
    for e in range(x+1,x_length):
        # print("EAST")
        # print(treeMap[y][e])
        if treeMap[y][e] >= treeHeight:
            area = e-x
            east = area
            print("area is ",area)
            break
    
    if east == 0:
        east = x_length - x - 1
    
    #search down
    south = 0
    for s in range(y+1,y_length):
        # print("SOUTH")
        # print(treeMap[s][x])
        if treeMap[s][x] >= treeHeight:
            area = s-y
            south = area
            print("area is ",area)
            break
  
    if south == 0:
        south = y_length - y - 1
    

    #search left
    west = 0
    for w in range(x-1,-1,-1):
        # print("WEST")
        # print(treeMap[y][w])
        if treeMap[y][w] >= treeHeight:
            area = x-w
            west = area
            # print("area is ",area)
            break
    
    if west == 0 :
        west = x
    
    return north*south*east*west

scores = []
for y in range(len(treeMap)):
    row = treeMap[y]
    if y != 0 and y != len(treeMap)-1:
        for x in range(len(row)):
            if x != 0 and x != len(treeMap[0])-1:
                scores.append(directionalSearchForViewing(treeMap,x,y))

print(scores)

max = 0
for score in scores:
    if score > max:
        max = score

#part two
print(max)