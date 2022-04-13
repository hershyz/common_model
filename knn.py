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
    
    # k = round(0.1 * len(dataframe))
    k = 5
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