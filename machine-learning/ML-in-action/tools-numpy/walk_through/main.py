import numpy as np

f = np.array([[1, 2], [1000, 2000]], dtype=np.int32)
if hasattr(f.data, "tobytes"):
    data_types = f.data.tobytes()  # python 3
else:
    data_types = memoryview(f.data).tobytes()  # python 2

print(data_types)
# b'\x01\x00\x00\x00\x02\x00\x00\x00\xe8\x03\x00\x00\xd0\x07\x00\x00'
