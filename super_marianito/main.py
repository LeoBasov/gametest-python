import pygame, sys
from pygame.locals import *
from config import parser
import state.gamestate
import state.level
from entities.supermarianito import SuperMarianito
from entities.dry_bones import DryBones
from entities.questionblock import QuestionBlock
from entities.block import Block
from entities.level_tile import LevelTile

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

	game_state = state.gamestate.GameState()

	restart(game_state, config)

	#start game loop
	while True: 
		events = pygame.event.get()

		game_state.exec(events)
		game_state.print(DISPLAYSURF)

		pygame.display.update()
		fps_clock.tick(config.fps)

		if game_state.restart:
			restart(game_state, config)

def set_up_entities(game_state, config):
	set_up_sup(game_state, config)
	set_up_dry_bones(game_state, config)
	set_up_level(game_state, config)

def set_up_sup(game_state, config):
	sup = SuperMarianito()
	sup.load_sounds({'jump': './sound/smb_jump-small.wav'})
	game_state.add_entitiy(('sup',sup))

def set_up_dry_bones(game_state, config):
	dry_bones = DryBones()
	dry_bones.load_sounds({'die': './sound/smb_kick.wav'})
	game_state.add_entitiy(('dry_bones',dry_bones))

def set_up_questionblock(game_state, config, position, name):
	block = QuestionBlock()

	block.position[0] = position[0]
	block.position[1] = position[1]

	game_state.add_entitiy((name,block))

def set_up_level(game_state, config):
	tile1 = LevelTile((0,200),'./graphics/level1-1_block_1.png')
	tile2 = LevelTile((1136,200),'./graphics/level1-1_block_2.png')
	tile3 = LevelTile((1425,200),'./graphics/level1-1_block_3.png')
	tile4 = LevelTile((2480,200),'./graphics/level1-1_block_4.png')

	tube1 = LevelTile((448,168),'./graphics/tube_small.png')

	stairs11 = LevelTile((2144,184),'./graphics/solid_line_4.png')
	stairs12 = LevelTile((2160,168),'./graphics/solid_line_3.png')
	stairs13 = LevelTile((2176,152),'./graphics/solid_line_2.png')
	stairs14 = LevelTile((2192,136),'./graphics/solid_line_1.png')

	q_block1 = QuestionBlock((256,136))
	q_block2 = QuestionBlock((336,136))
	q_block3 = QuestionBlock((368,136))
	q_block4 = QuestionBlock((352,72))

	block1 = Block((320,136))
	block2 = Block((352,136))
	block3 = Block((384,136))

	game_state.add_entitiy(('tile1',tile1))
	game_state.add_entitiy(('tile2',tile2))
	game_state.add_entitiy(('tile3',tile3))
	game_state.add_entitiy(('tile4',tile4))

	game_state.add_entitiy(('tube1',tube1))

	game_state.add_entitiy(('stairs11',stairs11))
	game_state.add_entitiy(('stairs12',stairs12))
	game_state.add_entitiy(('stairs13',stairs13))
	game_state.add_entitiy(('stairs14',stairs14))

	game_state.add_entitiy(('q_block1',q_block1))
	game_state.add_entitiy(('q_block2',q_block2))
	game_state.add_entitiy(('q_block3',q_block3))
	game_state.add_entitiy(('q_block4',q_block4))

	game_state.add_entitiy(('block1',block1))
	game_state.add_entitiy(('block2',block2))
	game_state.add_entitiy(('block3',block3))

def restart(game_state, config):
	#creae game state
	game_state.restart_func()
	game_state.create_level('./graphics/level1-1.png')

	#entities
	set_up_entities(game_state, config)

	#music
	pygame.mixer.music.load('./sound/01-main-theme-overworld.mp3')
	pygame.mixer.music.play(-1, 0.0)


if __name__ == '__main__':
	main()