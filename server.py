
import socket, sys, threading, Player, queue, pygame, os
'''if not sys.argv[0]:
    TCP_IP = '127.0.0.1'
else:
    TCP_IP = sys.argv[0]'''
#Definir la finestra
pygame.init()

#Demanem la mida del monitor
mw = pygame.display.Info().current_w
mh = pygame.display.Info().current_h

if mw > mh:
    windowSize = mh - int(mh/10)
else:
    windowSize = mw - int(mw/10)

#posicio de la finestra
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (int((mw/2)-(windowSize/2)),int((mh/2)-(windowSize/2)))
# Definim la mida de la finestra

SCREENSIZE = windowSize
BASICUNIT = int(SCREENSIZE/20)

# Creem una finestra de les mides indicades
DISPLAYSURF=pygame.display.set_mode((SCREENSIZE,SCREENSIZE))

# Posem el nom a la finestra
pygame.display.set_caption("NetShooter")

chip = pygame.sprite.Sprite()
chip.image = pygame.image.load("images/ship.png").convert_alpha()
chip.image = pygame.transform.scale(chip.image, (int(windowSize/20),int(windowSize/20)))
chip.rect = chip.image.get_rect()
rect = pygame.Rect(0, 0, (int(windowSize/20)), (int(windowSize/20)))

clock=pygame.time.Clock()

#Engeguem servidor
TCP_IP = '127.0.0.1'
TCP_PORT = 44223
BUFFER_SIZE=1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
cua = queue.Queue()

totalPlayers = 0
while totalPlayers <2:
    conn, addr = s.accept()
    t = threading._start_new_thread(Player.juga, (conn,cua,totalPlayers, SCREENSIZE, pygame.Rect(0, 0, (int(windowSize/20)), (int(windowSize/20)))))
    totalPlayers+=1

ships = []
for x in range(totalPlayers):
    ship = pygame.sprite.Sprite()
    ship.image = pygame.image.load("images/ship.png").convert_alpha()
    ship.image = pygame.transform.scale(ship.image, (int(windowSize/20),int(windowSize/20)))
    ship.rect = ship.image.get_rect()
    ships.append(ship)



#Bucle de joc
while True:
    for event in pygame.event.get():
        #si és de tipus sortida, tanquem el joc
        if event.type == pygame.QUIT:
            conn.close()
            pygame.quit()
            sys.exit()
    
    while not cua.empty():
        s = cua.get()
        print("Main Server: " + str(s))
        player = s[0]
        coordinates = s[1]
        shoot = s[2]

        ships[player].rect = coordinates
        print("Main Server: "+str(player)+" " + str(coordinates)+" " + str(shoot))
    
    DISPLAYSURF.fill((0,0,0))

    for ship in ships:
        DISPLAYSURF.blit(ship.image,(ship.rect.x,ship.rect.y)) 


    pygame.display.update()
    clock.tick(10)

'''conn, addr = s.accept()
print ("Adreça de connexio:", addr)
data = None
while not data:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print ("He rebut: ", data.decode())
    #retorn
    conn.send(data)'''


