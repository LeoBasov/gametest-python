"""reader module"""

from xml.etree import ElementTree

class Config:
	
	def __init__(self):
		self.resolution = [400, 400]
		self.fps = 30

def get_game_state(file_name):
	config = Config()

	tree = ElementTree.parse(file_name)
	root = tree.getroot()

	resolution = root.find("resolution")
	fps = root.find("fps")

	config.resolution[0] = int(resolution.get('x'))
	config.resolution[1] = int(resolution.get('y'))

	config.fps = int(fps.get('value'))

	return config