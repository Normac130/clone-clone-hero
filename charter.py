# Normac130

import sustain_note
import note_class
import pygame

images = []
sustain_images = []


note_g_image = pygame.image.load("note_green.bmp")
sustain_g_image = pygame.image.load("sustain_green.bmp")

note_r_image = pygame.image.load("note_red.bmp")
sustain_r_image = pygame.image.load("sustain_red.bmp")

note_o_image = pygame.image.load("note_orange.bmp")
sustain_o_image = pygame.image.load("sustain_orange.bmp")

note_b_image = pygame.image.load("note_blue.bmp")
sustain_b_image = pygame.image.load("sustain_blue.bmp")

note_y_image = pygame.image.load("note_yellow.bmp")
sustain_y_image = pygame.image.load("sustain_yellow.bmp")


images.append(note_o_image)
images.append(note_b_image)
images.append(note_y_image)
images.append(note_r_image)
images.append(note_g_image)

sustain_images.append(sustain_o_image)
sustain_images.append(sustain_b_image)
sustain_images.append(sustain_y_image)
sustain_images.append(sustain_r_image)
sustain_images.append(sustain_g_image)


def chart(document):

    beat = 0
    bpm = 0
    count = 0
    g_list = []
    r_list = []
    y_list = []
    b_list = []
    o_list = []
    sustain_list = []
    last_note = [0,0,0,0,0]



    for line in document:
        if count % 5 != 0:
            beat += 1
            colour = 0
            line = line.split()

            for note in line:
                colour += 1
                note = int(note)
                if note == 1:

                    new_note = note_class.Note(colour, beat * notespacing , speed, images[colour - 1])
                    if colour == 1:
                        o_list.append(new_note)
                    elif colour == 2:
                        b_list.append(new_note)
                    elif colour == 3:
                        y_list.append(new_note)
                    elif colour == 4:
                        r_list.append(new_note)
                    elif colour == 5:
                        g_list.append(new_note)

                elif note == 2 and last_note[colour - 1] != 2:
                    if last_note[colour - 1] != 2:
                        new_note = note_class.Note(colour, beat * notespacing , speed, images[colour - 1])
                        if colour == 1:
                            o_list.append(new_note)
                        elif colour == 2:
                            b_list.append(new_note)
                        elif colour == 3:
                            y_list.append(new_note)
                        elif colour == 4:
                            r_list.append(new_note)
                        elif colour == 5:
                            g_list.append(new_note)


                        newer_note = sustain_note.Sustain(colour, beat * notespacing, speed, sustain_images[colour - 1])
                        sustain_list.append(newer_note)


                elif note != 2 and last_note[colour - 1] == 2:

                    for sustain in sustain_list:
                        if sustain.variant == colour and not sustain.aligned:
                            sustain.align(sustain.align_count * notespacing * 2)
                            sustain.aligned = True


                elif last_note[colour - 1] == 2:
                    for sustain in sustain_list:
                        if sustain.variant == colour and not sustain.aligned:
                            sustain.align_count += 1


                last_note[colour - 1] = note

        elif count == 0:
            speed = 3.002777777777778 # (((int(line) / 60) / 60) * 100) * (94 / 100)
            if int(line) == 115:
                bpm = 1.85
            elif int(line) == 121:
                bpm = -1.4
            elif int(line) == 92:
                bpm = 16
            notespacing = ((int(line) / 4) + bpm) * 1

        count += 1


    return (g_list,r_list,y_list,b_list,o_list,sustain_list)





