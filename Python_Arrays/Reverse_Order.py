"""Write a program to print the array in reverse order."""


def Reverse_Array(array):
    start = 1

    while start < len(array):
        print(array[-1 * start])

        start += 1


array = range(0,100)


Reverse_Array(array)