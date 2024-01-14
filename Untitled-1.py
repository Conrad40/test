import turtle
import keyboard
import math
import time
Screen = turtle.Screen()
Screen.bgcolor("light green")
Screen.title("Turtle")
Screen.screensize(300,300)

T = turtle.Turtle()
T.width("2")
T.hideturtle()
T.speed(0)
def board():
    T.penup()
    T.goto(-150,-400)
    T.pendown()
    T.goto(-150,400)
    T.penup()
    T.goto(150,-400)
    T.pendown()
    T.goto(150,400)
    T.penup()

    T.goto(-480,-150)
    T.pendown()
    T.goto(480,-150)
    T.penup()
    T.goto(-500,150)
    T.pendown()
    T.goto(500,150)

def drawMark(pos,player):
    T.penup()
    Xs = [-350,0,350]
    Ys = [-300,0,300]
    T.goto(Xs[(pos-1)%3],-Ys[math.floor((pos-1)/3)])
    T.pendown()
    if player == 1:
        T.setheading(45)
        T.forward(80)
        T.backward(160)
        T.penup()
        T.goto(Xs[(pos-1)%3],-Ys[math.floor((pos-1)/3)])
        T.pendown()
        T.setheading(-45)
        T.forward(80)
        T.backward(160)
    if player==2:
        T.penup()
        T.sety(T.ycor()-40)
        T.setx(T.xcor()-40)
        T.pendown()
        T.circle(80)
#drawMark(1,1)
#drawMark(9,1)
#drawMark(5,2)
board()

def drawMap(game):
    I = 1
    board()
    for a in game:
        drawMark(I,int(a))
        I += 1

f = open("boards.txt", "r")
lines = f.readlines()
MoveF = open("spot.txt", 'r')
Done = sum(1 for line in MoveF)
MoveF.close()
MoveF = open("spot.txt", 'a')
i =0
for line in lines:
    #print(line, end="")
    line = line.replace("\n", "")
    i += 1
    
    if i > Done:
        MoveF.close()
        MoveF = open("spot.txt", 'a')
        drawMap(line)
        while True:
            if keyboard.is_pressed('1'):
                MoveF.write('1\n')
                break
            if keyboard.is_pressed('2'):
                MoveF.write('2\n')
                break
            if keyboard.is_pressed('3'):
                MoveF.write('3\n')
                break
            if keyboard.is_pressed('4'):
                MoveF.write('4\n')
                break
            if keyboard.is_pressed('5'):
                MoveF.write('5\n')
                break
            if keyboard.is_pressed('6'):
                MoveF.write('6\n')
                break
            if keyboard.is_pressed('7'):
                MoveF.write('7\n')
                break
            if keyboard.is_pressed('8'):
                MoveF.write('8\n') 
                break
            if keyboard.is_pressed('9'):
                MoveF.write('9\n')
                break
            if keyboard.is_pressed(' '):
                MoveF.close()
        #time.sleep(.5)        
        T.clear()
    
   

MoveF.close()


while True:
    if keyboard.is_pressed('a'):
        T.left(5)
    if keyboard.is_pressed('d'):
        T.right(5)
    if keyboard.is_pressed('w'):
        T.forward(5)
    if keyboard.is_pressed(' '):
        T.home()       
    if keyboard.is_pressed('s'):
        T.goto(0,300)
T.forward(100)
turtle.done()