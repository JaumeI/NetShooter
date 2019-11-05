import pygame, socket, threading


class Player(pygame.sprite.Sprite):
   

    def __init__(self, connexio, screensize, playerN):
        super().__init__()
        self.conn = connexio
        #self.cua = cua
        self.screensize = screensize
        self.playerN = playerN
        fileName = "ship"+str(playerN)+".png"
        self.image = pygame.image.load("images/"+fileName).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(screensize/30),int(screensize/15)))
        self.rect = self.image.get_rect()

        startX = int((screensize/8*self.playerN) + int(self.rect.width*self.playerN))
        startY = int((screensize/8*self.playerN) + int(self.rect.height*self.playerN))

        self.rect.x=startX
        self.rect.y=startY

        self.speed = 10
        self.isAlive = True

        #threading._start_new_thread(juga, (self,cua))
        self.thread = threading._start_new_thread(self.juga,())
    
    def juga(self):
        end = False
        self.shoot=False
        shootTimer=2000
        lastShotTime=pygame.time.get_ticks()

        while not end:
            self.shoot=False
            stringKey = (self.conn.recv(24)).decode()

            if len(stringKey)>0:
                KEY = int(stringKey)

                if KEY==pygame.K_RIGHT and self.rect.x+self.rect.width+self.speed < self.screensize:
                    self.rect.x+=self.speed
                elif KEY==pygame.K_LEFT and self.rect.x-self.speed > 0 :
                    self.rect.x-=self.speed
                elif KEY==pygame.K_UP and self.rect.y-self.speed > 0:
                    self.rect.y-=10
                elif KEY==pygame.K_DOWN and self.rect.y+self.rect.height+self.speed < self.screensize:
                    self.rect.y+=10
                elif KEY==pygame.K_SPACE:
                    now = pygame.time.get_ticks()
                    timeSinceLastShot = now - lastShotTime
                    if timeSinceLastShot >= shootTimer:
                        self.shoot=True
                        timeSinceLastShot = now
                elif KEY==pygame.K_ESCAPE:
                    end=True
                    self.isAlive = False
                    self.conn.close()

    