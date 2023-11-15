import pygame

class Mario:
  def __init__(self, pnum=1):
    """
    Initialize the Mario object
    args: pnum [int] Mario's id number
    """
    self.player_num = pnum
    self.lives = 3 # players always start with 3 lives
    self.is_large = False # player always starts small
    self.image = pygame.image.load ("mario.jpg")
    self.image = pygame.image.load(img)

#others
class Goomba:
  def __init__(self, pnum=2):
    """
    Initialize the gumba objects
    args: pnum [int] the number of goombas present onscreen
    """
    self.goomba_num = pnum
    self.attacks = 1 # number of attacks goomba's launch on player
    self.is_hostile = True # goomba's are always hostile to player characters
    self.image = pygame.image.load ("goomba.jpg")
def flatten(self):
    if self.type == "turtle":
        self.image = pygame.image.load("goomba_flattened.jpg")
        self.image = pygame.image.load(img)
    elif self.type == "Goomba":
        pass

class question_block:
  def __init__(self, pnum=1):
   """
    Initialize the question_block objects
    args: pnum [int] the number of question_blocks present onscreen
    """
   self.question_block_num = pnum
   self.interactions = 1 # number of times the player can interact w/ the box for a reward
   self.is_vertical = True # Question_blocks move vertically onscreen only
   self.image = pygame.image.load ("question_block.jpg")
   self.image = pygame.image.load(img)
