import sys
import os
import math
import random
import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.UI import TextUI, ImageUI
from scripts.card import Cards, Card

class Game:
    def __init__(self):
        '''
        initializes Game
        '''
        pygame.init()

        # change the window caption
        pygame.display.set_caption("S T O M P")
        # create window
        self.screen = pygame.display.set_mode((520,520))

        self.display = pygame.Surface((260, 260), pygame.SRCALPHA) # render on smaller resolution then scale it up to bigger screen

        self.display_2 = pygame.Surface((260, 260))

        self.clock = pygame.time.Clock()


        # keeping track of cards

        self.mouse = [0,0]

        self.score = 0 # for cards turned over add the amount

        # [
        # [00][01][02][03] [XX] [card1]... [card3]
        # [10][11][12][13] [Spray] [card4]... [card6]
        # [20][21][22][23]   [Pass] [card7]... [card9]
        # ]

        self.assets = {
            'card_back': load_image('card_back.png'),
            'cards': load_images('cards'),
            #'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'background': load_image('background.png')
        }

        self.background = []
        self.scene = 0

        # Chang this to switch between scenes
        # tracking level
        self.level = 0
        self.max_level = len(os.listdir('data/maps')) # max level
        # loading the level
        self.load_level(self.level)

        # screen shake
        self.screenshake = 0


    def load_level(self, map_id):
        self.cards = Cards(self)

        # creating 'camera' 
        self.scroll = [0, 0]

        self.dead = 0

        # transition for levels
        self.transition = -30

        # set the inital card to turnover
        self.first_card = 0

        self.turned_over = 0


    def run(self):
        '''
        runs the Game
        '''
        # creating an infinite game loop
        while True:
            self.display.fill((0, 0, 0, 0))    # outlines
            # clear the screen for new image generation in loop
            self.display_2.blit(self.assets[str(self.background[self.scene])], (0,0)) # no outline

            self.screenshake = max(0, self.screenshake-1) # resets screenshake value

            # move 'camera' to focus on player, make him the center of the screen
            # scroll = current scroll + (where we want the camera to be - what we have/can see currently) 
            self.scroll[0] += (- self.scroll[0])  / 30  # x axis
            self.scroll[1] += (- self.scroll[1]) / 30

            # fix the jitter
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))


            if not self.first_card:
                self.cards.card_map[[2,2]].turnOver()
                self.first_card = 1

            # turnover card if selected
            if self.selected:
                self.cards.card_map[self.mouse].turnOver()
                self.turned_over += 1


            # update cards & flags
            for card in self.cards.card_map.values():
                card.update()
                card.render()


            # ouline based on display
            display_mask = pygame.mask.from_surface(self.display)
            display_sillhouette = display_mask.to_surface(setcolor=(0, 0, 0, 180), unsetcolor=(0, 0, 0, 0)) # 180 opaque, 0 transparen
            self.display_2.blit(display_sillhouette, (0, 0))
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                self.display_2.blit(display_sillhouette, offset) # putting what we drew onframe back into display
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # have to code the window closing
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: # referencing right and left arrow keys
                        self.mouse[1] = min(self.mouse - 1, 0)
                    if event.key == pygame.K_RIGHT: 
                        self.mouse[1] = max(self.mouse + 1, 3)
                    if event.key == pygame.K_UP: # jump!, dont care about it's release as I dont want a constant jump on hold
                        self.mouse[0] = min(self.mouse - 1, 3)
                    if event.key == pygame.K_DOWN:
                        self.mouse[0] = min(self.mouse - 1, 3)
                    if event.key == pygame.K_x:
                        self.select = True
                if event.type == pygame.KEYUP: # when key is released
                    if event.key == pygame.K_x:
                        self.select = False

            # implementing transition
            if self.transition:
                transition_surf = pygame.Surface(self.display.get_size())
                pygame.draw.circle(transition_surf, (255, 255, 255), (self.display.get_width() // 2, self.display.get_height() // 2), (30 - abs(self.transition)) * 8) # display center of screen, 30 is the timer we chose, 30 * 8 = 180
                transition_surf.set_colorkey((255, 255, 255)) # making the circle transparent now
                self.display_2.blit(transition_surf, (0, 0))

            self.display_2.blit(self.display, (0, 0)) # cast display 2 on display

            screenshake_offset = (random.random() * self.screenshake - self.screenshake / 2, random.random() * self.screenshake - self.screenshake / 2)
            self.screen.blit(pygame.transform.scale(self.display_2, self.screen.get_size()), screenshake_offset) # render (now scaled) display image on big screen
            pygame.display.update()
            self.clock.tick(60) # run at 60 fps, like a sleep

# returns the game then runs it
Game().run()