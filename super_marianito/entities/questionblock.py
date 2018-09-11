import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
from entities.baseentity import BaseState
import math

class Hanging(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.animation_iter_max = 4

		self.front = True

		self.load_animation_step('./graphics/block_1.png', './graphics/block_1.png')
		self.load_animation_step('./graphics/block_2.png', './graphics/block_2.png')
		self.load_animation_step('./graphics/block_3.png', './graphics/block_3.png')
		self.load_animation_step('./graphics/block_4.png', './graphics/block_4.png')

	def _move(self, addition):
		self.position[0] += addition[0]
		self.position[1] += addition[1]

class DryBones(Entitiy):
	"""docstring for ClassName"""

	def __init__(self):
		super().__init__()

		self.state_step = 'hang'

		self.position[0] = 200
		self.position[1] = 100

		self._set_up_states()
		self._set_up_sounds()

	def _set_up_states(self):
		self.states['hang'] = Hanging(self.position)

	def _set_up_sounds(self):
		pass

	def process_events(self, events):
		pass

	def evaluate_collisions(self):
		pass