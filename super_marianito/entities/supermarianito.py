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

		self.animation_step = 'stand'

		self.walking = False
		self.walk_it = 0
		self.walk_max1 = 4
		self.walk_max2 = 8

	def process_events(self, events):
		for event in events:
			if (event.type == KEYDOWN) and (event.key == K_UP) and (not self.jumping):
				self.jumping = True
				self.walking = False
				self.animation_step = 'jump'
				self.start = self.position[1]
				self.position[1] -= 1
				self.iter = self.iter_length
			elif (event.type == KEYDOWN) and (event.key == K_RIGHT) and (not self.jumping):
				self.walking = True
			elif (event.type == KEYUP) and (event.key == K_RIGHT) and (not self.jumping):
				self.walking = False

	def move(self, addition):
		if self.jumping and (self.position[1] < self.start):
			self.position[1] = self.start - self.height*math.sin(self.iter)
			self.iter += self.iter_length
		elif self.jumping and (self.position[1] >= self.start):
			self.position[1] = self.start
			self.jumping = False
			self.walking = True
			self.animation_step = 'stand'

		if self.walking and self.walk_it<=self.walk_max1:
			self.animation_step = 'walk'
			self.walk_it += 1
		elif self.walking and self.walk_it<self.walk_max2:
			self.animation_step = 'stand'
			self.walk_it += 1
		elif self.walking and self.walk_it>=self.walk_max2:
			self.walk_it = 0
		
		if not self.walking and not self.jumping:
			self.animation_step = 'stand'

