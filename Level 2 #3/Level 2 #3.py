

x = int(input(" input number between 0 to 35: "))

if x <= 9:
    print(x)
else:
    for i in range(ord('A'), ord('Z') + 1):
        print(chr(i),'For',i-55)
