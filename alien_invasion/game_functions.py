#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:41:48 2019

@author: Elisabeth
"""

# storing alien invasion game functions

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen,ship,bullets):
    """Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit is not reached yet"""
        # Create a new bullet and add it to the bullet group
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet= Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
            
        

def check_keyup_events(event, ship):
    """Repond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen,stats,sb,play_button, ship,aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
            
        # If player closes display window, the game is terminated
        if event.type == pygame.QUIT:
            sys.exit()
            
        # pressing right arrow key moves ship to the right
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get position of mouse cursor
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings, screen,stats,sb, play_button,ship, aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen,stats,sb, play_button,ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks play."""
    # store true or false value for button clicked
    button_clicked=play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        # Reset Game statistics
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # Empty the list of alien and bullets,
        aliens.empty()
        bullets.empty()
        
        #Create a new fleet and center the ship
        create_fleet(ai_settings, screen,ship,aliens)
        ship.center_ship()
        
def update_screen(ai_settings, screen,stats,sb, ship,aliens, bullets, play_button):
    """Update images on screen and flip to a new screen"""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    #Redraw all bullets behind ship and aliens by looping through bullet group.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    # drawing each alien of the fleet on the screen
    aliens.draw(screen)
    
    # Draw the scoreboard
    sb.show_score()
    
    # Draw the play button when the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    
    # Make the most recently drawn screen visible -> updating display window
    pygame.display.flip()
    
def update_bullets(ai_settings, screen,stats, sb, ship, aliens,bullets):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet position
    bullets.update()
    # Get rid of bullets that have past the screen and disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collision(ai_settings, screen, stats,sb, ship,bullets, aliens)
            
def check_bullet_alien_collision(ai_settings, screen,stats, sb, ship,bullets, aliens):
    """Respond to bullet-alien collisions"""
     # Check if any bullets hits an alien
     # If so get rid of the bullet and the alien
    collisions=pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points* len(aliens)
        # create new image for the updated score
            sb.prep_score()
        check_high_score(stats,sb)
        
    if len(aliens)==0:
        # start a new level: destroy existing bullets, speed up game and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        # Increase level
        stats.level +=1
        sb.prep_level()
        create_fleet(ai_settings,screen, ship, aliens)
        

def create_alien(ai_settings, screen,aliens, alien_number,row_number):
      #Create an alien and place it in the row.
      alien=Alien(ai_settings,screen)
      alien_width=alien.rect.width
      alien.x=alien_width + 2*alien_width*alien_number
      alien.rect.x=alien.x
      alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
      aliens.add(alien)

def get_number_aliens_x(ai_settings, alien_width):
    """Determine number of alien that fit in a row"""
    # Spacing between each alien is equal to one alien width.
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine number of rows that fit on screen"""
    available_space_y=ai_settings.screen_height-ship_height-(3*alien_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_fleet(ai_settings, screen,ship, aliens):
    """Create a full fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x=get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height, alien.rect.height)
    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def check_fleet_edges(ai_settings, aliens):
    """Respons appropriately if alien hits edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
         change_fleet_direction(ai_settings, aliens)
         break
     
def change_fleet_direction(ai_settings, aliens):
    """Drop entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y +=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
            
            
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """updating position of alien on screen after checking if the fleet is at the edge"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats, screen,stats, sb,ship, aliens, bullets)
        
    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom (ai_settings, screen,stats, sb,ship, aliens, bullets)
    
        
def ship_hit(ai_settings, screen,stats,sb,ship, aliens, bullets):
    """Respond to ship being hit by an alien"""
    if stats.ships_left>0:
        # Decrement ships left
        stats.ships_left -=1
        # Update scoreboard
        sb.prep_ships()
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause before restarting
        sleep (0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom (ai_settings, screen,stats, sb,ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this the same as if ship got it
            ship_hit(ai_settings, screen,stats, sb, ship, aliens, bullets)
            break

def check_high_score(stats,sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
        

    
    
    
    
    