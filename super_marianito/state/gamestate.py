"""game state module"""

from state.level import Level

class GameState:
	"""docstring for Entitiy"""

	def __init__(self):
		self.entities = {}
		self.level = Level()

	def exec(self, events):
		self._process_events(events)
		self._move()
		self._check_collisions(events)

	def _process_events(self, events):
		pass

	def _move(self):
		pass

	def _check_collisions(self, events):
		pass

	def add_entitiy(self,entity_key_pair):
		if entity_key_pair[0] in self.entities:
			raise Exception('Entitiy exists')
		else:
			self.entities[entity_key_pair[0]] = entity_key_pair[1]

	def remove_entitiy(self,entity_key):
		del self.entities[entity_key_pair[0]]