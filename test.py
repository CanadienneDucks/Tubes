import pygame

pygame.init()

###################################################################################
def startGame(win, xCordOne,yCordOne,xCordTwo,yCordTwo):
    pygame.draw.rect(win, (0,0,0), (0,0,500,500))
    pygame.draw.rect(win, (255,0,0), (xCordOne, yCordOne, 10, 10))
    pygame.draw.rect(win, (0,255,0), (xCordTwo, yCordTwo, 10, 10))
    #pygame.display.update()

###################################################################################
def main():
    screenWidth = 1000
    screenHeight = 1000

    win = pygame.display.set_mode((screenWidth,screenHeight)) #width and height
    pygame.display.set_caption("Python Solver")

    #top left = 0,0 
    #top right = 500,0
    #bottom right = 500,500
    #python = row,col
    xCordOne = 50
    yCordOne = 50 
    xCordTwo = 400
    yCordTwo = 400

    charWidth = 10
    charHeight = 10
    vel = 3

    leftOne = False
    rightOne = False
    upOne = False
    downOne = False 

    leftTwo = False
    rightTwo = False
    upTwo = False
    downTwo = False

    startGame(win, 50,50,400,400)

    inGame = True
    run = True
    while run:
        pygame.time.delay(20) #100 = 0.1 secons and 1000 = 1 second
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        
        keysOne = pygame.key.get_pressed()

        if keysOne[pygame.K_LEFT]:
            leftOne = True
            rightOne = False
            upOne = False
            downOne = False
        if keysOne[pygame.K_RIGHT]:
            leftOne = False
            rightOne = True
            upOne = False
            downOne = False
        if keysOne[pygame.K_UP]:
            leftOne = False
            rightOne = False
            upOne = True
            downOne = False
        if keysOne[pygame.K_DOWN]:
            leftOne = False
            rightOne = False
            upOne = False
            downOne = True

        keysTwo = pygame.key.get_pressed()

        if keysTwo[pygame.K_a]:
            leftTwo = True
            rightTwo = False
            upTwo = False
            downTwo = False
        if keysOne[pygame.K_d]:
            leftTwo = False
            rightTwo = True
            upTwo = False
            downTwo = False
        if keysOne[pygame.K_w]:
            leftTwo = False
            rightTwo = False
            upTwo = True
            downTwo = False
        if keysOne[pygame.K_s]:
            leftTwo = False
            rightTwo = False
            upTwo = False
            downTwo = True

        if bool(leftOne):
            xCordOne -= vel
            if xCordOne < 10: xCordOne = 980
        if bool(rightOne):
            xCordOne += vel
            if xCordOne > 980: xCordOne = 10
        if bool(upOne):
            yCordOne -= vel 
            if yCordOne < 10: yCordOne = 980
        if bool(downOne):
            yCordOne += vel
            if yCordOne > 980: yCordOne = 10

        if bool(leftTwo):
            xCordTwo -= vel
            if xCordTwo < 10: xCordTwo = 980
        if bool(rightTwo):
            xCordTwo += vel
            if xCordTwo > 980: xCordTwo = 10
        if bool(upTwo):
            yCordTwo -= vel 
            if yCordTwo < 10: yCordTwo = 980
        if bool(downTwo):
            yCordTwo += vel
            if yCordTwo > 980: yCordTwo = 10

       
        if win.get_at((xCordOne+11,yCordOne+11)) == (0, 255, 0):
            pygame.draw.rect(win, (0,255,0), (0, 0, 500, 500))
        else:
            pygame.draw.rect(win, (255,0,0), (xCordOne, yCordOne, charWidth, charHeight))

        if win.get_at((xCordTwo+11,yCordTwo+11)) == (255,0,0):
            pygame.draw.rect(win, (255,0,0), (0, 0, 500, 500))
        else:
            pygame.draw.rect(win, (0,255,0), (xCordTwo, yCordTwo, charWidth, charHeight))

        if keysOne[pygame.K_SPACE]:
            startGame(win,50,50,400,400)
            xCordOne = 50
            yCordOne = 50 
            xCordTwo = 400
            yCordTwo = 400
            leftOne = False
            rightOne = False
            upOne = False
            downOne = False
            leftTwo = False
            rightTwo = False
            upTwo = False
            downTwo = False
        pygame.display.update()

###################################################################################

main()

pygame.quit()

