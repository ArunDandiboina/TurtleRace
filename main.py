import random
from turtle import Turtle,Screen
color = ["violet","blue","green","yellow","orange","red"]
screen = Screen()
w= Turtle()
w.hideturtle()
screen.setup(600,600)
pos = [(-260,0),(-260,-60),(-260,60),(-260,120),(-260,-120),(-260,180)]

user_ans = (screen.textinput("Turtle race","Which color turtle wins the race?\n\nviolet, blue, green, yellow, orange, red\n")).lower()

tur_list = []
k=0
for x in color:
    t = Turtle(shape="turtle")
    t.color(x)
    t.penup()
    t.setposition(pos[k])
    tur_list.append(t)
    k += 1

race_on = False
if user_ans:
    race_on = True
while race_on:
    for t in tur_list:
        k= random.randint(0,10)
        t.forward(k)
        if t.xcor()>260:
            winner = t.pencolor()

            if user_ans == winner:
                w.write(f"You Won! {user_ans} turtle wins the race.", align="center", font=("Arial", 15, "normal"))
            else:
                w.write(f"You lose! {winner} turtle won the race.", align="center", font=("Arial", 15, "normal"))
            race_on=False



screen.exitonclick()

