import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#10 lanes between -250 and 250
#Y_LANES_POSITIONS = [-250, -200, -150, -100, 50, 0, 50, 100, 150, 200, 250]


class CarManager:

    def __init__(self):
        self.cars = []
        self.level_car_speed = STARTING_MOVE_DISTANCE
        self.add_cars()

    def add_cars(self):
        for i in range(1):
            new_car = Car(self.level_car_speed)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move()
    
    def increase_speed(self):
        for car in self.cars:
            self.level_car_speed += MOVE_INCREMENT*0.5
            car.increase_speed()

    def reset_position(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.reset_position()
                print('reset_position')


    def __len__(self):
        return len(self.cars)


class Car(Turtle):
    def __init__(self, car_speed=STARTING_MOVE_DISTANCE):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randint(-250,250))
        self.car_speed = car_speed


    def move(self):
        #Move the car to the left with car_speed
        new_x = self.xcor() 
        self.goto(new_x, self.ycor())
        self.goto(self.xcor() - self.car_speed, self.ycor())
        
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT*0.5

    def reset_position(self):
        self.goto(300, random.randint(-250, 250))

