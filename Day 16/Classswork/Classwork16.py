num = int(input("Enter a number: "))
sum = 0
for i in range(num):
    sum = sum +1
    print(sum)

correct_password = "password"
password = input("Enter your password: ")
counter = 0
while password != correct_password:
    password = input("Enter your password: ")
    counter += 1
print("Access granted!")
print("your guess count: ",  str(counter))




