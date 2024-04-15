import decimal

a=1.01

print(type(a))

b = 1.01 * 100.23

print(f"b = {b}, type is {type(b)}")

c = decimal.Decimal(b).quantize(decimal.Decimal('0.0000'))
print(f"c = {c}, type is {type(c)}")
