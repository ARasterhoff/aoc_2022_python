file_path = 'day3.txt'
scorepart1 = 0
with open(file_path) as file:
    line_array = file.readlines()
    line_array = [item.rstrip() for item in line_array]
    # print(line_array)
    for line in line_array:
        line_len = len(line)//2
        part1 = line[0:line_len]
        part2 = line[line_len:]
        compare = ''
        for letter in part1:
            if letter in part2:
                compare = letter
        if compare.islower():
            scorepart1 += ord(compare) - 96
        else:
            scorepart1 += ord(compare) - 38
print(scorepart1)
# YES PART 1 BITCH