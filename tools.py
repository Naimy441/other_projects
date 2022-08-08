import copy

def count(array):
    count_dict = {}
    for item in array:
        count_dict.setdefault(item, 0)
        count_dict[item] += 1
    return count_dict

def mean(array):
    return sum(array) / len(array)

def median(array):
    sorted_array = copy.copy(array)
    sorted_array.sort()
    if len(array) % 2 == 0:
        med = (sorted_array[int(len(array)/2)] + sorted_array[int(len(array)/2)-1])/2
    else:
        med = sorted_array[int((len(array)-1)/2)]
    return med

def mode(array):
    array_count = count(array)
    max_number = max([v for v in array_count.values()])
    max_numbers = []
    for key in array_count:
        if array_count[key] == max_number:
            max_numbers.append(key)
    return max_numbers
