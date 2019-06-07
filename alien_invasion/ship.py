#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:36:18 2019

@author: Elisabeth
"""

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting position."""
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings = ai_settings
        
        # Load the ship image and get its rect.
        self.image=pygame.image.load('images/ship.bmp')
        # access screen rectangle
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Updating the ship's position based on the movement flag. If True ship moves"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # update rect object from self.center
        self.rect.centerx=self.center
        
    def center_ship(self):
        self.center =self.screen_rect.centerx
        
    def blitme(self):
        """Draw the ship at its current location specified by self.rect."""
        self.screen.blit(self.image,self.rect)
        