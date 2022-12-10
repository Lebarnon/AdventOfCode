def readInput():
    input = open('input.txt').read().splitlines()
    rows = len(input)
    forest = [[]for x in range(rows)]
    for i,val in enumerate(input):
        for c in val:
            forest[i].append(int(c))
    return forest

def getMinHeightForEachCell(forest):
    rows = len(forest)
    cols = len(forest[0])
    minHeightEachCell = [[[float("-inf"), float("-inf")] for x in range(cols)] for x in range(rows)] 
    # [HorizontalMax, VerticalMax]

    # process horizontally first
    for r in range(rows):
        maxIndex = forest[r].index(max(forest[r]))
        curSubMax = forest[r][0]
        # tranverse from left to before maxIndex and store the max so far in largest for each cell
        for c in range(1,maxIndex): # edges largest will be left as -inf
            minHeightEachCell[r][c][0] = curSubMax
            curSubMax = max(curSubMax, forest[r][c])
        # trancerse from right to maxIndex excluding max index
        curSubMax = forest[r][cols-1]
        for c in range(cols-2, maxIndex, -1):
            minHeightEachCell[r][c][0] = curSubMax
            curSubMax = max(curSubMax, forest[r][c])
        # the first max can always be seen so leave its value in largestforeachcell as (-inf, -inf)

    # process vertically 
    for c in range(cols):
        # consolidate col vals in a array
        colVals = []
        for r in range(0, rows):
            colVals.append(forest[r][c])
        
        # undergo same logic as vertical processing
        maxIndex = colVals.index(max(colVals))
        curSubMax = forest[0][c]
        # tranverse from top to maxIndex and store the max so far in minHeight for each cell
        for r in range(1,maxIndex): # edges largest will be left as -inf
            minHeightEachCell[r][c][1] = curSubMax
            curSubMax = max(curSubMax, forest[r][c])
        # trancerse from bottom to maxIndex
        curSubMax = forest[rows-1][c]
        for r in range(rows-2, maxIndex, -1):
            minHeightEachCell[r][c][1] = curSubMax
            curSubMax = max(curSubMax, forest[r][c])
    return minHeightEachCell
    
def part1(forest):
    rows = len(forest)
    cols = len(forest[0])
    minHeightEachCell = getMinHeightForEachCell(forest)
    totalVisible = 0

    for r in range(rows):
        for c in range(cols):
            curHeight = forest[r][c]
            minHeightArr = minHeightEachCell[r][c]
            totalVisible += 1 if curHeight > minHeightArr[0] or curHeight > minHeightArr[1] else 0
    print(totalVisible)

def getViewDistMatrix(forest):
    rows = len(forest)
    cols = len(forest[0])
    viewDistMatrix = [[[0, 0, 0, 0] for x in range(cols)] for x in range(rows)] 
    # [top,right,down,left]s

    # process horizontally first
    for r in range(rows):
        # find viewDist from left
        for c in range(1,cols-1): # edges largest will be left as 0
            viewDistMatrix[r][c][3] = c
            for i in range(c-1, 0,-1):
                if(forest[r][c] <= forest[r][i]):
                    viewDistMatrix[r][c][3] = c-i
                    break

        # transverse from right
        for c in range(cols-2, 0, -1):
            viewDistMatrix[r][c][1] = cols-1 - c
            for i in range(c+1, cols-1):
                if(forest[r][c] <= forest[r][i]):
                    viewDistMatrix[r][c][1] = i-c
                    break

    # process horizontal
    for c in range(cols):
        colVals = []
        for r in range(rows):
            colVals.append(forest[r][c])

        # tranverse from top 
        for r in range(1,rows-1): # edges largest will be left as 0
            viewDistMatrix[r][c][0] = r
            for i in range(r-1, 0, -1):
                if(forest[r][c] <= forest[i][c]):
                    viewDistMatrix[r][c][0] = r-i
                    break

        # transverse from bottom
        for r in range(rows-2, 0, -1):
            viewDistMatrix[r][c][2] = rows-1 - r
            for i in range(r+1, rows-1):
                if(forest[r][c] <= forest[i][c]):
                    viewDistMatrix[r][c][2] = i-r
                    break
    for v in viewDistMatrix:
        print(v)

    return viewDistMatrix

def part2(forest):
    rows = len(forest)
    cols = len(forest[0])
    viewDistMatrix = getViewDistMatrix(forest)
    maxDist = 0
    for r in range(rows):
        for c in range(cols):
            curViewDist = 1
            for dist in viewDistMatrix[r][c]:
                curViewDist *= dist
            maxDist = max(maxDist, curViewDist)
    print("Max Distance" ,maxDist)

forest = readInput()

part2(forest)