#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:38:09 2019

@author: Elisabeth
"""

class GameStats():
    """Track statistics for Alien Invasion""" 

    def __init__(self, ai_settings):
        """Initialise statistics."""
        self.ai_settings=ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active=False
        
        # store high score never to be reset
        self.high_score=0
        
    def reset_stats(self):
        """Initialise statistics that can change during the game.""" 
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
        