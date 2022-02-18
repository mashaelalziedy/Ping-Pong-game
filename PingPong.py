import turtle
#set the screen of our game from turtle module
wind =turtle.Screen()
#write the title of window
wind.title("ping pong game")
#set the background color
wind.bgcolor("black")
#set the hight and width of the window
wind.setup(width=800, height=600)
#don't update the window
wind.tracer(0)

#draw mallet1
mallet1=turtle.Turtle()
mallet1.speed(0) #to update mallet1 fast 
mallet1.shape("square")
mallet1.color("blue")
mallet1.penup() #don't draw lines after moving mallet1
#the position of mallet1
mallet1.goto(-350,0)
#set the size of mallet1
mallet1.shapesize(stretch_wid=5,stretch_len=1) #20 is the defualt width size. 20*5=100
#draw mallet2
mallet2=turtle.Turtle()
mallet2.speed(0)
mallet2.shape("square")
mallet2.color("white")
mallet2.penup()
mallet2.goto(350,0) #the center of square(mallet2) is at 350 and 0
mallet2.shapesize(stretch_wid=5,stretch_len=1)
#draw the ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0,0)
#movement of ball
ball.dx=0.25 #move right by 0.25 
ball.dy=0.25 #move up
#calculate scores
score1=0
score2=0
score =turtle.Turtle()
score.speed(0)
score.color("purple")
score.penup()
score.hideturtle() #hide score object 
score.goto(0,260)
score.write("player 1: 0  player 2:0 ", align="center", font=("Courier",18,"normal"))

#functions 
#move mallet1 and mallet2 up and down
def mallet1_up():
    
    y=mallet1.ycor() #variable to keep current y position 
    if y<230:
        y+=20 #increase y position by 20
        mallet1.sety(y) #set the new y

    

def mallet1_down():
    y=mallet1.ycor()
    if y>-230:
        y-=20 
        mallet1.sety(y)
    

def mallet2_up():
    y=mallet2.ycor()
    if y<230:
        y+=20
        mallet2.sety(y)

def mallet2_down():
    y=mallet2.ycor()
    if y>-230:
        y-=20
        mallet2.sety(y)

     
   
#keyboard bindings, so we can move the mallets by using keyboard buttons
wind.listen() #wait until the keyboard pressed 
wind.onkeypress(mallet1_up, "w") #move up by w button 
wind.onkeypress(mallet1_down,"s") #move down by s button
wind.onkeypress(mallet2_up, "Up") #moving by arrow buttons
wind.onkeypress(mallet2_down,"Down")

#loop to keep the window show up 
while True:
    wind.update()
    #move the ball and keep moving the ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)
    #make sure that the ball will never go out the window 
    if ball.ycor()>290:
        ball.sety(290) 
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290) 
        ball.dy *= -1
    #the user will lose if he didn't catch the ball
    if ball.xcor()>390:
        ball.goto(0,0) #the user didn't catch the ball? then go to the center 
        ball.dx *= -1 #move in opposite direction
        if score1 !=4: #when the score become 5 the player1 wins
            score1 +=1
            score.goto(0,260)
            score.clear()
            score.write("player 1: {}  player 2: {} ".format(score1,score2), align="center", font=("Courier",18,"normal"))
        else:
            score.clear()
            score.goto(0,0)
            score.write("player1 is the winner, play again",align="center",font=("Courier",24,"normal"))
            score1=0
            score2=0
    if ball.xcor()<-390:
        ball.goto(0,0) 
        ball.dx *= -1
        if score2 !=4: #when the score become 5 the player2 wins
            score2 +=1
            score.goto(0,260)
            score.clear()
            score.write("player 1: {}  player 2: {} ".format(score1,score2), align="center", font=("Courier",18,"normal"))
        else:
            score.clear()
            score.goto(0,0)
            score.write("player2 is the winner, play again",align="center",font=("Courier",24,"normal"))
            score1=0
            score2=0   
    #when the ball hit the mallet move the ball in opposite direction
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < mallet2.ycor() +40 and ball.ycor() > mallet2.ycor() -40):
        ball.setx(340) 
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < mallet1.ycor() +40 and ball.ycor() > mallet1.ycor() -40):
        ball.setx(-340) 
        ball.dx *= -1   

