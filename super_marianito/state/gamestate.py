"""game state module"""

import pygame, sys
from pygame.locals import *
from state.level import Level

class Move:

	def __init__(self):
		self.move_speed = [0, 0]

class GameState:
	"""docstring for Entitiy"""

	def __init__(self):
		self.entities = {}
		self.level = Level()
		self.move = Move()

	def create_level(self, file_name):
		self.level.graphic =  pygame.image.load(file_name)

	def exec(self, events):
		self._process_events(events)
		self._move()
		self._check_collisions(events)

	def _process_events(self, events):
		for event in events:
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

	def _move(self):
		pass

	def _check_collisions(self, events):
		pass

	def add_entitiy(self,entity_key_pair):
		if entity_key_pair[0] in self.entities:
			raise Exception('Entitiy exists')
		else:
			self.entities[entity_key_pair[0]] = entity_key_pair[1]

	def remove_entitiy(self,entity_key):
		del self.entities[entity_key_pair[0]]

	def print(self, surface_surf):
		self._print_level(surface_surf)

	def _print_level(self, surface_surf):
		surface_surf.blit(self.level.graphic, (0, 0))