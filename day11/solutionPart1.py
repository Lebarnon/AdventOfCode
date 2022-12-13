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
        self.operand = int(operand) # -1 means operand is the item's value
        self.testVal = int(testVal)
        self.trueMonkey = int(trueMonkey)
        self.falseMonkey = int(falseMonkey)
        self.totalInspected = 0 

    def addItems(self, item):
        self.items.append(item)
    
    def calcNewWorry(self, item):
        operand = self.operand
        if(operand == -1):
            operand = item
        return ops[self.operator](item, operand)
         
    def playTurn(self, monkeys):
        while(len(self.items) > 0):
            item = self.items.pop(0)
            newWorry = self.calcNewWorry(item)
            self.totalInspected += 1
            boredWorry = newWorry//3
            if(boredWorry%self.testVal == 0):
                monkeys[self.trueMonkey].addItems(boredWorry)
            else:
                monkeys[self.falseMonkey].addItems(boredWorry)
    
def initialiseMonkeys(input):
    monkeys = {}
    monkeyInputs = input.split("\n\n")
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
        testVal = testInfo[-1]
        i+=1
        trueMonkey = monkeyInfo[i].split(" ")[-1]
        i+=1
        falseMonkey = monkeyInfo[i].split(" ")[-1]
        monkeys[id] = Monkey(items, operator, operand, testVal, trueMonkey, falseMonkey)
    return monkeys

def part1(monkeys):
    inspectedVals= []
    for i in range(20):
        for k,monkey in monkeys.items():
            monkey.playTurn(monkeys)
    for k,monkey in monkeys.items():
        print("Monkey", k, "inspected items", monkey.totalInspected, "times")
        inspectedVals.append(monkey.totalInspected)
    sortedInspectedVals = sorted(inspectedVals)
    print("MonkeyBusiness: ", sortedInspectedVals[-1] * sortedInspectedVals[-2])


# main
input = open('day11/input.txt').read()
monkeys = initialiseMonkeys(input)
part1(monkeys)


    