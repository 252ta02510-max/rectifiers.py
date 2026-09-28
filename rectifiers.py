import math

v = float(input("Enter AC voltage: "))

print("Half Wave Rectifier =", v / math.pi)
print("Full Wave Rectifier =", 2 * v / math.pi)
