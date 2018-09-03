import pygame, sys
from pygame.locals import *
from config import parser
import state.gamestate
import state.level

def main():
	"""main function of the game"""

	#read config
	config = parser.get_game_state('./config/config.xml')

	#initiize pygame
	pygame.init()
	fps_clock = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((config.resolution[0], config.resolution[1]))
	pygame.display.set_caption('SUPER Marianito')

	#creae game state
	state1 = state.gamestate.GameState()

	#start game loop
	while True:
		#handle events
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

	pygame.display.update()
	fps_clock.tick(config.fps)

if __name__ == '__main__':
	main()