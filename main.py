from cmath import sqrt
from copy import deepcopy
import abs_distance_classifier
import sqrt_distance_classifier

def common_model(path):
    
    # read lines and find unique categories
    f = open(path, 'r')
    lines = f.readlines()
    cats = []
    for i in range(1, len(lines)):
        split = lines[i].split(',')
        cat = split[len(split) - 1].replace('\n', '')
        if cat not in cats:
            cats.append(cat)
    
    # populate init quantity totals
    model = {}
    n_features = len(lines[0].split(',')) - 1
    init_arr = []
    for i in range(0, n_features):
        init_arr.append(0)
    for cat in cats:
        model[cat] = init_arr

    # populate init category frequencies
    freq = {}
    for cat in cats:
        freq[cat] = 0

    # add feature totals
    for i in range(1, len(lines)):
        data = lines[i].replace('\n', '').split(',')
        cat = data[len(data) - 1]
        arr = model[cat]
        for j in range(0, len(arr)):
            try:
                arr[j] += float(data[j])
            except:
                continue
        model[cat] = deepcopy(arr)
        freq[cat] = freq[cat] + 1
    
    # calculate averages
    for cat in cats:
        arr = model[cat]
        n = freq[cat]
        for i in range(0, len(arr)):
            arr[i] /= n
        model[cat] = deepcopy(arr)

    return model








# read data
csv_path = 'data/cervical_cancer.csv'
f = open(csv_path, 'r')
point_arr = []
lines = f.readlines()
for i in range(1, len(lines)):
    line = lines[i]
    line = line.replace('\n', '')
    point_arr.append(line.split(','))


# testing
model = common_model(csv_path)
totals = {}
correct = {}
for cat in model:
    totals[cat] = 0
    correct[cat] = 0

for point in point_arr:
    prediction = sqrt_distance_classifier.classify(point, model)  # classifier type
    cat = point[len(point) - 1]
    totals[cat] += 1
    if prediction == cat:
        correct[cat] += 1


# display categorical accuracy
for cat in totals:
    print(cat + ': ' + str(float(correct[cat] / totals[cat])))


# display total accuracy
total = 0
total_correct = 0
for cat in totals:
    total += totals[cat]
    total_correct += correct[cat]
print('overall accuracy: ' + str(float(total_correct / total)))