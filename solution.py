reports = [[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]]

def is_safe(report):
    diffs = [b - a for a, b in zip(report, report[1:])]

    all_increasing = all(d > 0 for d in diffs) #ascending
    all_decreasing = all(d < 0 for d in diffs) #descending
    
    valid_distances = all(1 <= abs(d) <= 3 for d in diffs)
    
    return (all_increasing or all_decreasing) and valid_distances


for individual_reports in reports:
    if is_safe(individual_reports):    
        print('safe')
    else:
        print('unsafe')