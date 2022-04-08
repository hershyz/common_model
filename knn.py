import math

def classify(point, dataframe):

    dists = []
    for arr in dataframe:
        cat = arr[len(arr) - 1]
        dist = 0
        for i in range(len(arr) - 1):
            try:
                a = float(arr[i])
                b = float(point[i])
                dist += ((a - b) ** 2)
            except:
                continue
            dist = math.sqrt(dist)
            dists.append([dist, cat])
    
    k = round(0.1 * len(dataframe))
    dists.sort(key=lambda x: x[0])
    freqs = {}
    for i in range(0, k):
        cat = dists[i][1]
        if cat in freqs:
            freqs[cat] += 1
        if cat not in freqs:
            freqs[cat] = 1
    
    max = 0
    max_cat = ''
    for cat in freqs:
        if freqs[cat] > max:
            max = freqs[cat]
            max_cat = cat

    return max_cat

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
    classification = classify(point, point_arr)
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