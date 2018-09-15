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
		self.height = 80
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

		if self.front:
			self.graphic = self.animation_front[self.animation_iter]
			self.bounding_box = self.bounding_boxes_front[self.animation_iter]
		else:
			self.graphic = self.animation_back[self.animation_iter]
			self.bounding_box = self.bounding_boxes_back[self.animation_iter]

	def _move(self, addition):
		self.position[1] = self.start - self.height*math.sin(self.jump_iter)
		self.jump_iter += self.jump_iter_step

		if self.position[1] <= self.start - 0.99*self.height:
			self.done = True

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

		self.load_animation_step('./graphics/sup_jump.png', './graphics/sup_jump_back.png')

	def _move(self, addition):
		if self.iter < self.iter_number:
			self.iter_pos += self.iter_step
			self.falling_speed = self.falling_speed_max*math.sin(self.iter_pos)
			self.iter += 1

		self.position[1] += self.falling_speed

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

class SuperMarianito(Entitiy):
	"""docstring for ClassName"""

	def __init__(self):
		super().__init__()

		self.state_step = 'stand'

		self.position[0] = 50
		self.position[1] = 185

		self.start_falling = False

		self.death_range[1][1] = 224

		self.stuck = False

		self._set_up_states()
		self._set_up_sounds()

	def _set_up_states(self):
		self.states['stand'] = Standing(self.position)
		self.states['run'] = Running(self.position)
		self.states['jump'] = Jumping(self.position)
		self.states['fall'] = Falling(self.position)

	def _set_up_sounds(self):
		pass

	def process_events(self, events, moving):
		if self.state_step == 'stand':
			self._process_for_stand(events, moving)
		elif self.state_step == 'run':
			self._process_for_run(events, moving)
		elif self.state_step == 'jump':
			self._process_for_jump(events, moving)
		elif self.state_step == 'fall':
			self._process_for_fall(events, moving)

	def _process_for_stand(self, events, moving):
		if not len(events) and moving:
			self.state_step = 'run'
			self.states[self.state_step].reset(self.states['stand'].front)

		for event in events:
			if (event.type == KEYDOWN) and (event.key == K_RIGHT):
				self.state_step = 'run'
				self.states[self.state_step].reset(True)
			elif (event.type == KEYDOWN) and (event.key == K_LEFT):
				self.state_step = 'run'
				self.states[self.state_step].reset(False)
			elif (event.type == KEYDOWN) and (event.key == K_UP):
				self.sounds['jump'].play()
				self.state_step = 'jump'
				self.states[self.state_step].reset(self.states['stand'].front)

	def _process_for_run(self, events, moving):
		for event in events:
			if self.states[self.state_step].front:
				if (event.type == KEYDOWN) and (event.key == K_LEFT):
					self.states[self.state_step].reset(False)
				elif (event.type == KEYUP) and (event.key == K_RIGHT):
					self.state_step = 'stand'
					self.states[self.state_step].reset(True)
				elif (event.type == KEYDOWN) and (event.key == K_UP):
					self.sounds['jump'].play()
					self.state_step = 'jump'
					self.states[self.state_step].reset(self.states['run'].front)
			elif not self.states[self.state_step].front:
				if (event.type == KEYDOWN) and (event.key == K_RIGHT) and (not self.states[self.state_step].front):
					self.states[self.state_step].reset(True)
				elif (event.type == KEYUP) and (event.key == K_LEFT):
					self.state_step = 'stand'
					self.states[self.state_step].reset(False)
				elif (event.type == KEYDOWN) and (event.key == K_UP):
					self.sounds['jump'].play()
					self.state_step = 'jump'
					self.states[self.state_step].reset(self.states['run'].front)

	def _process_for_jump(self, events, moving):
		if self.states[self.state_step].done:
			self.state_step = 'fall'
			self.states[self.state_step].reset(self.states['jump'].front)
			self._process_for_fall(events, moving)
		else:
			for event in events:
				if (event.type == KEYDOWN) and (event.key == K_RIGHT):
					self.states[self.state_step].front = True
				elif (event.type == KEYDOWN) and (event.key == K_LEFT):
					self.states[self.state_step].front = False

	def _process_for_fall(self, events, moving):
		for event in events:
			if (event.type == KEYDOWN) and (event.key == K_RIGHT):
				self.states[self.state_step].front = True
			elif (event.type == KEYDOWN) and (event.key == K_LEFT):
				self.states[self.state_step].front = False

	def evaluate_collisions(self):
		self.stuck = False

		for key, collision in self.collisions.items():
			if collision[0].collided and collision[0].other.type=='enemy':
				if collision[0].right_in or collision[0].left_in or collision[0].top_in:
					self.kill()
				elif collision[0].buttom_in:
					self.sounds['jump'].play()
					self.state_step = 'jump'
					self.states[self.state_step].reset(self.states['jump'].front)
					collision[0].other.kill()
			elif collision[0].collided and collision[0].other.type=='block':
				self._interact_with_bloc(collision, collision[0].other)
			elif collision[0].collided and collision[0].other.type=='level':
				self._interact_with_level(collision)
				

		if not len(self.collisions.items()) and self.start_falling and self.state_step == 'run':
			front = self.states[self.state_step].front
			self.state_step = 'fall'
			self.states[self.state_step].reset(front)
			self.start_falling = False
		elif not len(self.collisions.items()) and self.state_step == 'run':
			self.start_falling = True
		else:
			self.start_falling = False

		self.collisions = {}

	def _interact_with_bloc(self, collision, block):
		if collision[0].buttom_in and self.state_step == 'fall' and not collision[0].right_in and not collision[0].left_in:
			self.position[1] = collision[0].other.get_bounding_box().get_top() - self.get_bounding_box().height + 2
			front = self.states[self.state_step].front
			self.state_step = 'stand'
			self.states[self.state_step].reset(front)
		elif collision[0].buttom_in and not collision[0].right_in and not collision[0].left_in:
			self.position[1] = collision[0].other.get_bounding_box().get_top() - self.get_bounding_box().height + 2
		elif collision[0].right_in:
			self.position[0] =  collision[0].other.get_bounding_box().get_left() - self.get_bounding_box().width
			self.stuck = True
		elif collision[0].left_in:
			self.position[0] =  collision[0].other.get_bounding_box().get_right()
			self.stuck = True
		elif collision[0].top_in:
			block.hit()
			self.position[1] =  collision[0].other.get_bounding_box().get_buttom()
			front = self.states[self.state_step].front
			self.state_step = 'fall'
			self.states[self.state_step].reset(front)

	def _interact_with_level(self, collision):
		if collision[0].buttom_in and self.state_step == 'fall' and not collision[0].right_in and not collision[0].left_in:
			self.position[1] = collision[0].other.get_bounding_box().get_top() - self.get_bounding_box().height + 2
			front = self.states[self.state_step].front
			self.state_step = 'stand'
			self.states[self.state_step].reset(front)
		elif collision[0].buttom_in and not collision[0].right_in and not collision[0].left_in:
			self.position[1] = collision[0].other.get_bounding_box().get_top() - self.get_bounding_box().height + 2
		elif collision[0].right_in:
			self.position[0] =  collision[0].other.get_bounding_box().get_left() - self.get_bounding_box().width
			self.stuck = True
		elif collision[0].left_in:
			self.position[0] =  collision[0].other.get_bounding_box().get_right()
			self.stuck = True
		elif collision[0].top_in:
			self.position[1] =  collision[0].other.get_bounding_box().get_buttom()
			front = self.states[self.state_step].front
			self.state_step = 'fall'
			self.states[self.state_step].reset(front)

	def kill(self):
		self.dead = True

	def check_death_range(self):
		if self.position[1] > self.death_range[1][1]:
			self.kill()