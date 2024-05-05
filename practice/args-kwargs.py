
#passing positional arguments
def add(*args):
    #args has type tuple
    print(type(args))
    return sum(args)


print(add(1,2,3))


#passing keyword arguments
def calculate(n, **kwargs):
    #kwargs has type dict
    print(type(kwargs))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model)