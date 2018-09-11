import pygame, sys
from pygame.locals import *
from config import parser
import state.gamestate
import state.level
from entities.supermarianito import SuperMarianito
from entities.dry_bones import DryBones
from entities.questionblock import QuestionBlock

def main():
	"""main function of the game"""

	#read config
	config = parser.get_game_state('./config/config.xml')

	#initiize pygame
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.init()
	fps_clock = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((config.resolution[0], config.resolution[1]))
	pygame.display.set_caption('SUPER Marianito')

	#creae game state
	game_state = state.gamestate.GameState()
	game_state.create_level('./graphics/SuperMarioBros-World1-Area1.png')

	#entities
	set_up_entities(game_state, config)

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

def set_up_entities(game_state, config):
	set_up_sup(game_state, config)
	set_up_dry_bones(game_state, config)
	set_up_questionblock(game_state, config)

def set_up_sup(game_state, config):
	sup = SuperMarianito()
	sup.load_sounds({'jump': './sound/smb_jump-small.wav'})
	game_state.add_entitiy(('sup',sup))

def set_up_dry_bones(game_state, config):
	dry_bones = DryBones()
	dry_bones.load_sounds({'die': './sound/smb_kick.wav'})
	game_state.add_entitiy(('dry_bones',dry_bones))

def set_up_questionblock(game_state, config):
	block = QuestionBlock()
	game_state.add_entitiy(('questionblock',block))

if __name__ == '__main__':
	main()