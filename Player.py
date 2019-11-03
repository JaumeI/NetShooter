import pygame


def juga(conn,cua,player, SCREENSIZE, rect):
    print ("Jugador "+str(player))
    speed = 10

    rect.x = 100*player + 30
    rect.y = 100*player + 30

    if rect.x > SCREENSIZE:
        rect.x = 0
        rect.y  = 0

    end = False
    shoot=False
    shootTimer=2000
    lastShotTime=pygame.time.get_ticks()

    while not end:
        shoot=False
        stringKey = (conn.recv(24)).decode()
        print (stringKey)
        KEY = int(stringKey)
        print("Player: " + str(player))

        if KEY==pygame.K_RIGHT and rect.x+rect.width+speed < SCREENSIZE:
            rect.x+=speed 
            print("Right")
        elif KEY==pygame.K_LEFT and rect.x-speed > 0 :
            rect.x-=speed
            print("Left") 
        elif KEY==pygame.K_UP and rect.y-speed > 0:
            rect.y-=10
            print("Up")
        elif KEY==pygame.K_DOWN and rect.y+rect.height+speed < SCREENSIZE:
            rect.y+=10
            print("Down")
        elif KEY==pygame.K_SPACE:
            now = pygame.time.get_ticks()
            timeSinceLastShot = now - lastShotTime
            if timeSinceLastShot >= shootTimer:
                shoot=True
                timeSinceLastShot = now
            print("Shoot")
        elif KEY==pygame.K_ESCAPE:
            end=True
            print("End")

        cua.put((player,rect, shoot))
        print("Player: " + str(player)+" " + str(rect)+" " + str(shoot))
    
    