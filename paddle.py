from turtle import Turtle


class Paddle(Turtle):

	def __init__(self, position):
		"""Assign either 'l' or 'r' as the argument for direction"""
		super().__init__()
		self.color("white")
		self.penup()
		self.shape("square")
		self.shapesize(stretch_wid = 5, stretch_len = 1)
		self.goto(position)

	def up(self):
		new_y = self.ycor() + 20
		self.sety(new_y)

	def down(self):
		new_y = self.ycor() - 20
		self.sety(new_y)
