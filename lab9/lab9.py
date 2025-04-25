"""
Irsan Sutanto
April 24, conditional statement
"""
print(f"\n----- example 1 and 2: if statement -----")
age = 20
agecode = 123

if age >= 21:
    print("You are an adult")
    agecode = 200
else:
    print("You are under 21!!")
    agecode = 100

print(f"After the 'if' statement, agecode = {agecode}")

print(f"\n----- example 3: multi statement -----")
age = 50
if 0<= 21:
    print("You are an adult!!")
elif 65<= age <=130:
    print("You are senior citizen")
else:
    print("unable to read age!!")

print(f"\n----- example 4: and operator -----")
temperature = 90 
humidity = 60 

if 70 <= temperature <= 90 and humidity < 80:
    print("The weather is pleasant")
else:
    print("THe wather is not ideal")

print(f"\n----- example 5 : or operator -----")
day = "Monday"
is_holiday = True

if day=="Saturday" or day=="Sunday" or is_holiday:
    print("You can relax today")
else:
    print("It is a workday")

print(f"\n----- example 6 : nested conditional statement -----")
number = int(input("Enter a number: "))
if (number>=0):
    if number==0:
        print("The number is zero")
    else:
        print(f"{number} is positive")
else:
    print(f"{number} is negative")

print(f"\n----- example 7 : username validation -----")
# username validation, username must have 3+ characters
username = input("Enter username: ")
username = username.strip()
len_username = len(username)
if len_username >= 3:
    print(f"{username} has 3+ character")
    index_whitespace = username.find(" ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print(f"Username CANNOT have whitespace")
else:
    print(f"{username} is INVALID. Username must have 3+ character")

print(f"\n----- example 8 : match-case statement -----")
response_code = 400

match response_code:
    case 400:
        print(f"Code = {response_code}. Server CANNOT understand")
    case 401 | 403:
        print(f"Code ={response_code}. Server refused to send back")
    case 404:
        print(f"Code = {response_code}. Server cant find")
    case _:
        print(f"INVALID CODE")

print(f"\n------ LAB EXERCISE -------")
"""calculate the average of 2 grades and returns a GPA"""
grade1 = input("Enter your grade1: ")
grade1 = float(grade1)
grade2 = input("Enter your grade2: ")  
grade2 = float(grade2)

average = (grade1 + grade2)/2

if 90 <= average <= 100:
            GPA = "A"
elif 70 <= average <= 89.99:
            GPA = "B"
elif 60 <= average <= 69.99:
            GPA = "C"
elif 0 <= average <= 59.99:
            GPA = "YOU FAILED!!"
else:
            GPA = "UNDEFINED!"

print(f"For the average of {average}, your GPA is {GPA}")
