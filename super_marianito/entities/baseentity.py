"""This is the base class for entities in the game"""

class Entitiy:
	"""docstring for Entitiy"""

	def __init__(self):
		self.position = [0, 0]
		self.grapic  = []

	def process_events(self, events):
		pass

	def move(self, addition):
		pass

	def print(self, surface_surf):
		surface_surf.blit(self.graphic, (self.position[0], self.position[1]))