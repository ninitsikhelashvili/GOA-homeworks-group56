list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
num = int(input("Enter number: "))
if num > 0 and num < 10:
    print(list[num])
elif num >= -10 and num <= -1:
    print(list[num])

list1 = [1, 2, 3, 5, True, False, 3.14, "a", "b"]
user_number = int(input("Enter number: "))
if user_number >= 0 and user_number < 10:
    print(list1[user_number])
elif user_number >= -10 and user_number <= -1:
    print(list[user_number])
else:
    print("wrong index:")

list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for x in list2:
    print(x*2)
    print(x/2)



