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

def drawBoard(screen):
    for i in range(8):
        for j in range(8):
            color = p.Color("light gray") if (i+j) % 2 == 0 else p.Color("#69923E")
            p.draw.rect(screen, color, p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece != "-":
                screen.blit(IMAGES[piece], p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

if __name__ == "__main__":
    main()