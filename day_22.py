from turtle import Screen
import paddle, ball, time, scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkeypress(fun = r_paddle.up, key = "Up")
screen.onkeypress(fun = r_paddle.down, key = "Down")
screen.onkeypress(fun = l_paddle.up, key = "w")
screen.onkeypress(fun = l_paddle.down, key = "s")

game_on = True
while game_on:
	screen.update()
	time.sleep(ball.move_speed)
	ball.move()

	# COLLISION WITH WALL
	if ball.ycor() > 280 or ball.ycor() <= -280:
		ball.bounce_y()

	# COLLISION WITH PADDLE
	if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
		ball.bounce_x()

	# DETECT WHEN RIGHT PADDLE MISSES THE BALL
	if ball.xcor() > 380:
		ball.reset_button()
		scoreboard.l_point()

	# DETECT WHEN LEFT PADDLE MISSES THE BALL
	if ball.xcor() < -380:
		ball.reset_button()
		scoreboard.r_point()

##
##
##
screen.exitonclick()
