
import pygame
import random

# for the UI have 1 version in the beginning generated 3 times

# set the different cards in a list and randomize getting it on turnover action, remove the card from the list, reseting the list when the round is over


# pass button and spray button are different

# pass screen and spray screen, find a way to add up the score keeping track of rounds lost/won

        # [
        # [00][01][02][03] [XX] [card1]... [card3]
        # [10][11][12][13] [Spray] [card4]... [card6]
        # [20][21][22][23]   [Pass] [card7]... [card9]
        # ]

CARDS = [0,2,3,4,5,6,7,8,9] # where zero refs bigfoot
CARD_MAP = [
            [0,0],[0,1],[0,2], [0,3],   #[XX] [card1]... [card3]
            [1,0],[1,1],[1,2],[1,3],    #[Spray] [card4]... [card6]
            [2,0],[2,1],[2,2],[2,3],    #[Pass] [card7]... [card9]
           ]

class Cards:
    def __init__(self, game):
        self.game = game
        self.card_map = {}
        self.unselected = list(CARDS)
        
        # generate cards for games
        for i, n in range(len(CARDS)), CARD_MAP[0]:
            select = random.randint(0,len(self.unselected))
            self.card_map[n] = Card(CARDS[select], self.game)
            self.unselected.pop(select)
        

class Card:
    def __init__(self, value, game):
        self.game = game
        self.value = value
        self.flag = 0
        self.animation = self.game.assets['card_back'].copy()
        self.type = 'card'
    
    def turnOver(self):
        self.flag = 1

    def update(self):
        # if clicked which cards will edit and send info

        # show back of card
        if self.flag:
            self.animation = self.game.assets[self.type][self.value].copy() # get card asset and navigate to the value which is stored in the list


    
    def render(self, surf, offset={0,0}):
        '''
        renders card on the screen
        '''
        # show front of card on selected, if card value == 0, also send shocks 
        surf.blit(self.animation.img(), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))

