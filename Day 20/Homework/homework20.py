list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in list1:
    print(x)

list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
if num1 > num2 : 
    print(list2[num2:num1])
elif num2 > num1 :
    print(list1[num1:num2])
else:
    print("[]")

list3 = [1, 3, 5, 7, 9]
print(list3[0])
print(list3[2])
print(list3[4])

list4 = ["cat", "dog", "parrot"]
print(list4[::-1])

list5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
print(list5[::2])

list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
list6[3] = 100
print(list6)
