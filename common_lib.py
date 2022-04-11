from copy import deepcopy
import random

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

def dataframe(csv_path):
    f = open(csv_path, 'r')
    point_arr = []
    lines = f.readlines()
    for i in range(1, len(lines)):
        line = lines[i]
        line = line.replace('\n', '')
        point_arr.append(line.split(','))
    return point_arr

def unique_cats(dataframe):
    cats = []
    for point in dataframe:
        cat = point[len(point) - 1]
        if cat not in cats:
            cats.append(cat)
    return cats

def unique_random(low, high, taken):
    while True:
        n = random.randint(low, high)
        if n not in taken:
            return n