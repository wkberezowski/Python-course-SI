import time
from Onsets import onsetsForFunction
from sorting_methods import bubbleSort, selectionSort

list1 = ([43, 123, 0, 32, 1, 4, 451235], 25)
list2 = ([5, 30, 63, 1, 3, 0, 105, 21], 1)


def Timer(onSets, list_, function):
    start = time.perf_counter()
    onSets(list_, function)
    end = time.perf_counter()
    return end - start


print("Time for Bubble Sort function for list1: {}".format(Timer(onsetsForFunction, list1, bubbleSort)))
print("Time for Bubble Sort function for list2: {}".format(Timer(onsetsForFunction, list2, bubbleSort)))
print(40*"=")
print("Time for Selection Sort function for list1: {}".format(Timer(onsetsForFunction, list1, selectionSort)))
print("Time for Selection Sort function for list2: {}".format(Timer(onsetsForFunction, list2, selectionSort)))
