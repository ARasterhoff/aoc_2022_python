file_path = 'day1.txt'
totalarray = []
tempsum = 0
with open(file_path) as file:
    line_array = file.readlines()
    line_array.append('')
    # ;-) niet vertellen
    line_array = [item.rstrip() for item in line_array]
    # print(line_array)
    for line in line_array:
        if line != '':
            tempsum = tempsum + int(line)
            # print(tempsum)
        else:
            totalarray.append(tempsum)
            tempsum = 0
max = 0
for value in totalarray:
    if value > max:
        max = value
print(max)
# print(totalarray)
# dit was deel 1
totalarray.sort(reverse=True)
print(sum(totalarray[:3]))
# deel 2 kwam goed uit denk
# https://datagy.io/python-read-text-file/