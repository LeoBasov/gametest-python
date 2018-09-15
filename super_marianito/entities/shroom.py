import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
from entities.baseentity import BaseState
import math

class Running(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.animation_iter_max = 6

		self.front = False

		self.load_animation_step('./graphics/shroom.png', './graphics/shroom.png')

	def _move(self, addition):
		if self.front:
			self.position[0] += addition[0] + 1
			self.position[1] += addition[1]
		else:
			self.position[0] += addition[0] - 1
			self.position[1] += addition[1]

class Hiding(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.animation_iter_max = 6

		self.front = False

		self.load_animation_step('./graphics/shroom.png', './graphics/shroom.png')

	def _move(self, addition):
		if self.front:
			self.position[0] += addition[0]
			self.position[1] += addition[1]
		else:
			self.position[0] += addition[0]
			self.position[1] += addition[1]

class Ememrging(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.animation_iter_max = 6

		self.front = False
		self.done = False
		self.counter = 0

		self.load_animation_step('./graphics/shroom.png', './graphics/shroom.png')

	def _move(self, addition):
		if self.counter >= 15:
			self.done = True
		else:
			self.position[0] += addition[0]
			self.position[1] += addition[1] - 1

			self.counter += 1

	def reset(self, front):
		super().reset(front)

		self.done = False
		self.counter = 0

class Falling(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.falling_speed = 0
		self.falling_speed_max = 10
		self.iter_number = 10
		self.iter_step = 0.5*math.pi/self.iter_number
		self.iter_pos = 0
		self.iter = 0

		self.animation_iter_max = 4

		self.front = False

		self.load_animation_step('./graphics/shroom.png', './graphics/shroom.png')

	def _move(self, addition):
		if self.iter < self.iter_number:
			self.iter_pos += self.iter_step
			self.falling_speed = self.falling_speed_max*math.sin(self.iter_pos)
			self.iter += 1

		self.position[0] += addition[0]
		self.position[1] += addition[1] + self.falling_speed

	def reset(self, front):
		self.falling_speed = 0
		self.falling_speed_max = 10
		self.iter_number = 10
		self.iter_step = 0.5*math.pi/self.iter_number
		self.iter_pos = 0
		self.iter = 0

		self.animation_iter = 0
		self.animation_index = 0
		self.front = front

		if self.front:
			self.graphic = self.animation_front[self.animation_iter]
			self.bounding_box = self.bounding_boxes_front[self.animation_iter]
		else:
			self.graphic = self.animation_back[self.animation_iter]
			self.bounding_box = self.bounding_boxes_back[self.animation_iter]

class Shroom(Entitiy):
	"""docstring for ClassName"""

	def __init__(self, position):
		super().__init__()

		self.type = 'goodie'

		self.state_step = 'hide'

		self.position[0] = position[0]
		self.position[1] = position[1]

		self.death_range[1][1] = 224

		self.counter = 0

		self.load_sounds({'die': './sound/smb_kick.wav'})

		self._set_up_states()

	def _set_up_states(self):
		self.states['run'] = Running(self.position)
		self.states['fall'] = Falling(self.position)
		self.states['hide'] = Hiding(self.position)
		self.states['emerge'] = Ememrging(self.position)

	def kill(self):
		self.dead = True

	def check_death_range(self):
		if self.position[1] > self.death_range[1][1]:
			self.dead = True

	def evaluate_collisions(self):
		self.stuck = False

		for key, collision in self.collisions.items():
			if collision[0].collided and (collision[0].other.type=='level' or collision[0].other.type=='block'):
				if collision[0].left_in:
					self.states['run'].reset(True)
				elif collision[0].right_in:
					self.states['run'].reset(False)

		self.collisions = {}
				
	def move(self, addition):
		self.states[self.state_step].exec(addition)

		if self.state_step == 'emerge' and self.states[self.state_step].done:
			front = self.states[self.state_step].front

			self.state_step = 'run'
			self.states[self.state_step].reset(True)