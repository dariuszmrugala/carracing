import pgzrun
from random import randint

WIDTH=700
HEIGHT=800
ILEDOWYGRANIA = 400
CARSPEED = 3
ILEBECZEKNAEKRANIE = WIDTH/32

car=Actor("racecar")
car.pos=250,700
crashsound = tone.create('A4', 2)
winsound = tone.create('F5' , 0.5)

trackLeft = []
trackRight = []

SPEED = 4
trackCount = 0
trackPosition = 250
trackWidth = 120
trackDirection = False
gameStatus = 0


def draw():
    global gameStatus
    #ekran(128)
    screen.fill((0, 250, 0))
    if gameStatus == 0:
        car.draw()
        b = 0
        while b < len(trackLeft):
            trackLeft[b].draw()
            trackRight[b].draw()
            b += 1
    if gameStatus == 1:
        screen.blit('rflag', (318,268))

        #gameStatus = 0
       #tutaj
    if gameStatus == 2:
        screen.blit('cflag', (318,268))

def update():
    global gameStatus, trackCount, SPEED
    if gameStatus == 0:
        if keyboard.left and car.x > 0:  car.x -= CARSPEED
        if keyboard.right and car.x < WIDTH: car.x += CARSPEED

        updateTrack()
    if gameStatus == 1:
        if keyboard.space:
            resetGame()
            
    if gameStatus == 2:
        if keyboard.space:
            resetGame()

    if trackCount > ILEDOWYGRANIA: gameStatus = 2

    #print(trackCount)

def makeTrack():
    global trackCount, trackLeft, trackRight, trackPosition,trackWidth, ILEBECZEKNAEKRANIE
    trackLeft.append(Actor("barrier", pos=(trackPosition-trackWidth,0)))
    trackRight.append(Actor("barrier", pos=(trackPosition+trackWidth,0)))
    trackCount += 1
    #print('ile w kontenerze: ')
    #print(len(trackLeft))

    #print(trackCount)
    #print(ILEBECZEKNAEKRANIE)

    if trackCount > ILEBECZEKNAEKRANIE:
        #print('beczki poza ekranem')
        del trackLeft[0]
        del trackRight[0]


def updateTrack():
    global trackCount, trackPosition, trackDirection, trackWidth, gameStatus, SPEED, CARSPEED
    b = 0
    while b < len(trackLeft):
        if car.colliderect(trackLeft[b]) or car.colliderect(trackRight[b]):
            gameStatus = 1
            crashsound.play()
        trackLeft[b].y += SPEED
        trackRight[b].y += SPEED
        b += 1
    if trackCount == 100:
        SPEED += 0.1
        CARSPEED += 0.2
    if trackCount == 200:
        SPEED += 0.1
        CARSPEED += 0.2
    if trackCount == 300:
        SPEED += 0.1
        CARSPEED += 0.2


    if trackLeft[len(trackLeft)-1].y > 32:
        if trackDirection == False: trackPosition += 16
        if trackDirection == True: trackPosition -= 16
        if randint(0,4) == 1: trackDirection = not trackDirection
        if trackPosition > 700-trackWidth: trackDirection = True
        if trackPosition < trackWidth: trackDirection = False
        makeTrack()

def resetGame():
    global gameStatus, trackLeft, trackRight, trackCount, SPEED, CARSPEED, trackPosition, trackDirection
    gameStatus = 0
    trackLeft.clear()
    trackRight.clear()
    trackCount = 0
    SPEED = 4
    CARSPEED = 3
    car.pos=250,700
    trackPosition = 250
    trackDirection = False
    makeTrack()

makeTrack()