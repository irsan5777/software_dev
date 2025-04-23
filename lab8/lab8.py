"""
Irsan Sutanto
April 20, Introduction to Python
"""

#Single comment. This line will not RUN
print('\n------ Example 1: string characters -----')
print("\tGood morning! \nThis is my first Python Code!")
print("\n---------Good morning! \nThis is my first \"Python\" code!")

print('\n-------- Example 2: data type -----')
print(f"Data type of 3.56 = {type(3.56)}")
print(f"Data type of -25 = {type(-25)}")
print(f"Data type of 'Hello WOrld!' = {type('Hello WOrld!')}")
print(f"Data type of character '$' = {type('$')}")
print(f"Data type of False = {type(False)}")

print('\n------ Example 3: Variables -------')
# declare variables
number1 = 25.5
number2 = -12
username = "Peter Pan"
add_numbers = number1 + number2
is_raining = True
#prompt results
print(f"{username}, the sum of {number1} and {number2} is {add_numbers}")
print(f"Is it raining today? = {is_raining}")

print('\n----- Example 4: assigning values to multiple variables ----')
# declare multiple variables
item1, item2, item3 = "apples",25, False
print(f"item 1 = {item1}, item 2 = {item2}, item 3 = {item3}")
# declare multiple variables with the same value
score1 = score2 = score3 = 88
print(f"score 1 ={score1}, score 2 = {score2}, score 3 = {score3}")

print('\n---- Example 5: input command -----')
print("Enter username: ")
username = input()
print(f"collected username = {username}")

# Cast from string to integer
luckynumber = int(input("Enter a lucky number: "))
print(f"Lucky number = {luckynumber}")

# double the lucky number. 
dblucky = luckynumber*2
print(f"Double of lucky = {dblucky}")

# cast integer(or float)into string
triplenumber = str(dblucky) * 3
print(f"tripled the casted number = {triplenumber}")

# cast integer to bol value
# 0 = false, ay other number = Truep
completed_task = -20
print(f"completed task = {bool(completed_task)}")

print('\n---- Example 6: arithmatic operators ------')
num1 = 25
num2 = 9

print(f"The sum of {num1} is {num2} is \t{num1+num2}")
print(f"The different between {num1} is {num2} is \t{num1-num2}")
print(f"The product of {num1} is {num2} is {num1*num2}")
print(f"The quotient of of {num1} is {num2} is \t{num1/num2}")
print(f"The modulus(remainder) of {num1} is {num2} is \t{num1%num2}")
print(f"The integer of quotient of {num1} is {num2} is \t{num1//num2}")
print(f"The exponent of base {num2} to the power of 3 is \t{num2**3}")

print('\n---- Example 7: finding the hypotesuna ------')
# declare and assign values
x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))
# calculate the hypotenusa
hyp = (x**2 + y**2)**0.5
# prompt result
print(f"The hypotenuse of {x} and {y} is {hyp}")

print('\n---- Example 8: assignment operators ------')
n = 20
print(f"number =        {n}")
# assignment operator +
n +=3
print(f"number + 3 =     {n}")
# assignment operator -
n -=4
print(f"updated number = {n}")
# assignment operator *
n *= 2
print(f"updated * number = {n}")
# assignment operator /
n /= 3
print(f"updated / number = {n}")
# assignment operator // 
n //=2
print(f"updated // number = {n}")
# assignment operator **
n **= 2
print(f"updated ** number = {n}")
# modulus or remainder
n %= 5
print(f"updated %= number = {n}")

print('\n---- Example 8: comparison operators -----')
n1 = 10
n2 = 3
n3 = 7
compare1 = n1==n2
compare2 = n1==(n2+n3)
print(f"is n1 equal n2?     {compare1}")
print(f"is n1 = n2+n3?     {compare2}")
compare3 = n1>n2
compare4 = n2<=n3
print(f"is n1 greater than n2?  {compare3}")
print(f"is n2 less than or equal to n3?   {compare4}")

print('\n----- Example 10: string indexing -------')
username = "peterpan123"
# positive index
print(f"The fifth character = {username[4]}")

# negative index
print(f"The fifth last character = {username[-5]}")


print('\n----- Example 11: string slice ------')

# slice from the beginning to the 4th character
print(f"slice from beginning to 4th character    {username[:4]}")

