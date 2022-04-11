import time
import common_lib
import abs_distance_classifier
import sqrt_distance_classifier
import knn


csv_path = input('csv path: ')
start_time = time.perf_counter()
dataframe = common_lib.dataframe(csv_path)
cats = common_lib.unique_cats(dataframe)
model = common_lib.common_model(csv_path)


print('')
print('abs_distance_classifier:')
abs_totals = {}
abs_correct = {}

for cat in cats:
    abs_totals[cat] = 0
    abs_correct[cat] = 0

for point in dataframe:
    cat = point[len(point) - 1]
    classification = abs_distance_classifier.classify(point, model)
    abs_totals[cat] += 1
    if classification == cat:
        abs_correct[cat] += 1

for cat in abs_totals:
    print(cat + ': ' + str(abs_correct[cat] / abs_totals[cat]))

overall_abs_total = 0
overall_abs_correct = 0
for cat in abs_totals:
    overall_abs_total += abs_totals[cat]
    overall_abs_correct += abs_correct[cat]
print('overall accuracy: ' + str(overall_abs_correct / overall_abs_total))


print('')
print('sqrt_distance_classifier:')
sqrt_totals = {}
sqrt_correct = {}

for cat in cats:
    sqrt_totals[cat] = 0
    sqrt_correct[cat] = 0

for point in dataframe:
    cat = point[len(point) - 1]
    classification = sqrt_distance_classifier.classify(point, model)
    sqrt_totals[cat] += 1
    if classification == cat:
        sqrt_correct[cat] += 1

for cat in sqrt_totals:
    print(cat + ': ' + str(sqrt_correct[cat] / sqrt_totals[cat]))

overall_sqrt_total = 0
overall_sqrt_correct = 0
for cat in sqrt_totals:
    overall_sqrt_total += sqrt_totals[cat]
    overall_sqrt_correct += sqrt_correct[cat]
print('overall accuracy: ' + str(overall_sqrt_correct / overall_sqrt_total))


print('')
print('knn:')
sample_size = round(0.1 * len(dataframe))
knn_totals = {}
knn_correct = {}
sample_indices = []

for cat in cats:
    knn_totals[cat] = 0
    knn_correct[cat] = 0

for i in range(0, sample_size):
    index = common_lib.unique_random(0, len(dataframe) - 1, sample_indices)
    sample_indices.append(index)

for i in sample_indices:
    point = dataframe[i]
    cat = point[len(point) - 1]
    classification = knn.classify(point, dataframe)
    knn_totals[cat] += 1
    if classification == cat:
        knn_correct[cat] += 1

for cat in knn_totals:
    print(cat + ': ' + str(knn_correct[cat] / knn_totals[cat]))

overall_knn_total = 0
overall_knn_correct = 0
for cat in knn_totals:
    overall_knn_total += knn_totals[cat]
    overall_knn_correct += knn_correct[cat]
print('overall accuracy: ' + str(overall_knn_correct / overall_knn_total))


elapsed = time.perf_counter() - start_time
print('')
print('elapsed: ' + str(elapsed) + ' seconds')