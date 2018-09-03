"""reader module"""

from xml.etree import ElementTree

class Config:
	
	def __init__(self):
		self.resolution = [400, 400]
		self.fps = 30

def get_game_state():
	config = Config()

	tree = ElementTree.parse('config.xml')
	root = tree.getroot()

	resolution = root.find("resolution")
	fps = root.find("fps")

	config.resolution[0] = float(resolution.get('x'))
	config.resolution[1] = float(resolution.get('y'))

	config.fps = float(fps.get('value'))

	return config