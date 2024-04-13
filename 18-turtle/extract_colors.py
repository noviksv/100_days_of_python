import colorgram
import turtle as t
import random



# Extract 6 colors from an image
colors = colorgram.extract('hirst.jpg', 10)

print(colors)
#convert colors to list of RGB tuples
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
print(rgb_colors)
cols = rgb_colors #[(235, 234, 231), (235, 229, 232), (230, 237, 232), (223, 232, 237), (235, 36, 108), (143, 28, 66)]

franak = t.Turtle()
t.colormode(255)

#paint a dot

for __ in range(10):
    franak.setpos(0, __*30)
    for _ in range(10):
        franak.pendown()
        franak.dot(20, random.choice(cols)) 
        franak.penup()
        franak.forward(30)

franak.hideturtle()
t.done()