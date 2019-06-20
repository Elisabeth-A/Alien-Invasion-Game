#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 08:47:16 2019

@author: Elisabeth
"""

import pygame

# Sprite groups elements together to act on them at once
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen=screen
        
        # Create a bullet rect at (0,0) and then set correct position.
        self.rect =pygame.Rect(0,0, ai_settings.bullet_width,
                               ai_settings.bullet_height)
        # set bullet to the center top of the ship
        self.rect.centerx=ship.rect.centerx
        self.rect.top= ship.rect.top
        
        # Store the bullet's position as a decimal value for fine adjustments.
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """Move the bullet up the screen."""
        # update the decimal position of the bullet.
        self.y -= self.speed_factor
        # update the rect position.
        self.rect.y =self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
