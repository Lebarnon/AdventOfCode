def printCave(visited):
    miny, maxy = min(visited.keys()), max(visited.keys())
    minx, maxx = float("inf"), float("-inf")
    for k, v in visited.items():
        minx = min(minx, min(v))
        maxx = max(maxx, max(v))
    caveMap = [["." for x in range(40)]for x in range(40)]
    for y in visited:
        for x in visited[y]:
            caveMap[y+5][x+5] = "#"
    for r in range(len(caveMap)):
        for c in range(len(caveMap[0])):
            print(caveMap[r][c], end=" ")
        print(r," ")
    print("")
        # print(r, end=" ")
    
    

def part1(input):
    # visited map --> y:set()
    visited = {}
    DIRECTION = [(0,1), (1,0), (0,-1), (-1,0)]

    for line in input.splitlines():
        lineArr = line.split(" ")
        sx = int(lineArr[2][2:-1])
        sy = int(lineArr[3][2:-1])
        bx = int(lineArr[-2][2:-1])
        by = int(lineArr[-1][2:])
        # bfs till from sensor to beacon
        queue = []
        queue.append((sx,sy))
        found = False
        if sy in visited:
            visited[sy].add(sx)
        else:
            visited[sy] = set([sx])
        while len(queue) > 0:
            itemsInQ = len(queue)
            for i in range(itemsInQ):
                curx, cury = queue.pop(0)
                for dx, dy in DIRECTION:
                    newx, newy = curx+dx, cury+dy
                    if(newy not in visited or newx not in visited[newy]):
                        if newy in visited:
                            visited[newy].add(newx) 
                        else:
                            visited[newy] = set([newx])
                        queue.append((newx, newy))
                printCave(visited)
            found = True if by in visited and bx in visited[by] else False   
            if found:
                break    
           
    printCave(visited)
    print(len(visited[10]))
            
input = open("day15/test.txt").read()
part1(input) 






