#!/usr/bin/env python3


# Created by: Tomi, Oyediran
# Created on: Jan. 31, 2023
# This program displays a playable space alien game on a  PyBadge


import ugame
import stage


import constants


def game_scene():
    # main scene


    #image bank for the pybadge
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")


#set the background to image 0 in the image bank and the size (10x8 tiles of size 16)


    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)


    #sprite
    ship = stage.Sprite(image_bank_sprite, 5, 75, 66)


    #create a stage for the background to show on
    #and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = [ship]+[background]
    #render all sprites
    game.render_block()


    #repeat forever game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()


        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        #input to make the sprite move
        # if right button is pressed the sprites moves to the right + 1
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
        # catch to make sure that the sprite cannot go past its boundaries
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        # if right button is pressed the sprites moves to the left - 1
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
        # catch to make sure that the sprite cannot go past its boundaries
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass




        #update game logic


        # refreshes the sprite forever ( forever loop)


        game.render_sprites([ship])
        # refreshes the sprite every 1 60th of a second to maintain the 60 fps refresh rate


        game.tick()        


if __name__ == "__main__":
    game_scene()
