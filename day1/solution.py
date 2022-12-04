f = open('./input.txt')
data = f.read().splitlines()
f.close()

# part 1
results = []
curTotal = 0
for d in data:
  if d == "":
    results.append(curTotal)
    curTotal = 0
    continue
  curTotal += int(d)

print(max(results))

# part 2
sortedR = sorted(results)
top3 = sortedR[-3:]
print(sum(top3))