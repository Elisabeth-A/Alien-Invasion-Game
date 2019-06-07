#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:08:24 2019

@author: Elisabeth
"""
# generating a class containing all setting for the Alien Invasion game


class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        
        # Ship settings
        self.ship_limit=3
        
        # Bullet settings
        self.bullet_width=4
        self.bullet_height =15
        self.bullet_color= 60,60,60
        # restrict number of bullets fired at a time 
        self.bullets_allowed=3
        
        # Alien Settings
        self.fleet_drop_speed=13
        
        # How quickly the game speeds up
        self.speedup_scale =1.3
        
        # How much the alien point values increase over levels
        self.score_scale =1.5

        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """Initialise settings that change throughout the game.""" 
        self.ship_speed_factor =3.5
        self.bullet_speed_factor = 4
        self.alien_speed_factor=2
        
        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction=1
        
        # Scoring
        self.alien_points=50
        
    def increase_speed(self):
        """Increasing the speed and alien point values when progressing to the next level."""
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale
        
        # increasing the score by whole intergers
        self.alien_points = int(self.alien_points * self.score_scale)
        