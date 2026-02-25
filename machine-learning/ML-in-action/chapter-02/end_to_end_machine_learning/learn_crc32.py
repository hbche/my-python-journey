# 学习CRC32循环冗余校验
import struct
from zlib import crc32

print(crc32(b"Hello, World~"))  # 396267445
print(crc32(b"Tom"))  # 1167209971
num_data = 127.92
print(crc32(struct.pack("d", num_data)))  # 1394855653
