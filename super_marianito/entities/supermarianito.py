import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
import math

class SuperMarianito(Entitiy):
	"""docstring for ClassName"""

	def __init__(self):
		super().__init__()

		self.position[0] = 50
		self.position[1] = 180

		self.jumping = False
		self.start = 0
		self.height = 50
		self.iter = 0
		self.iter_length = 0.1

		self.animation_step = 'walk_1'

	def process_events(self, events):
		for event in events:
			if (event.type == KEYDOWN) and (event.key == K_UP) and (not self.jumping):
				self.jumping = True
				self.animation_step = 'jump'
				self.start = self.position[1]
				self.position[1] -= 1
				self.iter = self.iter_length

	def move(self, addition):
		if self.jumping and (self.position[1] < self.start):
			self.position[1] = self.start - self.height*math.sin(self.iter)
			self.iter += self.iter_length
		elif self.jumping and (self.position[1] >= self.start):
			self.position[1] = self.start
			self.jumping = False
			self.animation_step = 'walk_1'
		else:
			self.iter = self.iter_length
			self.jumping = False
			self.animation_step = 'walk_1'
