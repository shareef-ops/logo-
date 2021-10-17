import turtle
turtle. bgcolor('black')
turtle. pensize(10) 
turtle. speed(0)

for i in range(15):
    for colours in ['white', 'blue', 'red', 'gray', 'purple', 'pink', 'yellow']:
        turtle.color(colours)
        turtle.circle(200)
        turtle. left(25) 
        turtle. hideturtle()