def bubbleSort(numbersToSort):
    while True:
        Flag = False
        for i in range(len(numbersToSort) - 1):
            if numbersToSort[i] > numbersToSort[i + 1]:
                numbersToSort[i], numbersToSort[i + 1] = numbersToSort[i + 1], numbersToSort[i]
                Flag = True
        if not Flag:
            return numbersToSort


def selectionSort(numbersToSort):
    for i in range(len(numbersToSort)):
        currentMin = i
        for j in range(i + 1, len(numbersToSort)):
            if numbersToSort[j] < numbersToSort[currentMin]:
                currentMin = j
        numbersToSort[currentMin], numbersToSort[i] = numbersToSort[i], numbersToSort[currentMin]
    return numbersToSort


numbers = [10, 55, 2, 6, 7, 22, 101]

print(numbers)

sortedNumbersBubble = bubbleSort(numbers)
sortedNumbersSelection = selectionSort(numbers)

print("Bubble sort: {}".format(sortedNumbersBubble))
print("Insertion sort: {}".format(sortedNumbersSelection))
