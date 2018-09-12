"""This is the base class for entities in the game"""

import pygame
from pygame.locals import *

class BoundingBox:

	def __init__(self, surface, position, collision_points = ()):
		self.position = position
		self.centre = [surface.get_rect().centerx, surface.get_rect().centery]

		self.width = surface.get_rect().width
		self.height = surface.get_rect().height

		self.coll_points_left   = []
		self.coll_points_right  = []
		self.coll_points_top    = []
		self.coll_points_buttom = []

		self.number_of_points_per_side = collision_points

		self._create_collision_points()

	def _create_collision_points(self):
		if not len(self.number_of_points_per_side):
			number_of_points_per_side_loc = 3

			self.coll_points_left   = self._create_collision_points_left(number_of_points_per_side_loc)
			self.coll_points_right  = self._create_collision_points_right(number_of_points_per_side_loc)
			self.coll_points_top    = self._create_collision_points_top(number_of_points_per_side_loc)
			self.coll_points_buttom = self._create_collision_points_buttom(number_of_points_per_side_loc)
		else:
			self.coll_points_left   = self._create_collision_points_left(self.number_of_points_per_side[0])
			self.coll_points_right  = self._create_collision_points_right(self.number_of_points_per_side[1])
			self.coll_points_top    = self._create_collision_points_top(self.number_of_points_per_side[2])
			self.coll_points_buttom = self._create_collision_points_buttom(self.number_of_points_per_side[3])

	def _create_collision_points_left(self, number):
		first = [self.get_left(), self.get_top()]
		last = [self.get_left(), self.get_buttom()]

		dist = (self.get_buttom() - self.get_top())/number

		points = [first]

		for i in range(number - 1):
			point = [self.get_left(), self.get_top() + (i + 1)*dist]
			points.append(point)

		points.append(last)

		return points

	def _create_collision_points_right(self, number):
		first = [self.get_right(), self.get_top()]
		last = [self.get_right(), self.get_buttom()]

		dist = (self.get_buttom() - self.get_top())/number

		points = [first]

		for i in range(number - 1):
			point = [self.get_right(), self.get_top() + (i + 1)*dist]
			points.append(point)

		points.append(last)

		return points

	def _create_collision_points_top(self, number):
		first = [self.get_left(), self.get_top()]
		last = [self.get_right(), self.get_top()]

		dist = (self.get_right() - self.get_left())/number

		points = [first]

		for i in range(number - 1):
			point = [self.get_left() + (i + 1)*dist, self.get_top()]
			points.append(point)

		points.append(last)

		return points

	def _create_collision_points_buttom(self, number):
		first = [self.get_left(), self.get_buttom()]
		last = [self.get_right(), self.get_buttom()]

		dist = (self.get_right() - self.get_left())/number

		points = [first]

		for i in range(number - 1):
			point = [self.get_left() + (i + 1)*dist, self.get_buttom()]
			points.append(point)

		points.append(last)

		return points

	def get_left(self):
		return self.position[0]

	def get_right(self):
		return self.position[0] + self.width

	def get_top(self):
		return self.position[1]

	def get_buttom(self):
		return self.position[1] + self.height

	def checK_if_inside_mult(self, points):
		inside = []

		for point in points:
			if self.checK_if_inside(point):
				inside.append(point)

		return inside

	def checK_if_inside(self, point):
		ret = False

		if (point[0] <= self.get_right()) and (point[0] >= self.get_left()) \
		and (point[1] >= self.get_top()) and (point[1] <= self.get_buttom()):
			ret = True

		return ret


class Collision:

	def __init__(self):
		self.collided = False
		self.position = [0, 0]
		self.left_in = False
		self.right_in = False
		self.top_in = False
		self.buttom_in = False

		self.other = 0

class Entitiy:
	"""docstring for Entitiy"""

	def __init__(self):
		self.position = [0, 0]
		self.state_step = ''
		self.states  = {}
		self.sounds = {}
		self.dead = False
		self.collisions = {}
		self.death_range = [[0, 0],[0, 0]]
		self.type = ''

	def load_sounds(self, file_names):
		for key, file_name in file_names.items():
			self.sounds[key] =  pygame.mixer.Sound(file_name)

	def process_events(self, events):
		pass

	def move(self, addition):
		self.states[self.state_step].exec(addition)

	def print(self, surface_surf):
		surface_surf.blit(self.states[self.state_step].graphic, (self.position[0], self.position[1]))

	def kill(self):
		pass

	def check_collision(self, other, key):
		collision = self._check_collision(other, key)

		if collision.collided:
			if not key in self.collisions:
				self.collisions[key] = [collision]
			else:
				self.collisions[key].append(collision)

	def _check_collision(self, other, key):
		collision = Collision()

		other_box = other.get_bounding_box()
		my_box = self.get_bounding_box()
		my_box._create_collision_points()

		coll_points_right  = other_box.checK_if_inside_mult(my_box.coll_points_right)
		coll_points_left   = other_box.checK_if_inside_mult(my_box.coll_points_left)
		coll_points_top    = other_box.checK_if_inside_mult(my_box.coll_points_top)
		coll_points_buttom = other_box.checK_if_inside_mult(my_box.coll_points_buttom)

		if len(coll_points_right) > 1:
			collision.right_in = True
			collision.collided = True
			collision.other = other

		if len(coll_points_left) > 1:
			collision.left_in = True
			collision.collided = True
			collision.other = other

		if len(coll_points_top) > 1:
			collision.top_in = True
			collision.collided = True
			collision.other = other

		if len(coll_points_buttom) > 1:
			collision.buttom_in = True
			collision.collided = True
			collision.other = other

		return collision

	def evaluate_collisions(self):
		self.collisions = {}

	def get_bounding_box(self):
		return self.states[self.state_step].bounding_box

class BaseState:
	def __init__(self, position):
		self.animation_iter = 0
		self.animation_iter_max = 1
		self.animation_index = 0

		self.animation_front = []
		self.animation_back = []
		self.front = True

		self.bounding_boxes_front = []
		self.bounding_boxes_back = []

		self.graphic = 0
		self.bounding_box = 0

		self.position = position

	def load_animation_step(self, file_name_front, file_name_back):
		self.animation_front.append(pygame.image.load(file_name_front))
		self.animation_back.append(pygame.image.load(file_name_back))

		self.bounding_boxes_front.append(BoundingBox(self.animation_front[-1], self.position))
		self.bounding_boxes_back.append(BoundingBox(self.animation_back[-1], self.position))

	def reset(self, front):
		self.animation_iter = 0
		self.animation_index = 0
		self.front = front

		if self.front:
			self.graphic = self.animation_front[self.animation_iter]
			self.bounding_box = self.bounding_boxes_front[self.animation_iter]
		else:
			self.graphic = self.animation_back[self.animation_iter]
			self.bounding_box = self.bounding_boxes_back[self.animation_iter]

	def exec(self, addition):
		self._move(addition)

		if self.front:
			self.graphic = self.animation_front[self.animation_iter]
			self.bounding_box = self.bounding_boxes_front[self.animation_iter]
			self._check_animation_iter(self.animation_front)
		else:
			self.graphic = self.animation_back[self.animation_iter]
			self.bounding_box = self.bounding_boxes_back[self.animation_iter]
			self._check_animation_iter(self.animation_back)

	def _check_animation_iter(self, animations):
		self.animation_index += 1

		if self.animation_index == self.animation_iter_max:
			self.animation_index = 0

			if self.animation_iter == (len(animations) - 1):
				self.animation_iter = 0
			else:
				self.animation_iter += 1

	def _move(self, addition):
		pass
