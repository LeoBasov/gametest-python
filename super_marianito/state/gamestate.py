"""game state module"""

import pygame, sys
from pygame.locals import *
from state.level import Level

class Move:

	def __init__(self):
		self.up = False
		self.down = False
		self.left = False
		self.right = False

	def _move(self):
		mov = [0, 0]

		if self.right:
			mov[0] -= 5

		if self.left:
			mov[0] += 5

		return mov

class GameState:
	"""docstring for Entitiy"""

	def __init__(self):
		self.entities = {}
		self.level = Level()
		self.mover = Move()
		self.position = [0, 0]

		self.draw_bounding_boxes = False
		self.draw_collision_points = False

	def create_level(self, file_name):
		self.level.graphic =  pygame.image.load(file_name)

	def exec(self, events):
		self._process_events(events)
		self._move()
		self._check_collisions(events)
		self._evaluate_collisions()
		self._delete_dead()

	def _process_events(self, events):
		for event in events:
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					self.mover.right = True
				elif event.key == K_LEFT:
					self.mover.left = True
				elif event.key == K_b:
					self.draw_bounding_boxes = (self.draw_bounding_boxes != True)
				elif event.key == K_c:
					self.draw_collision_points = (self.draw_collision_points != True)
			elif event.type == KEYUP:
				if event.key == K_RIGHT:
					self.mover.right = False
				elif event.key == K_LEFT:
					self.mover.left = False

		for key, ent in self.entities.items():
			ent.process_events(events)

	def _move(self):
		mov = self.mover._move()

		self.position[0] += mov[0]
		self.position[1] += mov[1]

		for key, ent in self.entities.items():
			ent.move(mov)

	def _check_collisions(self, events):
		for key, ent in self.entities.items():
			for key_inner, ent_inner in self.entities.items():
				if key_inner != key:
					ent.check_collision(ent_inner, key_inner)

	def _evaluate_collisions(self):
		for key, ent in self.entities.items():
			ent.evaluate_collisions()

	def add_entitiy(self,entity_key_pair):
		if entity_key_pair[0] in self.entities:
			raise Exception('Entitiy exists')
		else:
			self.entities[entity_key_pair[0]] = entity_key_pair[1]

	def remove_entitiy(self,entity_key):
		del self.entities[entity_key_pair[0]]

	def print(self, surface_surf):
		surface_surf.fill((0, 0, 0))

		self._print_level(surface_surf)

		for key, ent in self.entities.items():
			ent.print(surface_surf)

		if self.draw_bounding_boxes:
			for key, ent in self.entities.items():
				box = ent.get_bounding_box()

				pygame.draw.rect(surface_surf, (0, 0, 0), (box.get_left(), box.get_top(), box.get_right() - box.get_left(), box.get_buttom() - box.get_top()), 1)

		if self.draw_collision_points:
			for key, ent in self.entities.items():
				box = ent.get_bounding_box()

				for point in box.coll_points_left:
					pygame.draw.line(surface_surf, (255, 0, 0), (point[0], point[1]), (point[0], point[1]), 5)

				for point in box.coll_points_right:
					pygame.draw.line(surface_surf, (255, 0, 0), (point[0], point[1]), (point[0], point[1]), 5)

				for point in box.coll_points_top:
					pygame.draw.line(surface_surf, (255, 0, 0), (point[0], point[1]), (point[0], point[1]), 5)

				for point in box.coll_points_buttom:
					pygame.draw.line(surface_surf, (255, 0, 0), (point[0], point[1]), (point[0], point[1]), 5)

	def _print_level(self, surface_surf):
		surface_surf.blit(self.level.graphic, (self.position[0], self.position[1]))

	def _delete_dead(self):
		del_keys = []

		for key, ent in self.entities.items():
			if ent.dead:
				del_keys.append(key)

		for key in del_keys:
			del self.entities[key]