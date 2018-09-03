from entities.baseentity import Entitiy

class SuperMarianito(Entitiy):
	"""docstring for ClassName"""

	def __init__(self):
		super().__init__()

		self.position[0] = 50
		self.position[1] = 180

	def move(self, addition):
		self.position[0] -= addition[0]
		self.position[1] += addition[1]
