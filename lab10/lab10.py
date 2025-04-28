"""
Irsan Sutanto
Friday Apr 25, loops
"""
print(f"\n----- example 1: for loops as a counter ----")
# print Hello from 0 to 4
for x in range(0,5):
    print(f"Hello = {x}")

print(f"\n---- example 2: for loop in a list----")
fruits = ['apples', 'oranges', 'grapes', 'mango', 'kiwis', 'pineaplle']
for eachfruitindex in range(0,len(fruits)):
    print(f"fruit with index {eachfruitindex} = {fruits[eachfruitindex]}")

# alternative way to loop through a list
print("\n---- alternative way to loop through a list ---")
for eachfruit in fruits:
    print(eachfruit)

print(f"\n---- example 3: for loop with different increment ----")
# for loop to print from 2 to 30, with an increment of 3
for num in range(2,30,3):
    print(num)

print(f"\n---- example 4: for loop with different decrement ----")
# for loop to print from 10 to 0, with decrement of 2
for num in range(10,0,-2):
    print(num)

print(f"\n---- example 5: for loop through a string ----")
username = "peterpan123"
for eachcharacter in username:
    print(eachcharacter)

print(f"\n---- example 6: nested conditional statement: count  ----")
# for loop to check how many numbers are in the list.
numbers = [5, -2, 0, 8, 9, -1]
negativecounter = 0
for eachnumber in numbers:
    if eachnumber < 0:
        negativecounter += 1    # the same as negativenumber = negativenumber + 1

#prompt result
print(f"There is/are {negativecounter} negative numbers")

print(f"\n---- example 7: nested conditional statement: operation  ----")
# for loop to add all ‘odd’ numbers
sumodd = 0
for eachnumber in numbers:
    if eachnumber %2 == 1:
        sumodd += eachnumber

#prompt result
print(f"The sum of all odd number is = {sumodd}")

print(f"\n---- example 8: break statement in a loop  ----")
# for loop to print from 0 to 10 (exclusive), and terminte the loop when it reaches to 5
for n in range (0,10):
    if n==5:
        print("counter reaches to 5")
        break
    else:
        print(n)

print(f"\n---- example 9: continue statement in a loop  ----")
# for loop to add numbers from 0 to 10 (exclusive), except number 5
sumall = 0
for n in range (10):
    if n==5:
        print("skipping 5")
        continue

sumall += n
print(n)
print(f"\tsum = {sumall}")

print(f"\n---- example 10: else statement in a for loop  ----")
for n in range (6):
    if(n==3):
        break
    print(n)
else:
    print("Loop completed")

print(f"\n---- example 11: while loop as a counter  ----")
# while loop to print from 0 to 5 (inclusive) ----> 0 1 2 3 4 5
n = 0
while n<6:
    print(n)
    n += 1

print(f"\n---- example 12: while loop as a checkpoint  ----")
# while loop to collect and add numbers between -5 and 5
# if the user enters a number that is not between -5 and 5, then while will terminate.

sumusernumber = 0
while(True):
    number = int(input("Enter a number between -5 and 5: "))
    if number<-5 or number>5:    # if not (5>=number>=-5)
        break
    sumusernumber += number

# prompt result
print(f"The total sum is = {sumusernumber}")

print(f"\n---- example 13: while loop as a counting operator  ----")
# while loop to count the even numbers in the list
numbers = [2, 0, -5, 1, 8, -6, 7, -3]
index = 0
len_numbers = len(numbers)
evencount = 0
while index<len_numbers:
    if numbers[index]%2 == 0 and not(numbers[index]==0):
        evencount += 1
    index += 1
else:
    print(f"There is/are {evencount} even numbers")


print(f"\n------ LAB EXERCISE -------")
colors = ['red', 'magenta', 'yellow', 'blue', 'purple', 'green', 'olive']
found = False

user_color = input("Enter your color :")
for color in colors:
    if color == user_color:
        found=True
        break
    if found:
        print(f"{user_color} is in the list")
    else:
        print(f"{user_color} is NOT in the list")




