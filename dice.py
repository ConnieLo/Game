import networkx as nx
import random
import pygame
class Dice:

    def __init__(self):
        self.face = ['diceFace1.png','diceFace2.png','diceFace3.png','diceFace4.png','diceFace5.png','diceFace6.png'] #array to hold images for dice faces
        self.d1X = 1078
        self.d1Y = 539
        self.d2X = 1139
        self.d2Y = 539
        self.dimens = 51
        self.d1Val = 1
        self.d2Val = 1

    def num(self):
        return random.randint(1,6), random.randint(1,6) #randomises 2 dice rolls

    def roll(self):
        nums = self.num() #generates the result of a dice roll
        self.display(nums)
        self.d1Val = nums[0]
        self.d2Val = nums[1]
        return(nums)

    def display(self, nums = None):   #generate dice roll
        if nums == None:
            nums = [self.d1Val, self.d2Val]
        d1 = pygame.image.load(self.face[nums[0]-1]).convert()  #load dice 1
        d2 = pygame.image.load(self.face[nums[1]-1]).convert()  #load dice 2
        screen.blit(d1, (self.d1X, self.d1Y))   #'draw' dice 1
        screen.blit(d2, (self.d2X, self.d2Y))   #'draw' dice 2


# Initialize Pygame
pygame.init()

# Set the width and height of the screen (width, height).
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Set title of the window
pygame.display.set_caption("Catan Game")

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 153, 213)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(BLUE)

# Defining user events
DICE_EVENT = pygame.USEREVENT + 1 #this event will be active while dice is rolling

# Loop until the user clicks the close button.
done = False

pygame.display.update()

#define dice
dice = Dice()
diceRolling = False #boolean for event loop

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONUP:
            mouseX, mouseY = pygame.mouse.get_pos()
            if (dice.d1X <= mouseX <= dice.d2X+dice.dimens) and (dice.d1Y <= mouseY <= dice.d1Y+dice.dimens):
                if diceRolling == False:
                    pygame.time.set_timer(DICE_EVENT, 100)
                    diceRolling = True #so you can't retrigger dice roll when its already rolling
                    dRollCount = 0 #counting for animation of dice roll

        elif event.type == DICE_EVENT:
            if dRollCount == 10: #num of seconds for animation x10
                dRoll = dice.roll() #gets value of roll
                pygame.time.set_timer(DICE_EVENT, 0)
                diceRolling = False
                
            else:
                dice.display(dice.num()) #temp display of dice while rolling
                dRollCount += 1

    #display static dice when not rolling
    if diceRolling == False:
        dice.display()


    # Limit to 60 frames per second
    clock.tick(60)

    # Update the screen with what we've drawn.
    pygame.display.flip()

# Close the window and quit.
pygame.quit()



