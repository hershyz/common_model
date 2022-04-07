import math

def classify(point, model):

    dists = {}

    for cat in model:
        arr = model[cat]
        cat_dist = 0
        for i in range(len(arr)):
            try:
                x = float(point[i])
                cat_dist += (arr[i] - x) ** 2
            except:
                continue
        dists[cat] = math.sqrt(cat_dist)
    
    min = 10000000000
    min_cat = ''
    for cat in dists:
        if dists[cat] < min:
            min_cat = cat
            min = dists[cat]
    
    return min_cat