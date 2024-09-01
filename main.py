#import pygame
import pygame

import sys

#import scr size, objects attrbts from constants.py
from constants import *

#import player class
from player import Player

#import asteroid class, asteroidfield
from asteroid import *
from asteroidfield import *
from shot import *

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
	

		# define groups that contain objects
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

		# static group container for class
	AsteroidField.containers = (updatable,)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	Shot.containers = (updatable, drawable, shots)
	
		# instantialize objects
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
	asteroidfield = AsteroidField()

		# assign groups to objects
	player.containers = (updatable, drawable)
	print(f"player in dr: {player in drawable} , player in ud: {player in updatable}")
			## alternatively: groupname.add(player)
	
	


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
		for asteroid in asteroids:
			if asteroid.is_collide(player):
				sys.exit("GAME OVER")
			for shot in shots:
				for asteroid in asteroids:
					if shot.is_collide(asteroid):
						shot.kill()
						asteroid.split()

if __name__ == "__main__":
	main()
