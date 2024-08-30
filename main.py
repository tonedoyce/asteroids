#import pygame
import pygame

#import scr size, objects attrbts from constants.py
from constants import *

#import player class
from player import Player

def main():
	pygame.init
		#initialized pygame
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
		# messages to console
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		# setup screen object
	clock = pygame.time.Clock()
		# setup clock object
	dt = 0 				
		#time variable
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	updatable.add(player)
	drawable.add(player)
	while True:
		# frame delay
		dt = clock.tick(60) / 1000
		# game loop
		for event in pygame.event.get():
			# input check
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black", rect=None, special_flags=0)
		for u_object in updatable:
			u_object.update(dt)
			# movement on input
		for d_object in drawable:
			d_object.draw(screen)
		pygame.display.flip()
			# refresh screen

if __name__ == "__main__":
	main()
