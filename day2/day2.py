file_path = 'day2.txt'
counter = 0
counter2 = 0
cases = {
    'A X': '3',
    'A Y': '6',
    'A Z': '0',
    'B X': '0',
    'B Y': '3',
    'B Z': '6',
    'C X': '6',
    'C Y': '0',
    'C Z': '3',
    'X': '1',
    'Y': '2',
    'Z': '3'
}
cases2 = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W'
}
with open(file_path) as file:
    line_array = file.readlines()
    line_array = [item.rstrip() for item in line_array]
    # print(line_array)
    for array in line_array:
        counter = counter + int(cases[array]) + int(cases[array[-1]])
        outcome = cases2[array[-1]]
# print(counter)
# print(outcome)
# nou dat was deel 1 maar ik moet dat hele kut ding omgooien voor deel 2 ofzo dus die werk ik er gewoon wel in ipv eronder hahaHAAA
# doe deel 2 later wel
# tijd om deel 2 te forceren met wacky code
part2 = 0
with open(file_path) as file:
    line_array = file.readlines()
    line_array = [item.rstrip() for item in line_array]
    # print(line_array)
    for array in line_array:
        splitarray = array.split(' ')
        p1 = splitarray[0]
        p2 = splitarray[1]
        if p1 == 'A' and p2 == 'X':
            part2 += 3
        if p1 == 'A' and p2 == 'Y':
            part2 += 4
        if p1 == 'A' and p2 == 'Z':
            part2 += 8
        if p1 == 'B' and p2 == 'X':
            part2 += 1
        if p1 == 'B' and p2 == 'Y':
            part2 += 5
        if p1 == 'B' and p2 == 'Z':
            part2 += 9
        if p1 == 'C' and p2 == 'X':
            part2 += 2
        if p1 == 'C' and p2 == 'Y':
            part2 += 6
        if p1 == 'C' and p2 == 'Z':
            part2 += 7
print(part2)