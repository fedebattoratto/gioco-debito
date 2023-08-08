import pygame


class Giocatori():

    def __init__(self, x, y):

        self.rect=pygame.Rect((x,y, 80, 100))

        self.vel_y = 0

        self.salta=False

        self.attacking=False

        self.attack_type=0

        self.vita=100


    def movimenti(self, schermo_widht, schermo_height, surface, target):

        velocità = 10
        gravità=2
        destra=0
        sinistra=0

        key=pygame.key.get_pressed()


        if self.attacking==False:
            

            if key[pygame.K_a]:
                destra=-velocità
        

            if key[pygame.K_d]:
                destra=velocità

            if key[pygame.K_w] and self.salta==False:
                self.vel_y = -30
                self.salta=True

            if key[pygame.K_r] or key[pygame.K_t]:
                self.attacca(surface, target)

            if key[pygame.K_r]:
                self.attack_type=1
            if key[pygame.K_t]:
                self.attack_type=2
            

        self.vel_y+=gravità
        sinistra+=self.vel_y

        if self.rect.left + destra < 0:
            destra = -self.rect.left

        if self.rect.right + destra > schermo_widht:
            destra = schermo_widht - self.rect.right

        if self.rect.bottom + sinistra > schermo_height - 110:
            self.vel_y=0
            self.salta=False

            sinistra=schermo_height-110-self.rect.bottom




        self.rect.x+=destra
        self.rect.y+=sinistra


    def attacca(self, surface, target):
        self.attacking=True
        attacking_rect=pygame.Rect(self.rect.centerx, self.rect.y, 2*self.rect.width, self.rect.height )
        if attacking_rect.collidedict(target.rect):
            target.vita -= 10
            print('preso')
       
        pygame.draw.rect(surface, (0, 255, 0),attacking_rect)
    
    
    def disegnagiocatori(self, surface):

        pygame.draw.rect(surface, (255, 0, 0), self.rect)


