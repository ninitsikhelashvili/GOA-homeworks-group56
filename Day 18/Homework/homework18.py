num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 > num2:
    print(num1)
else:
    print(num2)

num3 = 8
if num3%2 == 0:
    print("even")
else:
    print("odd")

num4 = -9
if num4 > 0:
    print("positive")
else:
    print("negative")


num5 = float(input("Enter a number: "))
if num5%5 == 0:
    print("devisible by 5")
else:
    print("not devisible by 5")

num6 = int(input("enter a number: "))
if num6%2 == 0:
    print("even")
else:
    print("odd")

num7 = int(input("enter a number: "))
if num7%2 == 0:
    print("even")
else:
    print("odd")

num8 = int(input("enter a number: "))
if num8%2 == 0:
    print("even")
else:
    print("odd")

num9 = int(input("enter a number: "))
if num9%2 == 0:
    print("even")
else:
    print("odd")


password = "GOA best"
passw = input("enter password")
counter = 0
while passw != password:
    passw = input("enter password")
    counter += 1
print("total attempts", str(counter))

