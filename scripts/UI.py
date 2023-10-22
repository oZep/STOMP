import pygame
import math


class ImageUI:
    def __init__(self, img, pos, size):
        '''
        initializing the heart
        (image, position=[x,y], speed)
        '''
        self.img = img
        self.pos = pos
        self.size = size
        self.posy = pos[1]
        self.angle = 0
        self.count = 0.0
        self.countC = 10 # frequency
    
    def update(self):
        '''
        update fn, calculates new position on y axis
        '''
        self.count = (self.count + self.countC) % (2 * math.pi)
        bobbing_offset = math.sin(self.count) * self.speed
        self.pos[1] = self.posy + bobbing_offset

    def render(self, surf):
        '''
        renders img on screen
        '''
        surf.blit(self.img, self.pos)

    def rect(self):
        '''
        creates a rectangle at the entitiies current postion
        '''
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    

class TextUI:
    def __init__(self, text, pos=[0,0], fontsize=16, color=(0,0,0), float=0):
        '''
        initializing the level counter
        (current level, position=[x,y], color)
        '''
        self.text = text
        self.pos = pos
        self.fontsize = fontsize
        self.color = color
        self.float = float
        self.x_offset = 0


    def update(self, dt):
        # Initialize variables
        if self.float:
            amplitude = 40  # Amplitude of the sine wave
            frequency = 1  # Frequency of the sine wave
            self.x_offset += dt * 0.001
            self.y = amplitude * math.sin(frequency * self.x_offset)
        else:
            self.y = 0
    

    def render(self, surf):
        '''
        renders img on screen
        (surface, font size)
        '''
        current_level = pygame.font.SysFont('Return of Ganon', self.fontsize).render(f"{self.text}", False, self.color)
        surf.blit(current_level, (self.pos[0], self.pos[1] + self.y))

