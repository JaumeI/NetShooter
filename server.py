
import socket, sys, threading, Player, queue, pygame, os, select
'''if not sys.argv[0]:
    TCP_IP = '127.0.0.1'
else:
    TCP_IP = sys.argv[0]'''
MAX_CLIENTS = 2

#Definir la finestra
pygame.init()

#Demanem la mida del monitor
mw = pygame.display.Info().current_w
mh = pygame.display.Info().current_h

if mw > mh:
    screensize = mh - int(mh/10)
else:
    screensize = mw - int(mw/10)

#posicio de la finestra
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (int((mw/2)-(screensize/2)),int((mh/2)-(screensize/2)))

# Creem una finestra de les mides indicades
DISPLAYSURF=pygame.display.set_mode((screensize,screensize))

# Posem el nom a la finestra
pygame.display.set_caption("NetShooter Server")

clock=pygame.time.Clock()

#Creem servidor
TCP_IP = '127.0.0.1'
TCP_IP = ''
TCP_PORT = 44223
print("Escoltant amb adreça " + TCP_IP + " al port " + str(TCP_PORT))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((TCP_IP, TCP_PORT))

#Engeguem servidor
server_socket.listen(5)


players = {}

ships = pygame.sprite.Group()

playerNumber = 0

while playerNumber < MAX_CLIENTS:
    client_socket, address = server_socket.accept()
    print ("Connexio de: ", address)
    players[playerNumber] = Player.Player(client_socket, screensize, playerNumber)
    playerNumber+=1

#Bucle de joc
while True:

    for event in pygame.event.get():
        #si és de tipus sortida, tanquem el joc
        if event.type == pygame.QUIT:
            server_socket.close()
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill((0,0,0))

    for x in range(MAX_CLIENTS):
        p = players[x]
        if p.isAlive:
            DISPLAYSURF.blit(p.image,(p.rect.x,p.rect.y))

    pygame.display.update()
    clock.tick(10)


