#!/usr/bin/env python3

# Created by: Tomi, oyediran
# Created on: Jan. 10, 2023
# This program displays a playable space alien game on a  PyBadge
# makes sure that the sprite can only move 160 x( left or right), 128 y ( up or down )
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8 
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
FPS = 60
# makes sure that the sprite can only move ant one grid per input 
SPRITE_MOVEMENT_SPEED = 1

# for button state
button_state = { "button_up": "up",
 "button_just_pressed": "just pressed", 
 "button_still_pressed": "still_pressed", 
 "button_released": "released"

}
