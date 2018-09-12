import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
from entities.baseentity import BaseState
import math

class Hanging(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.animation_iter_max = 7

		self.front = True

		self.load_animation_step('./graphics/q_block_1.png', './graphics/q_block_1.png')
		self.load_animation_step('./graphics/q_block_2.png', './graphics/q_block_2.png')
		self.load_animation_step('./graphics/q_block_3.png', './graphics/q_block_3.png')
		self.load_animation_step('./graphics/q_block_4.png', './graphics/q_block_4.png')

	def _move(self, addition):
		self.position[0] += addition[0]
		self.position[1] += addition[1]

class QuestionBlock(Entitiy):
	"""docstring for ClassName"""

	def __init__(self, position):
		super().__init__()

		self.type = 'q_block'

		self.state_step = 'hang'

		self.position[0] = position[0]
		self.position[1] = position[1]

		self._set_up_states()
		self._set_up_sounds()

	def _set_up_states(self):
		self.states['hang'] = Hanging(self.position)

	def _set_up_sounds(self):
		pass

	def evaluate_collisions(self):
		pass