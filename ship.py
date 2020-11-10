import pygame

class Ship:
	"""A class to manage the ship."""

	def __init__(self, ai_game):   # ai_game is a reference to the current instance of the AlienInvasion class
		"""Initialise the ship and set its starting position."""
		self.screen = ai_game.screen # assign the ai_game's screen to an attribute of Ship so we can access it easily in all the methods in this class
		self.screen_rect = ai_game.screen.get_rect()  # Access the screen's rect attribute using the get_rect() method - this lets us place the ship in the correct location on the screen

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp') # returns a surface representing the ship
		self.rect = self.image.get_rect() # now the image is loaded, call get_rect() to access the ship's rect attribute so we can later use it to place the ship

		# Start each new ship at the bottom centre of the screen
		self.rect.midbottom = self.screen_rect.midbottom


	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)  # draw the image to the screen at the position specified by self.rect