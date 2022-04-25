from cmath import rect
from turtle import Screen
import pygame
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
# Initialize pygame
pygame.init()

# Define constant for the screen width and height
SCREEN_WIDTH=800
SCREEN_HEIGHT=600

# Declare screen background
BLUE=76,0,153

# Declare length and width
LENGTH=50
WIDHT=50

# define a olayer object bt extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):
    def __init__(self) :
       super(Player,self).__init__()
       self.surf=pygame.Surface((75,75))
       self.surf.fill((255,255,255))
       self.rect=self.surf.get_rect()

# Create the screen object
# The size is determined by yhe constant  SCREEN_WIDTH SCREEN_HEIGHT
Screen=pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at very event in the queque
    for event in pygame.event.get():
        # did user hit a key ?
        if event.type==KEYDOWN:
            # was it the escape key ? if so, stop loop
            if event.key==K_ESCAPE:
                running=False
            print("Quit game")
             # Did user click the windows close button ? if so stop loop
        elif event.type==QUIT:
            running=False
            print("Quit game")

# Fill screen with white
Screen.fill((BLUE))

# Create a sufface and pass in a tuple containing its length and width
try:
    surf = pygame.Surface((LENGTH,WIDHT))
except:
    print("Typo maybe  surf = pygame.Surface((LENGTH,WIDHT)) ")

# Give the surface a color to separate it from the background
surf.fill((0,0,0))
rect=surf.get_rect()

# Draw surf onto the screen at the center

Screen.blit(surf,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
pygame.display.flip()


# put the center of surf at the center of the display
surf_center=(
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)

# Draw surf at teh new coordinates
Screen.blit(surf,surf_center)
pygame.display.flip()

