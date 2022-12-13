import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv
}

class Monkey:
    def __init__(self, items, operator, operand, testVal, trueMonkey, falseMonkey):
        self.items = items #queue
        self.operator = operator 
        self.operand = operand # -1 means operand is the item's value
        self.testVal = testVal
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.totalInspected = 0 
        self.reducer = 1

    def addItems(self, item):
        self.items.append(item)

    def setReducer(self, reducer):
        self.reducer = reducer
    
    def calcNewWorry(self, item):
        operand = self.operand
        if(operand == -1):
            operand = item
        return ops[self.operator](item, operand) % self.reducer # return reduced value
         
    def playTurn(self, monkeys):
        while(len(self.items) > 0):
            item = self.items.pop(0)
            newWorry = self.calcNewWorry(item)
            self.totalInspected += 1
            if(newWorry%self.testVal == 0):
                monkeys[self.trueMonkey].addItems(newWorry)
            else:
                monkeys[self.falseMonkey].addItems(newWorry)
    
def initialiseMonkeys(input):
    monkeys = {}
    monkeyInputs = input.split("\n\n")
    reducer = 1
    # initialise all monkeys and items
    for monkeyInput in monkeyInputs:
        monkeyInfo = monkeyInput.splitlines()
        i=0
        id = int(monkeyInfo[i].split(" ")[1][:-1])
        i+=1
        items = [int(x) for x in monkeyInfo[i].split(":")[1].strip().split(", ")]
        i+=1
        operationInfo = monkeyInfo[i].split(" ")
        operator = operationInfo[-2]
        operand = operationInfo[-1]
        if(operand == "old"):
            operand = -1
        operand = int(operand)
        i+=1
        testInfo = monkeyInfo[i].split(" ")
        testVal = int(testInfo[-1])
        reducer *= testVal
        i+=1
        trueMonkey = int(monkeyInfo[i].split(" ")[-1])
        i+=1
        falseMonkey = int(monkeyInfo[i].split(" ")[-1])
        monkeys[id] = Monkey(items, operator, operand, testVal, trueMonkey, falseMonkey)
    # set reducer for all items
    for k,monkey in monkeys.items():
        monkey.setReducer(reducer)
    return monkeys

def part2(monkeys):
    def display(monkeys):
        inspectedVals= []
        for k,monkey in monkeys.items():
            print("Monkey", k, "inspected items", monkey.totalInspected, "times")
            inspectedVals.append(monkey.totalInspected)
        sortedInspectedVals = sorted(inspectedVals)
        print("MonkeyBusiness: ", sortedInspectedVals[-1] * sortedInspectedVals[-2])
    
    roundsToPrint = {1,20,1000,10000}
    for i in range(10000):
        for k,monkey in monkeys.items():
            monkey.playTurn(monkeys)
        if(i+1 in roundsToPrint):
            print("== After round", i+1, "==")
            display(monkeys)

# main
input = open('day11/input.txt').read()
monkeys = initialiseMonkeys(input)
part2(monkeys)
