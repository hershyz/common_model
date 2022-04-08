# read data
csv_path = 'data/diabetes_data.csv'
f = open(csv_path, 'r')
point_arr = []
lines = f.readlines()
for i in range(1, len(lines)):
    line = lines[i]
    line = line.replace('\n', '')
    point_arr.append(line.split(','))