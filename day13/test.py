from collections import defaultdict as dd

def parse(instr):
    split_lines = instr.strip().split('\n')
    pairs = dd(list)
    i = 1
    for line in split_lines:
        if line:
            pairs[i].append(eval(line))
        else:
            i += 1
    return pairs

def check(left_list, right_list):
    for j in range(len(left_list)):
        try:
            if left_list[j] < right_list[j]:
                return True
            elif left_list[j] > right_list[j]:
                return False
        except IndexError:
            return False
        except TypeError:
            if type(left_list[j]) == list and type(right_list[j]) == list:
                left, right = left_list[j], right_list[j]
            elif type(left_list[j]) == int and type(right_list[j]) == list:
                left, right = [left_list[j]], right_list[j]
            elif type(left_list[j]) == list and type(right_list[j]) == int:
                left, right = left_list[j], [right_list[j]]

            return check(left, right)

    if len(left_list) < len(right_list):
        return True
    return False

def q13p1(instr):
    pairs = parse(instr)
    success = 0
    for i in range(1, len(pairs) + 1):
        left_list, right_list = pairs[i][0], pairs[i][1]
        # print(check(left_list, right_list))
        success += i * check(left_list, right_list)
    return success
 

# main
input = open("day13/input.txt").read()
print(q13p1(input))