x = 221212
b = 0
while x > 999:
    v = x % 10
    b = b + v
    x = int(x) / 10
print(int(b))

f = 0
while x > 0:
    g = x % 10
    f = f + g
    x = x / 10
print(int(f))


if int(b) == int(f):
    print("Билет Счасливый")

else:
    print("Билет Несчасливый")