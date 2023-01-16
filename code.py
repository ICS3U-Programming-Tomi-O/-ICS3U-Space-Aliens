#!/usr/bin/env python3

# Created by: Tomi Oyediran
# Created on: Jan. 10, 2023
# This program displays a playable space alien game on a  PyBadge

import ugame
import stage


def game_scene():
    # this function is the main game_scene

    #image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # background being set to 0 in the image bank
    # and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # sprite that is updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # creating a stage for the background to show up on screen
    # frames set to 60 fps
    game = stage.Stage(ugame.display, 60)
    #setting the layers of all sprites, items show up in order 
    game.layers = [ship] + [background]
    #render all sprites
    # rendering only the background
    game.render_block()

    #repeat forever in game loop
    while True:
        #user input
      
             
        # update game logic
         
        # redraw sprite
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__" :
      game_scene()