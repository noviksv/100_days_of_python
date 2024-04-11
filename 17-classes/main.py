class User:
    # Constructor
    # self is the instance of the class
    # first_name and last_name are the parameters
    # __init__ is the constructor
    # self.first_name and self.last_name are the instance variables
    # first_name and last_name are the local variables
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.followers = 0 # Default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = User("Alex", "Bowman")
user2 = User("Dave", "Bowman")



#you can add new attributes to an instance of a class outside the class definition itself
user1.some_attribute = "some value"
print(user1.some_attribute)


user1.follow(user2)
user2.follow(user1)
print(user1.following)
print(user1.followers)
print(user2.following)
print(user2.followers)

