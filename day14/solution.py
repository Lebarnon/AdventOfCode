def getRocksCoord(input):
    rocksCoord = set()
    for line in input.splitlines():
        coordinates = line.split(" -> ")
        for i in range(len(coordinates)-1):
            startx, starty = coordinates[i].split(",")
            startx, starty = int(startx), int(starty)
            endx, endy = coordinates[i+1].split(",")
            endx, endy = int(endx), int(endy)
            if(startx != endx): #vertical line
                if(startx<endx):
                    for x in range(startx, endx+1):
                        rocksCoord.add((x, starty))
                else:
                    for x in range(endx, startx+1):
                        rocksCoord.add((x, starty))
            else:
                if(starty<endy):
                    for y in range(starty, endy+1):
                        rocksCoord.add((startx, y))
                else:
                    for y in range(endy, starty+1):
                        rocksCoord.add((startx, y))
    return rocksCoord

def getMaxY(rocksCoord):
    maxY = 0
    for coord in rocksCoord:
        maxY = max(maxY, coord[1])
    return maxY

DIR_TO_FALL = [(0,1), (-1,1), (1,1)]
def dropSand(curCoord, maxY, rocksCoord):
        if(curCoord[1] > maxY): #dropping into void
            return False 
            
        for dir in DIR_TO_FALL:
            newx, newy = dir[0]+curCoord[0], dir[1]+curCoord[1]
            if (newx, newy) not in rocksCoord:
                nextPosPossible = dropSand((newx,newy), maxY, rocksCoord)
                if not nextPosPossible and newy == maxY:
                    rocksCoord.add(curCoord)
                return nextPosPossible
        
        rocksCoord.add(curCoord)
        return True
                
def part1(input):
    rocksCoord = getRocksCoord(input)
    maxY = getMaxY(rocksCoord)
    i=0
    while True:
        if(dropSand((500,0), maxY, rocksCoord)):
            i+=1
        else:
            break
    print(i)

def part2(input):
    rocksCoord = getRocksCoord(input)
    floorY = getMaxY(rocksCoord) + 2
    i=0
    while (500,0) not in rocksCoord:
        dropSand((500,0), floorY, rocksCoord)
        i+=1
    print(i)


input = open("day14/input.txt").read()
part1(input)
part2(input)


