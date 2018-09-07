"""This is the base class for entities in the game"""

import pygame
from pygame.locals import *

class BoundingBox:

	def __init__(self, surface, position, collision_points = (), additions = ()):
		self.position = position
		self.centre = [surface.get_rect().centerx, surface.get_rect().centery]

		self.left_add   = 0
		self.right_add  = 0
		self.top_add    = 0
		self.buttom_add = 0

		self.coll_points_left   = []
		self.coll_points_right  = []
		self.coll_points_top    = []
		self.coll_points_buttom = []

		self._create_additions(surface, additions)

	def _create_collision_points(self, surface, collision_points):
		if not len(collision_points):
			number_of_points_per_side = 3

			self.coll_points_left   = self._create_collision_points_left(surface, number_of_points_per_side)
			self.coll_points_right  = self._create_collision_points_right(surface, number_of_points_per_side)
			self.coll_points_top    = self._create_collision_points_top(surface, number_of_points_per_side)
			self.coll_points_buttom = self._create_collision_points_buttom(surface, number_of_points_per_side)
		else:
			self.coll_points_left   = self._create_collision_points_left(surface, collision_points[0])
			self.coll_points_right  = self._create_collision_points_right(surface, collision_points[1])
			self.coll_points_top    = self._create_collision_points_top(surface, collision_points[2])
			self.coll_points_buttom = self._create_collision_points_buttom(surface, collision_points[3])

	def _create_collision_points_left(self, surface, number):
		return []

	def _create_collision_points_right(self, surface, number):
		return []

	def _create_collision_points_top(self, surface, number):
		return []

	def _create_collision_points_buttom(self, surface, number):
		return []

	def _create_additions(self, surface, additions):
		rect = surface.get_rect()

		if not len(additions):
			self.left_add = rect.width/2
			self.right_add = rect.width/2

			self.top_add = rect.height/2
			self.buttom_add = rect.height/2
		else:
			self.left_add = additions[0]
			self.right_add = additions[1]

			self.top_add = additions[2]
			self.buttom_add = additions[3]

	def get_left(self):
		return self.position[0] + self.centre[0] - self.left_add

	def get_right(self):
		return self.position[0] + self.centre[0] + self.right_add

	def get_top(self):
		return self.position[1] + self.centre[1] - self.top_add

	def get_buttom(self):
		return self.position[1] + self.centre[1] + self.buttom_add


class Collision:

	def __init__(self):
		self.collided = False
		self.position = [0, 0]
		self.left_in = False
		self.right_in = False
		self.top_in = False
		self.buttom_in = False

class Entitiy:
	"""docstring for Entitiy"""

	def __init__(self):
		self.position = [0, 0]
		self.animation_step = ''
		self.graphics  = {}
		self.bounding_boxes = {}
		self.sounds = {}
		self.dead = False
		self.collisions = {}
		self.death_range = [[0, 0],[0, 0]]

	def load_graphic(self, file_names):
		for key, file_name in file_names.items():
			self.graphics[key] =  pygame.image.load(file_name)
			self.bounding_boxes[key] = BoundingBox(self.graphics[key], self.position)

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

	def check_collision(self, other, key):
		collision = self._check_collision(other)

		if collision.collided:
			if not key in self.collisions:
				self.collisions[key] = [collision]
			else:
				self.collisions[key].append(collision)

	def _check_collision(self, other):
		collision = Collision()

		"""if ((self.position[0] + self.extension[0]) > other.position[0]) \
		and ((self.position[0] + self.extension[0]) < (other.position[0] + other.extension[0])):
			collision.right_in = True

		if ((self.position[0]) > other.position[0]) \
		and ((self.position[0]) < (other.position[0] + other.extension[0])):
			collision.left_in = True

		if ((self.position[1] + self.extension[1]) > other.position[1]) \
		and ((self.position[1] + self.extension[1]) < (other.position[1] + other.extension[1])):
			collision.buttom_in = True

		if ((self.position[1]) > other.position[1]) \
		and ((self.position[1]) < (other.position[1] + other.extension[1])):
			collision.top_in = True

		if (collision.right_in or collision.left_in) and (collision.buttom_in or collision.top_in):
			collision.collided = True"""

		return collision

	def evaluate_collisions(self):
		self.collisions = {}