import pygame

#button class
class Button():
	def __init__(self, pos: tuple, image, scale: float):
		self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		self.clicked = False

    

	def draw(self, screen):
		task = False
		pos = pygame.mouse.get_pos()
		screen.blit(self.image, (self.rect.x, self.rect.y))
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				task = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		
		


		return task

		