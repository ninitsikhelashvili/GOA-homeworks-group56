goa = 50
while goa > 0:
    print("GOA BEST!!!")
    goa -= 1
num1 = 1
while num1 <= 10:
    print(num1)
    num1 += 1

num2 = 2
while num2 <= 20:
    print(num2)
    num2 +=2

num3 = 10
while num3 >= 1:
    print(num3)
    num3 -= 1
print("Blast Off !!!")

c_password = "password"
password = input("Enter your password: ")
counter = 0
while password != c_password:
    password = input("Enter your password: ")
    counter += 1

cpw = "pw"
pw = input("Enter your password: ")
counter = 0
while pw != cpw:
    pw = input("Enter correct password: ")
    counter += 1
usrn = "user123"
user = input("Enter user: ")
counter = 0
while user != usrn:
    user =input("Enter user: ")
    counter += 1


number = int(input("Enter a number: "))
factorial, starting_number = 1, 1
while starting_number <= number:
    factorial *= starting_number
    starting_number += 1
    print("starting number:", str(starting_number))
    print("factorial", str(factorial))
print("Factorial of" , str(number) , "is:" , str(factorial) )

    
