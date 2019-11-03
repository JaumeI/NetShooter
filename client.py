import socket, sys, pygame
####Configuració del client
if not sys.argv[0]:
    TCP_IP = "127.0.0.1"
else:
    TCP_IP = sys.argv[0]
TCP_IP = "127.0.0.1"
TCP_PORT = 44223

DISPLAYSURF=pygame.display.set_mode((200,200))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.close()
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            s.send(str(event.key).encode())
            if event.key == pygame.K_ESCAPE:
                end = True
                s.close()


#Rebem dades
#data = s.recv(BUFFER_SIZE)


####Tancar connexions de xarxa


