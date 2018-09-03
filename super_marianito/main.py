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
	game_state = state.gamestate.GameState()
	game_state.create_level('./graphics/SuperMarioBros-World1-Area1.png')

	#start game loop
	while True: 
		events = pygame.event.get()

		game_state.exec(events)
		game_state.print(DISPLAYSURF)

		pygame.display.update()
		fps_clock.tick(config.fps)

if __name__ == '__main__':
	main()