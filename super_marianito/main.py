import pygame, sys
from pygame.locals import *
from config import parser
import state.gamestate
import state.level
from entities.supermarianito import SuperMarianito
from entities.dry_bones import DryBones

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

	#entities
	set_up_entities(game_state)

	#music
	pygame.mixer.music.load('./sound/01-main-theme-overworld.mp3')
	pygame.mixer.music.play(-1, 0.0)

	#start game loop
	while True: 
		events = pygame.event.get()

		game_state.exec(events)
		game_state.print(DISPLAYSURF)

		pygame.display.update()
		fps_clock.tick(config.fps)

def set_up_entities(game_state):
	set_up_sup(game_state)
	set_up_dry_bones(game_state)

def set_up_sup(game_state):
	sup = SuperMarianito()

	sup.load_graphic({'walk': './graphics/sup_walk.png'})
	sup.load_graphic({'stand': './graphics/sup.png'})
	sup.load_graphic({'jump': './graphics/sup_jump.png'})

	game_state.add_entitiy(('sup',sup))

def set_up_dry_bones(game_state):
	dry_bones = DryBones()

	dry_bones.load_graphic({'walk_1': './graphics/drybones_w_1.png'})
	dry_bones.load_graphic({'walk_2': './graphics/drybones_w_2.png'})
	dry_bones.load_graphic({'walk_3': './graphics/drybones_w_3.png'})
	dry_bones.load_graphic({'walk_4': './graphics/drybones_w_4.png'})
	dry_bones.load_graphic({'walk_5': './graphics/drybones_w_5.png'})
	dry_bones.load_graphic({'walk_6': './graphics/drybones_w_6.png'})
	dry_bones.load_graphic({'walk_7': './graphics/drybones_w_7.png'})

	game_state.add_entitiy(('dry_bones',dry_bones))

if __name__ == '__main__':
	main()