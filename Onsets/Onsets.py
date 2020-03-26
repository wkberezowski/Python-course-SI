from sorting_methods import bubbleSort, selectionSort

list1 = ([43, 123, 0, 32, 1, 4, 451235], 25)
list2 = ([5, 30, 63, 1, 3, 0, 105, 21], 1)


def onsetsForBubble(list, function):
    input_ = list[0]
    threshold = list[1]
    output = []
    counter = 0

    for i in range(len(list[0])):
        if input_[i] > threshold:
            output.append(i)
            counter += 1
            if counter == 3:
                break
    try:
        output = function([input_[output[0]], input_[output[1]], input_[output[2]]])
    except:
        print("There are no 3 values greater than {}".format(threshold))

    finalList = []
    for i in range(3):
        finalList.append(input_.index(output[i]))

    return finalList


print(onsetsForBubble(list2, bubbleSort))
print(onsetsForBubble(list2, selectionSort))


