# Normac130

import pygame
import math
import note_class



class Sustain(note_class.Note):
    def align(self,length):


        # trying to fix unalignment
        self.rect.centery = self.rect.centery / 1.33

        centery = self.rect.centery + self.rect.h
        self.image= pygame.transform.scale(self.image_copy,(self.image_size_copy[3] + 100, int(length + ((9.25 * abs(self.variant - 3)) + (30 if self.variant == 1 or self.variant == 5 else 0) ))))
        self.length = length

        center = self.image.get_rect().center
        rotated_image = pygame.transform.rotate(self.image, (self.variant - 3) * 9.25)
        self.rect = rotated_image.get_rect(center = center)
        self.image = rotated_image
        self.rect.centery = centery
        self.pointy = self.rect.centery - (30 if self.variant == 1 or self.variant == 5 else 20)


    def update(self, green, red, yellow, blue, orange):
        colours = []
        colours.append(green)
        colours.append(red)
        colours.append(yellow)
        colours.append(blue)
        colours.append(orange)

        if self.pointy > 515 or self.pointy < 390 or not colours[self.variant - 1]:
            self.pointy += self.speed

            if self.pointy > 100 and self.pointy < 390:
                self.speed += (self.speed / 75)

        self.pointx = ((self.variant - 3) * (self.pointy / 6)) + (450 + ((self.variant - 3) * 65))

        self.rect.centery = self.pointy - (self.length + (9.25 * abs(self.variant - 3))) / 2 * ((math.sin(math.radians(90 + (9.25 * (self.variant - 3))))) / math.sin(math.radians(90)))


        if self.pointy < 515 and self.pointy > 390:
            if colours[self.variant - 1]:
                centery = self.rect.centery
                try:
                    self.image = pygame.transform.scale(self.image_copy,(self.image_size_copy[3] + 100, int(self.length + (9.25 * abs(self.variant - 3) ) - self.speed)))
                except:
                    self.image = pygame.transform.scale(self.image_copy,(self.image_size_copy[3], 0))
                    self.note_done = True

                self.image_copy = self.image
                self.length -= self.speed

                center = self.image.get_rect().center
                rotated_image = pygame.transform.rotate(self.image, (self.variant - 3) * 9.25)
                self.rect = rotated_image.get_rect(center = center)
                self.image = rotated_image
                self.rect.centery = centery

        self.rect.centerx = self.pointx - (self.length + (9.25 * abs(self.variant - 3))) / 2 * ((math.sin(math.radians(9.25 * (self.variant - 3)))) / math.sin(math.radians(90)))







