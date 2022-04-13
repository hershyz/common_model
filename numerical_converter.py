import common_lib

csv_path = input('csv path for conversion: ')
dataframe = common_lib.dataframe(csv_path)

map = {}
n = 0
for point in dataframe:
    for i in range(0, len(point) - 1):
        feature = point[i]
        if feature not in map:
            map[feature] = n
            n += 1

f = open(csv_path, 'r')
raw = f.readlines()
feature_labels = raw[0].replace('\n', '')

converted_dataframe = []
for point in dataframe:
    new_point = []
    for i in range(0, len(point) - 1):
        feature = point[i]
        if feature in map:
            new_point.append(map[feature])
        else:
            new_point.append(feature)
    new_point.append(point[len(point) - 1])
    converted_dataframe.append(new_point)

new_f = open(csv_path, 'w')
new_f.write(feature_labels + '\n')
for point in converted_dataframe:
    point_string = str(point)
    point_string = point_string.replace('[', '')
    point_string = point_string.replace(']', '')
    new_f.write(point_string + '\n')

print('converted dataset: ' + str(map))