"""FIND THE FREQUENCY OF EACH ELEMENT IN THE LIST"""
"""SORT LIST BY DESC FREQUENCY"""


arr = [1, 1, 3, 5, 3, 2, 1, 54, 5, 6, 34, 2, 1, 2, 3, 4, 5, 566, 1, 4,4, 4]




new_list = [('Germany',120), ('France',110) , ('England',40) , ('Japan',184), ('China',20)]


def Freq_Cnter(arr):

    results = list()
    for item in set(arr):

        count = 0
        for comp in arr:
            if item == comp:
                count += 1

        results.append((item, count))

    return results

def BubbleSort_Tuples(new_list):

    new_ele = 1
    new_lis_len = len(new_list)

    for k in range(0, new_lis_len):

        for l in range(0, new_lis_len-k-1):
            side1 = new_list[l][new_ele]
            side2 = new_list[l + 1][new_ele]
            if ( side1 < side2 ):
                new_tem = new_list[l]
                new_list[l]= new_list[l + 1]
                new_list[l + 1]= new_tem

    return new_list


def TestBubbleSort(arra):
    arrlen = len(arra)

    for k in range(0, arrlen):

        for i in range(0, arrlen - k - 1):

            if arra[i] > arra[i + 1]:
                item = arra[i]
                arra[i] = arra[i + 1]
                arra[i + 1] = item

    return arra


if __name__ == "__main__":
    test = Freq_Cnter(arr)
    test = BubbleSort_Tuples(test)
    print(test)

    test2 = TestBubbleSort([1,4,5,6,2,3,4,5])

    print(test2)