# slice from the 5th character to the end
print(f"slice from the 5th character to the end   {username[6:]}")

# slice from the 3rd to 8th
print(f"slide from 3rd to 8th             = {username[2:8]}")

# slice from the 4th to the 6th character using negative index
print(f"slice from 4th to 6th using negative index = {username[-8:-5]}")

print('\n------- Example 12: total characters in a string (len) ---------')
print(f"the username has = {len(username)} characters")

print('\n------- Example 13: strip() method ---------')
username = "   PeterPAN123    "
print(f"The username = {username}. End of username")
username = username.strip()
print(f"The username after method strip = {username}. End of username")

print('\n------- Example 14: upper and lower method ---------')
username = username.lower()
print(f"The username after method lower = {username}. End of username")
username = username.upper()
print(f"The username after method upper = {username}. End of username")

print('\n------- Example 15: replace method ---------')
username = username.replace('P', '%')
print(f"The username after replace method = {username}. End of username")

print('\n------- Example 16: split method ---------')
msg = "Introduction to Python Programming! Today we are learning string methods"
print(f"Message =                      {msg}")
print(f"Message after split method =   {msg.split('!')}")

print('\n------- Example 17: find method ---------')
# find the letter 'P'
index_P = msg.find('P')
print(f"Index of letter P is =             {index_P}")
# find the second letter 'P'
sec_index_P = msg.find('P',index_P + 1)
print(f"Next index of letter P is =        {sec_index_P}")
# find a non-existing letter 'Y'
index_Y = msg.find('Y')
print(f"The index of letter is =       {index_Y}")

print('\n------- Example 18: in, not in statement ------')
# check if the word 'we' is in the msg string
answer_we = "we" in msg
print(f"is the word 'we' in the 'msg' string? =      {answer_we}")
answer_today = "Today" not in msg
print(f"is the word 'Today' NOT in the 'msg' string? =      {answer_today}")

print('\n------- Example 19: list indexing ------')
colors =["orange", "magenta", "olive"]
numbers = [6, 20, -9, 5, -12]
mixedlist = [False, 20, "Peter", True, -9]
emptylist = []

print(f"colors list =         {colors}")
print(f"numbers list =      {numbers}")
print(f"empty list =         {emptylist}")
print(f"Mixed list =        {mixedlist}")

print(f"2nd color =     {colors[1]}")
print(f"1st number =      {numbers[0]}")
# print(f"3rd value =      {emptylist[2]}")  # cant return empty character

print(f"last color =    {colors[-1]}")
print(f"3rd last number =     {numbers[-3]}")

print('\n------ Example 20: + * operator on list ------')
#concatenate the first with the last color
new_color = colors[0] + colors[-1]
print(f"The new color is =      {new_color}")
#concatenate the 2nd color with the 3rd number
# new_word = number1[1] + numbers[2] #--> type error
# print(f"The new word is       {new_word}")

print('\n----- Example 21 : remove items from a list -------')
# remove the 2nd last color
colors.pop(-2)
print(f"colors after pop =      {colors}")

print('\n----- Example 22 : adding item to the list -------')
# add items to the end of list colors
colors.append("PINK")
print(f"colors after append =    {colors}")
# add a new list to a list
colors.append(["blue","green"])
print(f"colors after append =     {colors}")
# add multiple items to a list
# colors.append("RED", "PURPLE") #--> argument error
print(f"colors after append =   {colors}")

print('\n----- Example 23 : sort method -------')
colors = ["orange", "magenta", "olive", "Magenta"]
print(f"color list =    {mixedlist}")
colors.sort()
print(f"color list sorted =   {colors}")

bool_list = [True, True, False]
bool_list.sort()
print(f"bool list sorted =   {bool_list}")

print('\n----- Example 24: count method ------')
count_true = bool_list.count(True)
print(f"There is {count_true} True values")
count_red = colors.count("red")
print(f"There is/are {count_red} red colors")

print('\n----- Example 25: length of list ------')
length_colors = len(colors)
print(f"There is/are {length_colors} colors")

print('\n----- Example 26: index of item in a list ------')
# index of color 'olive'
index_olive = colors.index("olive")
print(f"The index of color olive is   {index_olive}")
# index of color 'green'
# index_green = colors.index("green") #---> value error, cant return index of an unexisting value, is not in list
# print(f"The index of color green is   {index_green}")








































      
