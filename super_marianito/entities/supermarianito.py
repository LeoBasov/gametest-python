import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
from entities.baseentity import BaseAnimation
import math


class Running(BaseAnimation):
	"""docstring"""

	def __init__(self):
		super().__init__()

		self.animation_front.append(pygame.image.load('./graphics/sup.png'))
		self.animation_front.append(pygame.image.load('./graphics/sup_walk.png'))

		self.animation_back.append(pygame.image.load('./graphics/sup_back.png'))
		self.animation_back.append(pygame.image.load('./graphics/sup_walk_back.png'))

class Jumping(BaseAnimation):
	"""docstring"""

	def __init__(self):
		super().__init__()

		self.animation_front.append(pygame.image.load('./graphics/sup_jump.png'))

		self.animation_back.append(pygame.image.load('./graphics/sup_jump_back.png'))

class Falling(BaseAnimation):
	"""docstring"""

	def __init__(self):
		super().__init__()

		self.animation_front.append(pygame.image.load('./graphics/sup_jump.png'))

		self.animation_back.append(pygame.image.load('./graphics/sup_jump_back.png'))

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

		self.walking = True
		self.walking_pressed = False
		self.walk_it = 0
		self.walk_max1 = 4
		self.walk_max2 = 8

		self.facing_front = True

	def process_events(self, events):
		for event in events:
			if (event.type == KEYDOWN) and (event.key == K_UP) and (not self.jumping):
				self.jumping = True
				self.walking = False
				self.start = self.position[1]
				self.position[1] -= 1
				self.iter = self.iter_length
				self.sounds['jump'].play()

				if self.facing_front:
					self.animation_step = 'jump'
				else:
					self.animation_step = 'jump_back'

			elif (event.type == KEYDOWN) and (event.key == K_RIGHT):
				self.facing_front = True
				self.walking_pressed = True
			elif (event.type == KEYUP) and (event.key == K_RIGHT):
				self.walking_pressed = False
			elif (event.type == KEYDOWN) and (event.key == K_LEFT):
				self.facing_front = False
				self.walking_pressed = True
			elif (event.type == KEYUP) and (event.key == K_LEFT):
				self.walking_pressed = False

	def move(self, addition):
		if self.jumping and (self.position[1] < self.start):
			self.position[1] = self.start - self.height*math.sin(self.iter)
			self.iter += self.iter_length
		elif self.jumping and (self.position[1] >= self.start):
			self.position[1] = self.start
			self.jumping = False
			self.walking = True

			if self.facing_front:
				self.animation_step = 'stand'
			else:
				self.animation_step = 'stand_back'

		if self.walking and self.walking_pressed and self.walk_it<=self.walk_max1:
			self.walk_it += 1

			if self.facing_front:
				self.animation_step = 'walk'
			else:
				self.animation_step = 'walk_back'

		elif self.walking and self.walking_pressed and self.walk_it<self.walk_max2:
			self.walk_it += 1

			if self.facing_front:
				self.animation_step = 'stand'
			else:
				self.animation_step = 'stand_back'

		elif self.walking and self.walking_pressed and self.walk_it>=self.walk_max2:
			self.walk_it = 0
		
		if (not self.walking or not self.walking_pressed) and not self.jumping:
			if self.facing_front:
				self.animation_step = 'stand'
			else:
				self.animation_step = 'stand_back'

