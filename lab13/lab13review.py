"""
Irsan Sutanto
May 4, Python class review
"""
# example 1: review of __init__
class Person:
    def __init__(self, name, age):
        self.username = name
        self.user_age = age

    def __str__(self):
        return f"Username = {self.username}\nUser age = {self.user_age}"
    
    # method
    def intro(self):
        return f"Hallooo! I am {self.username}"

print("\n---- Example 1-----")
# create an object of the class
user1 = Person("Peter", 23)
print(user1.intro())

# example 2, private properties
print("\n--- Example 2 -----")
class Chair:
    #accessible property
    chair_color = "brown"

    def __init__(self, height, width, length):
        self.chairheight = height
        self.__width = width  # __ makes property width to be very private
        self.chairlength = length*2

    # method to pass the length
    def pass_length(self):
        return self.chairlength
    
    # method to return the volume of the chair
    def chair_volume(self):
        return self.chairheight * self.chairlength * self.__width
    
    # method to return the color of the chair
    def get_color(self):
        return self.chair_color

    # method to return the description of the chair
    def chair_description(self):
        return f"The total volume of the chair {self.chair_volume()}. The chair color is {self.get_color()}"
    
    # method with a private property
    def setprice(self,price):
        self._chairprice = price


# create an object
userchair1 = Chair(2,5,9)
print(f"The chair length is = {userchair1.chairlength}")
print(f"The chair width is = {userchair1._Chair__width}")
# call method pass_length
print(f"The chair has length = {userchair1.pass_length()}")
print(f"The chair volume is = {userchair1.chair_volume()}")
print(userchair1.chair_description())
# call private method
userchair1.setprice(25)
print(f"The price of the chair is $ {userchair1._chairprice}")





