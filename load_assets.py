import pygame
pygame.init()
import os

def load(name):
    return pygame.image.load(os.path.join('Assets', name))
TITLE1 = load('title1.png')
TITLE2 = load('title2.png')
TITLE3 = load('title3.png')

BOARD1 = load('board1.png')
BOARD1 = pygame.transform.scale(BOARD1, (575, 575))
BOARD2 = load('board2.png')
BOARD2 = pygame.transform.scale(BOARD2, (575, 575))
BOARD3 = load('board3.png')
BOARD3 = pygame.transform.scale(BOARD3, (575, 575))
BOARD4 = load('board4.png')
BOARD4 = pygame.transform.scale(BOARD4, (575, 575))
BOARD5 = load('board5.png')
BOARD5 = pygame.transform.scale(BOARD5, (575, 575))

BOARD = (BOARD1, BOARD2, BOARD3, BOARD4, BOARD5)

DICE1 = load('dice1.png')
DICE1 = pygame.transform.scale(DICE1, (100, 100))
DICE2 = load('dice2.png')
DICE2 = pygame.transform.scale(DICE2, (100, 100))
DICE3 = load('dice3.png')
DICE3 = pygame.transform.scale(DICE3, (100, 100))
DICE4 = load('dice4.png')
DICE4 = pygame.transform.scale(DICE4, (100, 100))
DICE5 = load('dice5.png')
DICE5 = pygame.transform.scale(DICE5, (100, 100))
DICE6 = load('dice6.png')
DICE6 = pygame.transform.scale(DICE6, (100, 100))

DICE = (None, DICE1, DICE2, DICE3, DICE4, DICE5, DICE6)

DICE1DEG = load('dice1Degraded.png')
DICE1DEG = pygame.transform.scale(DICE1DEG, (100, 100))
DICE2DEG = load('dice2Degraded.png')
DICE2DEG = pygame.transform.scale(DICE2DEG, (100, 100))
DICE3DEG = load('dice3Degraded.png')
DICE3DEG = pygame.transform.scale(DICE3DEG, (100, 100))
DICE4DEG = load('dice4Degraded.png')
DICE4DEG = pygame.transform.scale(DICE4DEG, (100, 100))
DICE5DEG = load('dice5Degraded.png')
DICE5DEG = pygame.transform.scale(DICE5DEG, (100, 100))
DICE6DEG = load('dice6Degraded.png')
DICE6DEG = pygame.transform.scale(DICE6DEG, (100, 100))

DICEDEG = (None, DICE1DEG, DICE2DEG, DICE3DEG, DICE4DEG, DICE5DEG, DICE6DEG)

SNAKE1 = load('snake1.png')
SNAKE2 = load('snake2.png')
SNAKE3 = load('snake3.png')
SNAKE4 = load('snake4.png')

SNAKE1 = pygame.transform.scale(SNAKE1, (60, 50))
SNAKE2 = pygame.transform.scale(SNAKE2, (115, 120))
SNAKE3 = pygame.transform.scale(SNAKE3, (52, 320))
SNAKE4 = pygame.transform.scale(SNAKE4, (192, 257))

SNAKES = (SNAKE1, SNAKE2, SNAKE3, SNAKE4)

LADDER1 = load('ladder1.png')
LADDER2 = load('ladder2.png')
LADDER3 = load('ladder3.png')
LADDER4 = load('ladder4.png')

LADDER1 = pygame.transform.scale(LADDER1, (48, 230))
LADDER1 = pygame.transform.rotate(LADDER1, 225)
LADDER1 = pygame.transform.flip(LADDER1, True, False)
LADDER2 = pygame.transform.scale(LADDER2, (30, 108))
LADDER3 = pygame.transform.scale(LADDER3, (90, 96))
LADDER4 = pygame.transform.scale(LADDER4, (92, 274))

LADDERS = (LADDER1, LADDER2, LADDER3, LADDER4)

PIECERED = load('pieceRed.png')
PIECERED = pygame.transform.scale(PIECERED, (40, 40))
BIGGERPIECERED = pygame.transform.scale(PIECERED, (80, 80))
PIECEGREEN = load('pieceGreen.png')
PIECEGREEN = pygame.transform.scale(PIECEGREEN, (40, 40))
BIGGERPIECEGREEN = pygame.transform.scale(PIECEGREEN, (80, 80))
PIECEBLUE = load('pieceBlue.png')
PIECEBLUE  = pygame.transform.scale(PIECEBLUE, (40, 40))
BIGGERPIECEBLUE = pygame.transform.scale(PIECEBLUE, (80, 80))
PIECEYELLOW = load('pieceYellow.png')
PIECEYELLOW  = pygame.transform.scale(PIECEYELLOW, (40, 40))
BIGGERPIECEYELLOW = pygame.transform.scale(PIECEYELLOW, (80, 80))

