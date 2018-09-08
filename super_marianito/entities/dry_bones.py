import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
from entities.baseentity import BaseState
import math

class Running(BaseState):
	"""docstring"""

	def __init__(self, position):
		super().__init__(position)

		self.animation_iter_max = 4

		self.front = False

		self.load_animation_step('./graphics/drybones_w_1.png', './graphics/drybones_w_1.png')
		self.load_animation_step('./graphics/drybones_w_2.png', './graphics/drybones_w_2.png')
		self.load_animation_step('./graphics/drybones_w_3.png', './graphics/drybones_w_3.png')
		self.load_animation_step('./graphics/drybones_w_4.png', './graphics/drybones_w_4.png')
		self.load_animation_step('./graphics/drybones_w_5.png', './graphics/drybones_w_5.png')
		self.load_animation_step('./graphics/drybones_w_6.png', './graphics/drybones_w_6.png')
		self.load_animation_step('./graphics/drybones_w_7.png', './graphics/drybones_w_7.png')

	def _move(self, addition):
		self.position[0] += addition[0] - 1
		self.position[1] += addition[1]

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

		self.load_animation_step('./graphics/drybones_w_1.png', './graphics/drybones_w_1.png')
		self.load_animation_step('./graphics/drybones_w_2.png', './graphics/drybones_w_2.png')
		self.load_animation_step('./graphics/drybones_w_3.png', './graphics/drybones_w_3.png')
		self.load_animation_step('./graphics/drybones_w_4.png', './graphics/drybones_w_4.png')
		self.load_animation_step('./graphics/drybones_w_5.png', './graphics/drybones_w_5.png')
		self.load_animation_step('./graphics/drybones_w_6.png', './graphics/drybones_w_6.png')
		self.load_animation_step('./graphics/drybones_w_7.png', './graphics/drybones_w_7.png')

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

class Dying(BaseState):
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

		self.load_animation_step('./graphics/drybones_w_1.png', './graphics/drybones_w_1.png')
		self.load_animation_step('./graphics/drybones_w_2.png', './graphics/drybones_w_2.png')
		self.load_animation_step('./graphics/drybones_w_3.png', './graphics/drybones_w_3.png')
		self.load_animation_step('./graphics/drybones_w_4.png', './graphics/drybones_w_4.png')
		self.load_animation_step('./graphics/drybones_w_5.png', './graphics/drybones_w_5.png')
		self.load_animation_step('./graphics/drybones_w_6.png', './graphics/drybones_w_6.png')
		self.load_animation_step('./graphics/drybones_w_7.png', './graphics/drybones_w_7.png')

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

class DryBonesOld(Entitiy):
	"""docstring for ClassName"""
	def __init__(self):
		super().__init__()

		self.position[0] = 200
		self.position[1] = 165

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

class DryBones(Entitiy):
	"""docstring for ClassName"""

	def __init__(self):
		super().__init__()

		self.state_step = 'run'

		self.position[0] = 200
		self.position[1] = 165

		self._set_up_states()
		self._set_up_sounds()

	def _set_up_states(self):
		self.states['run'] = Running(self.position)
		self.states['fall'] = Falling(self.position)
		self.states['die'] = Dying(self.position)

	def _set_up_sounds(self):
		pass

	def process_events(self, events):
		pass

	def evaluate_collisions(self):
		if self.state_step == 'run':
			for key, collision in self.collisions.items():
				if key == 'sup' and collision[0].collided:
					self.sounds['die'].play()
					self.state_step = 'die'
					self.states[self.state_step].reset(False)

			self.collisions = {}