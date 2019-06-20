#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:29:32 2019

@author: Elisabeth
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initialise the alien and set its starting position"""
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        
        # Load the alien image and set its rect attribute
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        
        # Start each new alien near the top left of the screen adding a space to the left and top equal to its size.
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        # store the alien's position.
        self.x =float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True
        
    def update(self):
        """Move alien right or left (fleet_direction 1 or -1)."""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x=self.x
        
        