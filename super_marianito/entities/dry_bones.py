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

		self.dieing = False
		self.start = 0
		self.height = 10
		self.iter = 0
		self.iter_length = 0.4

		self.last_addition = 0

	def _move(self, addition):
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

	def _die(self, addition):
		if self.position[1] <= self.start:
			self.position[1] = self.start - self.height*math.sin(self.iter)
			self.iter += self.iter_length
			self.last_addition = self.height*math.sin(self.iter)
		else:
			self.position[1] -= self.last_addition

		self.position[0] += addition[0]
		self.position[1] += addition[1]

	def move(self, addition):
		if self.death_range[1][1] < self.position[1]:
			self.dead = True
		elif self.dieing:
			self._die(addition)
		else:
			self._move(addition)

	def evaluate_collisions(self):
		if not self.dieing:
			for key, collision in self.collisions.items():
				if key == 'sup' and collision[0].collided:
					self.sounds['die'].play()
					self.dieing = True
					self.start = self.position[1]

			self.collisions = {}
			