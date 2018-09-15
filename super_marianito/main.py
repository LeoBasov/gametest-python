import pygame, sys
from pygame.locals import *
from config import parser
import state.gamestate
import state.level
from entities.supermarianito import SuperMarianito
from entities.dry_bones import DryBones
from entities.gumba import Gumba
from entities.questionblock import QuestionBlock
from entities.block import Block
from entities.level_tile import LevelTile
from entities.shroom import Shroom

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
	set_upt_enemies(game_state)
	set_up_level(game_state, config)
	set_up_goodies(game_state)

def set_up_sup(game_state, config):
	sup = SuperMarianito()
	sup.load_sounds({'jump': './sound/smb_jump-small.wav'})
	game_state.add_entitiy(('sup',sup))

def set_up_dry_bones(game_state, config):
	dry_bones = DryBones()
	dry_bones.load_sounds({'die': './sound/smb_kick.wav'})
	game_state.add_entitiy(('dry_bones',dry_bones))

def set_up_questionblock(game_state, position, name):
	block = QuestionBlock(position)

	game_state.add_entitiy((name,block))

def set_up_block(game_state, position, name):
	block = Block(position)

	game_state.add_entitiy((name,block))

def set_up_level_tile(game_state, position, file_name, name):
	tile = LevelTile(position, file_name)

	game_state.add_entitiy((name,tile))

def set_up_level(game_state, config):
	set_up_level_tile(game_state, (0,200)   , './graphics/level1-1_block_1.png', 'tile1')
	set_up_level_tile(game_state, (1136,200), './graphics/level1-1_block_2.png', 'tile2')
	set_up_level_tile(game_state, (1425,200), './graphics/level1-1_block_3.png', 'tile3')
	set_up_level_tile(game_state, (2480,200), './graphics/level1-1_block_4.png', 'tile4')

	set_up_level_tile(game_state, (448,168), './graphics/tube_small.png' , 'tube1')
	set_up_level_tile(game_state, (608,152), './graphics/tube_medium.png', 'tube2')
	set_up_level_tile(game_state, (736,136), './graphics/tube_tall.png'  , 'tube3')
	set_up_level_tile(game_state, (912,136), './graphics/tube_tall.png'  , 'tube4')

	set_up_level_tile(game_state, (2144,184),'./graphics/solid_line_4.png' , 'stairs11')
	set_up_level_tile(game_state, (2160,168),'./graphics/solid_line_3.png' , 'stairs12')
	set_up_level_tile(game_state, (2176,152),'./graphics/solid_line_2.png' , 'stairs13')
	set_up_level_tile(game_state, (2192,136),'./graphics/solid_line_1.png' , 'stairs14')

	set_up_questionblock(game_state, (336,136), 'q_block1')
	set_up_questionblock(game_state, (256,136), 'q_block2')
	set_up_questionblock(game_state, (368,136), 'q_block3')
	set_up_questionblock(game_state, (352,72),  'q_block4')
	set_up_questionblock(game_state, (1024,120),'q_block5')

	set_up_block(game_state, (320,136), 'block1')
	set_up_block(game_state, (352,136), 'block2')
	set_up_block(game_state, (384,136), 'block3')

def set_upt_enemies(game_state):
	gumba1 = Gumba((600,184))

	game_state.add_entitiy(('gumba1',gumba1))

def set_up_goodies(game_state):
	set_up_shroom(game_state, (336,120), 'shroom1')

def set_up_shroom(game_state, position, name):
	shroom = Shroom(position)

	game_state.add_entitiy((name,shroom))

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