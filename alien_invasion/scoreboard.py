#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:40:16 2019

@author: Elisabeth
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """A class to report scoring information.""" 
    
    def __init__(self, ai_settings, screen, stats):
        """Initialise scorekeeping attributes."""
        self.screen =screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats
        
        # Font settings for scoring information
        self.text_color = (30,30,30)
        self.text_color_hs=(255,215,0)
        self.font =pygame.font.SysFont(None,40)
        
        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        # rounds score to the nearest 10,100,1000 etc. because of -1 arguement
        rounded_score =round(self.stats.score,-1)
        score_str= "{:,}".format(rounded_score)
        self.score_image=self.font.render('Score: ' + score_str,True, self.text_color, self.ai_settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top =20
    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        # rounds score to the nearest 10,100,1000 etc. because of -1 arguement
        high_score =str(self.stats.high_score)
        #high_score_str= "{:,}".format(high_score)
        self.high_score_image=self.font.render('* High Score: '+ high_score +' *',True, self.text_color_hs, self.ai_settings.bg_color)
        
        # Display the score at the top center of the screen.
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top =self.score_rect.top
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render('Level: '+str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top =self.score_rect.bottom +10
        # Position the level below the score
        
    def prep_ships(self):
        """ Show how many ships are left""" 
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_settings, self.screen)
            ship.rect.x= 10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
        
        
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # Draw ships
        self.ships.draw(self.screen)