PIECES = {"Red": PIECERED, "Green": PIECEGREEN, "Blue": PIECEBLUE, "Yellow": PIECEYELLOW}
BIGGERPIECES = {"Red": BIGGERPIECERED, "Green": BIGGERPIECEGREEN, "Blue": BIGGERPIECEBLUE, "Yellow": BIGGERPIECEYELLOW}

PIECEBLUEDEG = load('pieceBlueDegraded.png')
PIECEBLUEDEG = pygame.transform.scale(PIECEBLUEDEG, (40, 40))
BIGGERPIECEBLUEDEG = pygame.transform.scale(PIECEBLUEDEG, (80, 80))
PIECEGREENDEG = load('pieceGreenDegraded.png')
PIECEGREENDEG = pygame.transform.scale(PIECEGREENDEG, (40, 40))
BIGGERPIECEGREENDEG = pygame.transform.scale(PIECEGREENDEG, (80, 80))
PIECEREDDEG = load('pieceRedDegraded.png')
PIECEREDDEG = pygame.transform.scale(PIECEREDDEG, (40, 40))
BIGGERPIECEREDDEG = pygame.transform.scale(PIECEREDDEG, (80, 80))
PIECEYELLOWDEG = load('pieceYellowDegraded.png')
PIECEYELLOWDEG = pygame.transform.scale(PIECEYELLOWDEG, (40, 40))
BIGGERPIECEYELLOWDEG = pygame.transform.scale(PIECEYELLOWDEG, (80, 80))

PIECESDEG = {"Red": PIECEREDDEG, "Green": PIECEGREENDEG, "Blue": PIECEBLUEDEG, "Yellow": PIECEYELLOWDEG}
BIGGERPIECESDEG = {"Red": BIGGERPIECEREDDEG, "Green": BIGGERPIECEGREENDEG, "Blue": BIGGERPIECEBLUEDEG, "Yellow": BIGGERPIECEYELLOWDEG}

NUCLEARBOMB = load('nuclearBomb.png')
NUCLEARBOMB = pygame.transform.scale(NUCLEARBOMB, (37, 38))
NUCLEARICON = load('nuclearIcon.png')
NUCLEARICON = pygame.transform.scale(NUCLEARICON, (70, 70))
NUCLEARICONTRANSPARENT = load('nuclearIconTransparent.png')
NUCLEARICONTRANSPARENT = pygame.transform.scale(NUCLEARICONTRANSPARENT, (70, 70))

EXPLOSION_IMAGES = []
for num in range(1, 13):
    img = pygame.image.load(os.path.join('Assets', 'Explosion', f"{num}.png"))
    img = pygame.transform.scale(img, (950, 950))
    EXPLOSION_IMAGES.append(img)

UNMUTED = load('unmuted.png')
UNMUTED = pygame.transform.scale(UNMUTED, (70, 70))
MUTED = load('muted.png')
MUTED = pygame.transform.scale(MUTED, (70, 70))

papers_please = os.path.join('Assets', 'Audio', 'papers_please.mp3')
but_nobody_came = os.path.join('Assets', 'Audio', 'but_nobody_came.mp3')
genocide = os.path.join('Assets', 'Audio', 'genocide.mp3')

nuke_get_sounds = []
for num in range(1, 6):
    sound = pygame.mixer.Sound(os.path.join('Assets', 'Audio', f"nuke_get_{num}.mp3"))
    sound.set_volume(0.15)
    nuke_get_sounds.append(sound)

click = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'click.mp3'))
dice = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'dice.mp3'))
explosion = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'explosion.mp3'))
explosion.set_volume(0.1)
nukewin = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'nukewin.mp3'))
nukewin.set_volume(1)
pacifistwin = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'pacifistwin.mp3'))
pacifistwin.set_volume(0.1)
snake = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'snake.mp3'))
snake.set_volume(0.2)
ladder = pygame.mixer.Sound(os.path.join('Assets', 'Audio', 'ladder.mp3'))
ladder.set_volume(0.2)


