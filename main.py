# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

#import scr size, asteroid attrbts from constants.py
from constants import *

def main():
	pygame.init
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 				#time variable
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		clock.tick(60)
		dt = clock.tick(60) / 1000

		screen.fill("black", rect=None, special_flags=0)
		pygame.display.flip()

if __name__ == "__main__":
	main()
