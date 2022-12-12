import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('brown')
t.pencolor('pink')
t.speed(80)

col = ('purple', 'yellow', 'blue', 'green', 'white')
t.goto(0, 30)
for n in range(6):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
 
t.color('black')
t.penup()
t.goto(0, -260)
t.write('SEMANGAT RISMA CANTIK', align='center', font='Times 20 normal')
turtle.done()

s.exitonclick()

