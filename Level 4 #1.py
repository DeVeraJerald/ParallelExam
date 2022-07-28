import random

num = 100
odd = []
even = []
mylist = []

for i in range(0,100):
    x = random.randint(100, 999)
    mylist.append(x)

    if (x % 2) == 0:
        even.append(x)
    else:
        odd.append(x)

Divisible_list = []
def divisible(l =[]):

    for i in range(0, len(l)):
        if l[i] % 9 == 0:
            Divisible_list.append(l[i])

    return 1

prime_list = []
def prime(num):

    for i in range(len(num)):
        x = num[i]

        if x > 1:
            for e in range(2, x):
                if (x % e) == 0:
                    break
            else:
                prime_list.append(x)

def contains(lst):
    x = lst
    n = 9
    output = list(filter(lambda ele: str(n) in str(ele),x))
    print(str(output))



print('A. All elements in the list: ')
print(mylist)
print('B. All numbers grouped by odd and even numbers ')
print('Odd Numbers :')
print(odd)
print('Even Numbers :')
print(even)
print('C. All numbers divisible by 9. ')
divisible(mylist) == 1
print(Divisible_list)
print('D. All prime numbers')
prime(mylist)
print(prime_list)
print('E. All numbers that contains the digit 9')
contains(mylist)