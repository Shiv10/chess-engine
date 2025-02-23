"""
This is our driver file. This will handle user input and display the current GameState
"""

import pygame as p
import ChessEngine
import os

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
initialize global dictionary of images. Load images only once at start of game and save in memory
'''
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(os.path.join("images", piece + ".png")), (SQ_SIZE, SQ_SIZE))


