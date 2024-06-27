import math

array1 = [1,2,3,4,5]
array2 = []

def square_array(array):
    for i in range(len(array)):
        array2.append(math.pow(array[i],2))
    print(array2)

square_array(array1)