import numpy as np

arr_int = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr_int)

arr_bool = np.array([[True, True, True],
                    [True, True, True],
                    [True, True, True]])

print(arr_bool)

print(arr_int[arr_int % 2 != 0])

arr_int[arr_int % 2 != 0] = -1

print(arr_int)
