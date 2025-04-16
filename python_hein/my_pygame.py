import pygame
#Pygame is here only for test purposes to display things.
#Delete every pygame related lines or comment them out.

class Rectangle:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.speedx = 0
		self.speedy = 0
		self.maxspeedx = 0
		self.maxspeedy = 0

		self.pygame = pygame.Rect(x, y, width, height)
	
	@property
	def top(self):
		return self.y

	@top.setter
	def top(self, newtop):
		self.y = newtop
		self.pygame.top = newtop

	@property
	def bot(self):
		return self.y + self.height

	@bot.setter
	def bot(self, newbot):
		self.y = newbot - self.height
		self.pygame.y = newbot - self.height

	@property
	def left(self):
		return self.x

	@left.setter
	def left(self, newleft):
		self.x = newleft
		self.pygame.x = newleft

	@property
	def right(self):
		return self.x + self.width

	@right.setter
	def right(self, newright):
		self.x = newright - self.width
		self.pygame.x = newright - self.width

	@property
	def center(self):
		return (self.x + self.width/2, self.y + self.height)

	@center.setter
	def center(self, newcenter):
		self.x = newcenter[0] - self.width/2
		self.pygame.x = newcenter[0] - self.width/2
		self.y = newcenter[1] - self.height/2
		self.pygame.y = newcenter[1] - self.height/2