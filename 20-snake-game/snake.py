from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.setpos(position)
        print(tim.position())
        self.snake.append(tim)


    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 

    def extend(self):
        self.add_segment(self.snake[-1].position())
        

    def __len__(self):
        return len(self.snake)

    def __getitem__(self, index):
        return self.snake[index]