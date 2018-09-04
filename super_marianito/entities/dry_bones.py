import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
import math

class DryBones(Entitiy):
	"""docstring for ClassName"""
	def __init__(self):
		super().__init__()

		self.position[0] = 200
		self.position[1] = 165

		self.extension[0] = 25
		self.extension[1] = 20

		self.animation_step = 'walk_1'

		self.walk_it = 0
		self.walk_max1 = 6
		self.walk_max2 = 2*self.walk_max1
		self.walk_max3 = 3*self.walk_max1
		self.walk_max4 = 4*self.walk_max1
		self.walk_max5 = 5*self.walk_max1
		self.walk_max6 = 6*self.walk_max1
		self.walk_max7 = 7*self.walk_max1

	def move(self, addition):
		self.position[0] += addition[0] - 1
		self.position[1] += addition[1]

		if self.walk_it<=self.walk_max1:
			self.animation_step = 'walk_1'
			self.walk_it += 1
		elif self.walk_it<self.walk_max2:
			self.animation_step = 'walk_2'
			self.walk_it += 1
		elif self.walk_it<self.walk_max3:
			self.animation_step = 'walk_3'
			self.walk_it += 1
		elif self.walk_it<self.walk_max4:
			self.animation_step = 'walk_4'
			self.walk_it += 1
		elif self.walk_it<self.walk_max5:
			self.animation_step = 'walk_5'
			self.walk_it += 1
		elif self.walk_it<self.walk_max6:
			self.animation_step = 'walk_6'
			self.walk_it += 1
		elif self.walk_it<self.walk_max7:
			self.animation_step = 'walk_7'
			self.walk_it += 1
		elif self.walk_it>=self.walk_max7:
			self.walk_it = 0

	def evaluate_collisions(self):
		for key, collision in self.collisions.items():
			if key == 'sup' and collision[0].left and collision[0].right and collision[0].top and collision[0].buttom:
				self.dead = True

		self.collisions = {}