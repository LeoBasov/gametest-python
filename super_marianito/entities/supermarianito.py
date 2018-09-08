import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
from entities.baseentity import BaseState
import math

class Standing(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.load_animation_step('./graphics/sup.png', './graphics/sup_back.png')

class Running(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.animation_iter_max = 4

		self.load_animation_step('./graphics/sup_walk.png', './graphics/sup_walk_back.png')
		self.load_animation_step('./graphics/sup.png', './graphics/sup_back.png')

class Jumping(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.start = self.position[1]
		self.height = 50
		self.jump_iter_step = 0.1
		self.jump_iter = self.jump_iter_step
		self.done = False

		self.load_animation_step('./graphics/sup_jump.png', './graphics/sup_jump_back.png')

	def reset(self, front):
		self.jump_iter = self.jump_iter_step
		self.start = self.position[1]
		self.animation_iter = 0
		self.animation_index = 0
		self.front = front
		self.done = False

	def _move(self, addition):
		self.position[1] = self.start - self.height*math.sin(self.jump_iter)
		self.jump_iter += self.jump_iter_step

		if self.position[1] <= self.start - 0.99*self.height:
			self.done = True

class Falling(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.load_animation_step('./graphics/sup_jump.png', './graphics/sup_jump_back.png')

	def _move(self, addition):
		pass

class SuperMarianito(Entitiy):
	"""docstring for ClassName"""

	def __init__(self):
		super().__init__()

		self.state_step = 'jump'

		self.position[0] = 50
		self.position[1] = 180

		self._set_up_states()
		self._set_up_sounds()

	def _set_up_states(self):
		self.states['stand'] = Standing(self.position)
		self.states['run'] = Running(self.position)
		self.states['jump'] = Jumping(self.position)
		self.states['fall'] = Falling(self.position)

	def _set_up_sounds(self):
		pass

	def process_events(self, events):
		if self.state_step=='jump' and self.states[self.state_step].done:
			self.state_step = 'fall'
			self.states[self.state_step].reset(self.states[self.state_step].front)

		for event in events:
			if (event.type == KEYDOWN) and (event.key == K_RIGHT) and ((not self.state_step=='run') or (not self.states[self.state_step].front)):
				self.state_step = 'run'
				self.states[self.state_step].reset(True)
			elif (event.type == KEYDOWN) and (event.key == K_LEFT) and ((not self.state_step=='run') or (self.states[self.state_step].front)):
				self.state_step = 'run'
				self.states[self.state_step].reset(False)
			elif (event.type == KEYUP) and (event.key == K_RIGHT) and not self.state_step=='jump':
				self.state_step = 'stand'
				self.states[self.state_step].reset(True)
			elif (event.type == KEYUP) and (event.key == K_LEFT) and not self.state_step=='jump':
				self.state_step = 'stand'
				self.states[self.state_step].reset(False)

	def move(self, addition):
		self.states[self.state_step].exec(addition)