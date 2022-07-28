
a = int(input('Input A side:'))
b = int(input('Input B side:'))
c = int(input('Input c side:'))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Not a right triangle")
else:
    print("Right triangle")