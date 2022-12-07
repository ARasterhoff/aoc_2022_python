file_path = 'day3.txt'
firsthalf = []
lasthalf = []
with open(file_path) as file:
    line_array = file.readlines()
    line_array = [item.rstrip() for item in line_array]
    print(line_array)