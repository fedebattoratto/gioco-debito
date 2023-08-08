import pygame 

from giocatori import Giocatori
#creo l'inizio del gioco
pygame.init()


schermo_widht=1000
schermo_height=800


finestra=pygame.display.set_mode((schermo_widht, schermo_height))
pygame.display.set_caption('gioco debito settembre')

clock=pygame.time.Clock()

FPS=60

#carico le immagine 
imm_image=pygame.image.load('immagini.jpg').convert_alpha()

#qui le disegno

def disegna():
    scala=pygame.transform.scale(imm_image, (schermo_widht, schermo_height))
    finestra.blit(scala, (0, 0))


def disegnavita(vita, x, y):
    pass

#creo i 2 giocati

giocatore1=Giocatori(200, 310)

giocatore2=Giocatori(700, 310)


#faccio subito il ciclo fondamentale usando il while

run=True

while run:

    clock.tick(FPS)
    disegna()

    #insetiscp i movimenti


    giocatore1.movimenti(schermo_widht, schermo_height, finestra, giocatore2)
    giocatore2.movimenti()



    giocatore1.disegnagiocatori(finestra)
    giocatore2.disegnagiocatori(finestra)





    for event in pygame.event.get():
        if event.type==pygame.QUIT():
           run=False

    pygame.display.update()


pygame.quit()
