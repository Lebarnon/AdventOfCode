class DirInfo:
    def __init__(self, x):
        self.size = x
        self.children = set()

def createDirTree(input):
    def isCommand(input):
        return input.split(" ")[0] == "$"

    directories = {} #name:dirInfo

    curDir= ""
    for (i, line) in enumerate(input):
        if(isCommand(line)):
            command = line.split(" ")
            if(command[1] == "cd"):
                if(command[2] == ".."):
                    curDir = curDir[:-1] # get rid of last slash
                    lastSlashIndex = curDir.rfind("/")
                    curDir = curDir[:lastSlashIndex+1] # go back one dir level
                elif(command[2] == "/"):
                    curDir = "/"
                else:
                    curDir += command[2] + "/"
                continue
            if(command[1] == "ls"):
                if(curDir not in directories):
                    directories[curDir] = DirInfo(0)
                while i+1 != len(input) and not isCommand(input[i+1]):
                    i = i+1
                    fileInfo = input[i].split(" ")
                    if(fileInfo[0].isnumeric()):
                        directories.get(curDir).size += int(fileInfo[0])
                    else:
                        directories.get(curDir).children.add(curDir + fileInfo[1] + "/")
    return directories

def calcSize(directories, rootKey):
    curDirInfo = directories.get(rootKey)
    if len(curDirInfo.children) == 0:
        return curDirInfo.size
    for childKey in curDirInfo.children:
        curDirInfo.size += calcSize(directories,childKey)
    return curDirInfo.size

def findTotal(directories, rootKey):
    curDirInfo = directories.get(rootKey)
    total = 0
    if(curDirInfo.size <= 100000):
        total += curDirInfo.size
    for childKey in curDirInfo.children:
        total += findTotal(directories, childKey)
    return total

def findSmallestSizeToDel(directories, spaceToFree, rootKey):
    curDirInfo = directories.get(rootKey)

    if(curDirInfo.size < spaceToFree):
        return float("inf")

    smallestVal = curDirInfo.size
    for childKey in curDirInfo.children:
        smallestVal = min(smallestVal,findSmallestSizeToDel(directories, spaceToFree, childKey))
    return smallestVal

def part1(input):
    directories = createDirTree(input)
    calcSize(directories, "/")
    totalSize = findTotal(directories, "/")
    print(totalSize)
    

def part2(input):
    directories = createDirTree(input)
    calcSize(directories, "/")
    spaceToFree = 30000000 - (70000000 - directories.get("/").size)
    smallestVal = findSmallestSizeToDel(directories, spaceToFree, "/")
    print(smallestVal)

# main
input = open('input.txt').read().splitlines()
part1(input)
part2(input)







