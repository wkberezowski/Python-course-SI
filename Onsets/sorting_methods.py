def bubbleSort(numbersToSort):
    while True:
        Flag = False
        for i in range(len(numbersToSort) - 1):
            if numbersToSort[i] < numbersToSort[i + 1]:
                numbersToSort[i], numbersToSort[i + 1] = numbersToSort[i + 1], numbersToSort[i]
                Flag = True
        if not Flag:
            return numbersToSort


def selectionSort(numbersToSort):
    for i in range(len(numbersToSort)):
        currentMax = i
        for j in range(i + 1, len(numbersToSort)):
            if numbersToSort[j] > numbersToSort[currentMax]:
                currentMax = j
        numbersToSort[currentMax], numbersToSort[i] = numbersToSort[i], numbersToSort[currentMax]
    return numbersToSort
