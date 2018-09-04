"""This is the base class for entities in the game"""

import pygame
from pygame.locals import *

class Entitiy:
	"""docstring for Entitiy"""

	def __init__(self):
		self.position = [0, 0]
		self.animation_step = ''
		self.graphics  = {}
		self.sounds = {}
		self.dead = False

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