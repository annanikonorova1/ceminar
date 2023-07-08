import numpy as np

arr2d = np.arange(6).reshape(2, 3)
print(arr2d)
print('\n')
print('After using T attribute: ')
arr2d_T = arr2d.T
print(arr2d_T)