import pygame

pygame.init()

###################################################################################
class Character:
    def __init__(self, xCord, yCord, left, right, up, down):
        self.xCord = xCord
        self.yCord = yCord
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.width = 10
        self.height = 10
        self.vel = 5
        self.collisions = False

    def setX(self, xCord): self.xCord = xCord

    def setY(self, yCord): self.yCord = yCord

    def setLeft(self, left): self.left = left

    def setRight(self, right): self.right = right

    def setUp(self, up): self.up = up

    def setDown(self, down): self.down = down

    def getX(self): return self.xCord

    def getY(self): return self.yCord

    def getLeft(self): return self.left

    def getRight(self): return self.right

    def getWidth(self): return self.width

    def getHeight(self): return self.height

    def getVel(self): return self.vel

    def setDir(self, left, right, up, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def updateCords(self, screenWidth, screenHeight):
        if bool(self.left):
            self.xCord -= self.vel
            if self.xCord < 20: self.xCord = screenWidth - 20
        if bool(self.right):
            self.xCord += self.vel
            if self.xCord > screenWidth - 20: self.xCord = 20
        if bool(self.up):
            self.yCord -= self.vel 
            if self.yCord < 20: self.yCord = screenHeight - 20
        if bool(self.down):
            self.yCord += self.vel
            if self.yCord > screenHeight - 20: self.yCord = 20

    def checkCollision(self, win):
        if bool(self.left):
            if win.get_at((self.getX(), self.getY() + self.height/2)) == (0, 255, 0) or win.get_at((self.getX(), self.getY() + self.height/2)) == (255, 0, 0):
                self.collisions = True
                return True
        if bool(self.right):
            if win.get_at((self.getX() + self.width, self.getY() + self.height/2)) == (0, 255, 0) or win.get_at((self.getX() + self.width, self.getY() + self.height/2)) == (255, 0, 0):
                self.collisions = True
                return True
        if bool(self.up):
            if win.get_at((self.getX() + self.width/2, self.getY())) == (0, 255, 0) or win.get_at((self.getX() + self.width/2, self.getY())) == (255, 0, 0):
                self.collisions = True
                return True
        if bool(self.down):
            if win.get_at((self.getX() + self.width/2, self.getY() + self.height)) == (0, 255, 0) or win.get_at((self.getX() +self.width/2, self.getY() + self.height)) == (255, 0, 0):
                self.collisions = True
                return True
        
        return False

###################################################################################
'''def startGame(win, charOne, charTwo):
    pygame.draw.rect(win, (0,0,0), (0,0,500,500))
    pygame.draw.rect(win, (255, 0, 0), (charOne.getX(), charOne.getY(), charOne.getWidth(), charOne.getHeight())
    pygame.draw.rect(win, (255, 0, 0), (charTwo.getX(), charTwo.getY(), charTwo.getWidth(), charTwo.getHeight())
    #pygame.display.update()
'''

def test(self, win):
    if win.get_at((self.getX() + self.width/2, self.getY() + self.height/2)) == (0, 255, 0) or win.get_at((self.getX() + self.width/2, self.getY() + self.height/2)) == (255, 0, 0):
        return True
    '''
    if bool(self.left):
        if win.get_at((self.getX() + self.width/2, self.getY() + self.height/2)) == (0, 255, 0) or win.get_at((self.getX() + self.width/2, self.getY() + self.height/2)) == (255, 0, 0):
            return True
    if bool(self.right):
        if win.get_at((self.getX() + self.width/2, self.getY() + self.height/2)) == (0, 255, 0) or win.get_at((self.getX() + self.width/2, self.getY() + self.height/2)) == (255, 0, 0):
            return True
    if bool(self.up):
        if win.get_at((charOne.getX() + self.width/2,charOne.getY())) == (0, 255, 0) or win.get_at((charOne.getX() + self.width/2, charOne.getY() + self.height/2)) == (255, 0, 0):
            return True
    if bool(self.down):
        if win.get_at((charOne.getX() + self.width/2,charOne.getY() + self.height)) == (0, 255, 0) or win.get_at((charOne.getX() + self.width/2,charOne.getY() + self.heigth)) == (255, 0, 0):
            return True
    '''
    return False
   

###################################################################################
def main():
    screenWidth = 1000
    screenHeight = 700
    oneStartX = 50
    oneStartY = 50
    twoStartX = screenWidth - 50
    twoStartY = screenHeight - 50
    delayTime = 20 #this is in miliseconds = .02 seconds

    win = pygame.display.set_mode((screenWidth,screenHeight)) #width and height
    pygame.display.set_caption("Tubes")

    #top left = 0,0 
    #top right = 500,0
    #bottom right = 500,500
    #python = row,col
    charOne = Character(oneStartX, oneStartY, False, False, False, False)
    charTwo = Character(twoStartX, twoStartY, False, False, False, False)

    #startGame(win, charOne, charTwo)

    run = True
    gameOn = True
    while run:
        pygame.time.delay(delayTime) #100 = 0.1 secons and 1000 = 1 second
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        
        keys = pygame.key.get_pressed()
        if bool(gameOn):
            if keys[pygame.K_LEFT]:
                charOne.setDir(True, False, False, False)
            if keys[pygame.K_RIGHT]:
                charOne.setDir(False, True, False, False)
            if keys[pygame.K_UP]:
                charOne.setDir(False, False, True, False)
            if keys[pygame.K_DOWN]:
                charOne.setDir(False, False, False, True)
            if keys[pygame.K_a]:
                charTwo.setDir(True, False, False, False)
            if keys[pygame.K_d]:
                charTwo.setDir(False, True, False, False)
            if keys[pygame.K_w]:
                charTwo.setDir(False, False, True, False)
            if keys[pygame.K_s]:
                charTwo.setDir(False, False, False, True)

        charOne.updateCords(screenWidth, screenHeight)
        charTwo.updateCords(screenWidth, screenHeight)
        
        if bool(charOne.checkCollision(win) and gameOn):
            pygame.draw.rect(win, (0,255,0), (0, 0, screenWidth, screenHeight))
            gameOn = False
        elif bool(charTwo.checkCollision(win) and gameOn):
            pygame.draw.rect(win, (255,0,0), (0, 0, screenWidth, screenHeight))
            gameOn = False
        else:
            pygame.draw.rect(win, (0,255,0), (charTwo.getX(), charTwo.getY(), charTwo.getWidth(), charTwo.getHeight()))
            pygame.draw.rect(win, (255,0,0), (charOne.getX(), charOne.getY(), charOne.getWidth(), charOne.getHeight()))
        
        if not bool(gameOn):
            charOne.setDir(False, False, False, False)
            charTwo.setDir(False, False, False, False)

        if keys[pygame.K_SPACE]:
            pygame.draw.rect(win, (0,0,0), (0,0,screenWidth, screenHeight))
            pygame.draw.rect(win, (255, 0, 0), (oneStartX, oneStartY, charOne.getWidth(), charOne.getHeight()))
            pygame.draw.rect(win, (0, 255, 0), (twoStartX, twoStartY, charTwo.getWidth(), charTwo.getHeight()))
            gameOn = True
            charOne.setX(oneStartX)
            charOne.setY(oneStartY)
            

            charTwo.setX(twoStartX)
            charTwo.setY(twoStartY)
            
        #pygame.draw.rect(win, (255,0,0), (charOne.getX(), charOne.getY(), charOne.getWidth(), charOne.getHeight()))
        pygame.display.update()

###################################################################################

main()

pygame.quit()
