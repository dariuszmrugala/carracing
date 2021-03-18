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
trackWidth = 200 #poczatkawa wartosc 120
trackDirection = False
gameStatus = 0


def draw():
    global gameStatus

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

    if gameStatus == 2:
        screen.blit('cflag', (318,268))


def update():
    global gameStatus, trackCount, SPEED, CARSPEED, trackWidth
    
    if gameStatus == 0:
        if keyboard.left and car.x > 0:
            car.x -= CARSPEED
        if keyboard.right and car.x < WIDTH:
            car.x += CARSPEED
        if trackCount > ILEDOWYGRANIA:
            gameStatus = 2
        updateTrack()
        
    if gameStatus == 1:
        if keyboard.space:
            resetGame()
            gameStatus = 0

    if gameStatus == 2:
        if keyboard.space:
            resetGame()
            gameStatus = 0


def makeTrack():
    global trackCount, trackLeft, trackRight, trackPosition,trackWidth, ILEBECZEKNAEKRANIE
    
    trackLeft.append(Actor("barrier", pos=(trackPosition-trackWidth,0)))
    trackRight.append(Actor("barrier", pos=(trackPosition+trackWidth,0)))
    trackCount += 1
 
    if trackCount > ILEBECZEKNAEKRANIE:
        del trackLeft[0]
        del trackRight[0]
    

def updateTrack():
    global trackCount, trackPosition, trackDirection, trackWidth, gameStatus, SPEED, CARSPEED
    BarrelHeight = 32
    
    b = 0
    while b < len(trackLeft):
        if car.colliderect(trackLeft[b]) or car.colliderect(trackRight[b]):
            gameStatus = 1
            crashsound.play()
        trackLeft[b].y += SPEED
        trackRight[b].y += SPEED
        b += 1

    if trackLeft[len(trackLeft)-1].y > BarrelHeight:
        if trackDirection == False: trackPosition += 16
        if trackDirection == True: trackPosition -= 16
        if randint(0,4) == 1: trackDirection = not trackDirection
        if trackPosition > 700-trackWidth: trackDirection = True
        if trackPosition < trackWidth: trackDirection = False
        
        if trackCount == 100:
            SPEED += 1
            CARSPEED += 1.5
            trackWidth -= 50
        if trackCount == 200:
            SPEED += 1
            CARSPEED += 1.2
            trackWidth -= 20
        if trackCount == 300:
            SPEED += 1
            CARSPEED += 1
            trackWidth -= 20

        makeTrack()


def resetGame():
    global gameSatus, trackLeft, trackRight, trackCount, SPEED, CARSPEED, trackPosition, trackDirection, trackWidth
    
    gameStatus = 0
    trackLeft.clear()
    trackRight.clear()
    trackCount = 0
    SPEED = 4
    CARSPEED = 3
    car.pos=250,700
    trackPosition = 250
    trackDirection = False
    trackWidth = 200
    makeTrack()

makeTrack()
#pgzrun.go()