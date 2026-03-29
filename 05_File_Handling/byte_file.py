data = bytearray(100)

for i in range(100):
    data[i] = 100 - i

with open('data/output/byte_file.bin', 'wb') as f:
    f.write(data)

data_out = bytearray(10)

with open('data/output/byte_file.bin', 'rb') as f:
    for i in range(10):
        f.readinto(data_out)
        print(hex(int.from_bytes(data_out, byteorder='big')))