import math

def classify(point, model):

    distances = {}
    for cat in model:
        cat_distance = 0
        cat_arr = model[cat]
        for i in range(0, len(cat_arr)):
            try:
                cat_distance += abs(cat_arr[i] - float(point[i]))
            except:
                continue
        distances[cat] = cat_distance
    
    min_distance = 1000000000000
    min_cat = ''
    for cat in distances:
        if distances[cat] < min_distance:
            min_distance = distances[cat]
            min_cat = cat

    return min_cat