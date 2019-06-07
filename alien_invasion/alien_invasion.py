#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alien Invasion Game

In this game the player controls a ship that appears at the bottom center of the screen. 
The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar.
When the game begins, a fleet of aliens fills the sky and moves across and down the screen.
The player shoots and destroys the aliens. If the player shoots all aliens, a new fleet appears
that moves faster than the previous one. If any alien hits the player's ship or reaches the
bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.


Created on Wed Jun  5 10:26:42 2019

@author: Elisabeth

using Pygame modules
"""

# creating a Pygame window 


import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    
    ai_settings=Settings()
    #create display window called screen
    screen=pygame.display.set_mode((
            ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make play button.
    play_button=Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard
    stats= GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen, stats)
    
    # Add ship
    ship=Ship(ai_settings,screen)
    
    # Make a group to store bullets
    bullets=Group()
    
    # Maka group of aliens
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    # Start the main loop for a game
    while True:
        #Respond to keypresses and mouse events.
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            # update position of game elements
            ship.update()
            gf.update_bullets(ai_settings, screen,stats, sb, ship, aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats, sb, ship,aliens,bullets)
        
        # update screen 
        gf.update_screen(ai_settings, screen,stats,sb, ship,aliens, bullets, play_button)
        
run_game()