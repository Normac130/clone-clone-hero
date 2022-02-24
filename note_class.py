# Normac130

import pygame

WHITE = ( 255, 255, 255)

class Note(pygame.sprite.Sprite):
    def __init__( self, variant, place, song_speed, image):

        super().__init__()


        # image scaling setup

        image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(image,(50,25))
        self.image_copy = pygame.transform.scale(image,(50,25))
        self.image_size = self.image.get_rect()
        self.image_size_copy = self.image.get_rect()
        self.note_done = False

        self.rect = self.image.get_rect()
        self.variant = variant
        self.rect.centery = 0 - place
        self.speed = song_speed
        self.align_count = 1
        self.aligned = False



    def update(self, green, red, yellow, blue, orange):

        #  image scaling and movement

        self.rect.centery += self.speed
        #print(self.rect.centery)

        if self.rect.centery > 100:
            self.speed += (self.speed / 75)


        self.rect.centerx = ((self.variant - 3.45) * (self.rect.centery / 6)) + (450 + ((self.variant - 3) * 65))


        if self.rect.centery > -100:
            self.image_size[2] = (self.rect.centery / 7) + self.image_size_copy[2]
            self.image_size[3] = (self.rect.centery / 14) + self.image_size_copy[3]

            self.image = pygame.transform.scale(self.image_copy,(self.image_size[2],self.image_size[3]))

