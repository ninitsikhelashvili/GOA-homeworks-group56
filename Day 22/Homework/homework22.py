smth = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
for x in smth:
    print(x)
smth2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
if num1 > num2:
    print(smth2[num2:num1])
elif num2 > num1:
    print(smth2[num1:num2])
else:
    print("[]")

list1 = [ 1, 2, 3, 4, 5, ]
print(list1[0])
print(list1[2])
print(list1[4])

list2 = ["a", "b", "c"]
print(list2[::-1])

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list3[::2])

list3[3] = 100
print(list3)