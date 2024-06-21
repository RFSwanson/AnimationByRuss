import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

#scaled by 3 so new sub image is 72 pixels wide
frame_0 = sprite_sheet.get_image(0, 24, 24, 3, BLACK)
frame_1 = sprite_sheet.get_image(1, 24, 24, 3, BLACK)
frame_2 = sprite_sheet.get_image(2, 24, 24, 3, BLACK)
frame_3 = sprite_sheet.get_image(3, 24, 24, 3, BLACK)

run = True
while run:

	#update background
	screen.fill(BG)

	#show frame image
 #get_image gets the image but blit determines coordinate each image will be on screen
	screen.blit(frame_0, (0, 0))
	screen.blit(frame_1, (28, 0))
	screen.blit(frame_2, (56, 0))
	screen.blit(frame_3, (100, 0))

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()