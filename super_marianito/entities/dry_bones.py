import pygame
from pygame.locals import *
from entities.baseentity import Entitiy
import math

class DryBones(Entitiy):
	"""docstring for ClassName"""
	def __init__(self):
		super().__init__()

		self.position[0] = 200
		self.position[1] = 165

		self.animation_step = 'walk_1'
