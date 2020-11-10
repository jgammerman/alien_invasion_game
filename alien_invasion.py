import sys

import pygame

class AlienInvasion:
	"""Overall class to manage game assets and behaviour."""

	def __init__(self):
		"""Initialize the game, and create game resources"""

		pygame.init()  # initializes the background settings that Pygame needs to work properly

		self.screen = pygame.display.set_mode((1200, 800))  # create a display window, on which we’ll draw all the game’s graphical elements. 1200 pixels wide by 800 pixels high
		pygame.display.set_caption("Alien Invasion")

		# Set the background colour
		self.bg_color = (230, 230, 230) # equal mixture of RGB - produces light grey colour


	def run_game(self):
		"""Start the main loop for the game."""
		while True:  
			# Watch for keyboard and mouse events
			for event in pygame.event.get():  # this function returns a list of events that have taken place since the last time it was called
				if event.type == pygame.QUIT:  # a pygame.QUIT event is detected if the player clicks the game window's close button
					sys.exit()

			# Redraw the screen during each pass through the loop.
			self.screen.fill(self.bg_color)	# Fill the screen with the background colour using the fill() method	

			# Make the most recently drawn screen visible. pygame.display.flip() continually updates the display to show the new positions 
			# of game elements and hides the old ones, creating the illusion of smooth movement.
			pygame.display.flip()


if __name__ == '__main__':  # Specifies that the file should be called directly, making the following lines run
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()