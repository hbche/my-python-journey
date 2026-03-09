import numpy as np

a = np.random.rand(2, 3)
b = np.arange(24, dtype=np.uint8).reshape(2, 3, 4)

np.savez("my_array.npz", my_a=a, my_b=b)

my_arrays = np.load("my_array.npz")
print(my_arrays.keys())
# KeysView(NpzFile 'my_array.npz' with keys: my_a, my_b)

print(my_arrays["my_a"])
# [[0.38080268 0.79826849 0.87967549]
#  [0.35814068 0.13948382 0.69677489]]