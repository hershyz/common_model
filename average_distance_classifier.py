import math

def classify(dataframe, point):

    dists = {}
    freqs = {}
    for arr in dataframe:
        cat = arr[len(arr) - 1]
        if cat not in dists:
            dists[cat] = 0
            freqs[cat] = 0
    
    for arr in dataframe:
        cat = arr[len(arr) - 1]
        curr_dist = 0
        for i in range(len(arr) - 1):
            a = float(arr[i])
            b = float(point[i])
            curr_dist += ((a - b) ** 2)
        curr_dist = math.sqrt(curr_dist)
        dists[cat] += curr_dist
        freqs[cat] += 1
    
    for cat in dists:
        dists[cat] /= freqs[cat]
    
    min_dist = 100000000000
    min_cat = ''
    for cat in dists:
        if dists[cat] < min_dist:
            min_dist = dists[cat]
            min_cat = cat

    return min_cat


# read data
csv_path = 'data/diabetes_data.csv'
f = open(csv_path, 'r')
point_arr = []
lines = f.readlines()
for i in range(1, len(lines)):
    line = lines[i]
    line = line.replace('\n', '')
    point_arr.append(line.split(','))

# test
totals = {}
correct = {}
for point in point_arr:
    cat = point[len(point) - 1]
    if cat not in totals:
        totals[cat] = 0
        correct[cat] = 0

for point in point_arr:
    cat = point[len(point) - 1]
    classification = classify(point_arr, point)
    totals[cat] += 1
    if classification == cat:
        correct[cat] += 1

for cat in totals:
    print(cat + ': ' + str(correct[cat] / totals[cat]))

total = 0
total_correct = 0
for cat in totals:
    total += totals[cat]
    total_correct += correct[cat]

print('overall accuracy: ' + str(total_correct / total))