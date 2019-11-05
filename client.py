import socket, sys, pygame

####Configuració del client
if not sys.argv[0]:
    TCP_IP = "127.0.0.1"
else:
    TCP_IP = sys.argv[0]
TCP_IP = "127.0.0.1"
TCP_PORT = 44223
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

DISPLAYSURF=pygame.display.set_mode((200,200))
pygame.display.set_caption("NetShooter Client")

end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client_socket.send(str(pygame.K_ESCAPE).encode())
            client_socket.close()
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            client_socket.send(str(event.key).encode())
            if event.key == pygame.K_ESCAPE:
                end = True
                client_socket.close()


