for i in range(0, 20, 2):
    print(i)

for i in range(1, 20, 2):
    print(i)

for i in range(10, 31):
    if i%2 == 0:
        print(str(i), "even")
    else:
        print(str(i), "odd")

for i in range(1, 20, 2):
    print(i)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
total = 0
if num1 > num2:
    for i in range(num1, num2):
        if i%2 == 0:
            print(i)
            total += i
    else:
        for i in range(num1, num2 + 1):
            if i%2 != 0:
                print(i)
                total += i

print(total)    



for i in range(10, 30):
    if i%2 == 0:
        print(str(i), "even")
    else:
        print(str(i), "odd")

