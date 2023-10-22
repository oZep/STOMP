
import pygame
import random

# for the UI have 1 version in the beginning generated 3 times

# set the different cards in a list and randomize getting it on turnover action, remove the card from the list, reseting the list when the round is over


# pass button and spray button are different

# pass screen and spray screen, find a way to add up the score keeping track of rounds lost/won

CARDS = [0,2,3,4,5,6,7,8,9] # where zero refs bigfoot

class Cards:
    def __init__(self, game):
        self.game = game
        self.card_map = []
        self.unselected = list(CARDS)
        
        # generate cards for games
        for i in len(CARDS):
            select = random.randint(0,len(self.unselected))
            self.card_map.append(Card(CARDS[select]))
            self.unselected.pop(select)

class Card:
    def __init__(self, value):
        self.value = value

    def update():
        pass
        # if clicked which cards will edit and send info
    
    def render(self, surf, offset={0,0}):
        '''
        renders entitiy asset
        '''
        # show back of card

        # show front of card on selected, if card value == 0, also send shocks 
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))

