"""This is the base class for entities in the game"""

import pygame
from pygame.locals import *

class Collision:

	def __init__(self):
		self.collided = False
		self.position = [0, 0]
		self.left_in = False
		self.right_in = False
		self.top_in = False
		self.buttom_in = False

class Entitiy:
	"""docstring for Entitiy"""

	def __init__(self):
		self.position = [0, 0]
		self.extension = [0, 0]
		self.animation_step = ''
		self.graphics  = {}
		self.sounds = {}
		self.dead = False
		self.collisions = {}
		self.death_range = [[0, 0],[0, 0]]

	def load_graphic(self, file_names):
		for key, file_name in file_names.items():
			self.graphics[key] =  pygame.image.load(file_name)

	def load_sounds(self, file_names):
		for key, file_name in file_names.items():
			self.sounds[key] =  pygame.mixer.Sound(file_name)

	def process_events(self, events):
		pass

	def move(self, addition):
		pass

	def print(self, surface_surf):
		surface_surf.blit(self.graphics[self.animation_step], (self.position[0], self.position[1]))

	def kill(self):
		pass

	def check_collision(self, other, key):
		collision = self._check_collision(other)

		if collision.collided:
			if not key in self.collisions:
				self.collisions[key] = [collision]
			else:
				self.collisions[key].append(collision)

	def _check_collision(self, other):
		collision = Collision()

		if ((self.position[0] + self.extension[0]) > other.position[0]) \
		and ((self.position[0] + self.extension[0]) < (other.position[0] + other.extension[0])):
			collision.right_in = True

		if ((self.position[0]) > other.position[0]) \
		and ((self.position[0]) < (other.position[0] + other.extension[0])):
			collision.left_in = True

		if ((self.position[1] + self.extension[1]) > other.position[1]) \
		and ((self.position[1] + self.extension[1]) < (other.position[1] + other.extension[1])):
			collision.buttom_in = True

		if ((self.position[1]) > other.position[1]) \
		and ((self.position[1]) < (other.position[1] + other.extension[1])):
			collision.top_in = True

		if (collision.right_in or collision.left_in) and (collision.buttom_in or collision.top_in):
			collision.collided = True

		return collision

	def evaluate_collisions(self):
		self.collisions = {}