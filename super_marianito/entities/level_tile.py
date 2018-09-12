import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
from entities.baseentity import BaseState
import math

class Hanging(BaseState):
	"""docstring"""

	def __init__(self, position, file_name):
		super().__init__(position)

		self.load_animation_step(file_name, file_name)
		self.load_animation_step(file_name, file_name)
		self.load_animation_step(file_name, file_name)
		self.load_animation_step(file_name, file_name)

	def _move(self, addition):
		self.position[0] += addition[0]
		self.position[1] += addition[1]

class LevelTile(Entitiy):
	"""docstring for ClassName"""

	def __init__(self, position, file_name):
		super().__init__()

		self.type = 'level'

		self.state_step = 'hang'

		self.position[0] = position[0]
		self.position[1] = position[1]

		self._set_up_states(file_name)

	def _set_up_states(self, file_name):
		self.states['hang'] = Hanging(self.position, file_name)