"""How would you find all pairs in an array of integers whose sum equals a number given? """


def Find_Pair_Sum(array, designate):
    start = 0
    pairs = list()

    while start < len(array):
        compare = array[start]
        for item in array:
            if (item + compare) == designate:
                pairs.append((compare, item))

        start += 1

    return pairs

array = range(0,100)
results = Find_Pair_Sum(array, 34)

print(results)