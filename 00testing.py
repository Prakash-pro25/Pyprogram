import struct

n = struct.unpack('f', struct.pack('f', float(input())))[0]

print("%f" % n)
print("%.3f" % n)
print("%.2f" % n)
print("%.1f" % n)