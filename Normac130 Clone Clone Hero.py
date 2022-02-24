# Normac130

import pygame
import note_class
import sustain_note
import charter
import random

pygame.init()

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
FRET_KEY = (200,100,200)

size = (900,600)
screen = pygame.display.set_mode(size)

note_list_g   = []
note_list_r   = []
note_list_y   = []
note_list_b   = []
note_list_o   = []
sustain_list  = []
hit_list      = []

green         = False
red           = False
yellow        = False
blue          = False
orange        = False
playing       = False
anim_play     = False
end_anim_play = False
anim_y_top    = -300
anim_y_bottom = 600
anim_y_change = 0

score         = 0
first_high    = 0
second_high   = 0
third_high    = 0
high_display  = True
first         = False
second        = False
third         = False
closing       = False
fretboard     = False
autoplay      = False


# images
screen_anim_top = pygame.image.load("between_screen.bmp")
screen_anim_bottom = pygame.image.load("between_screen_bottom.bmp")
checkmark = pygame.image.load("checkmark.bmp")
checkmark.set_colorkey(WHITE)
background = pygame.image.load("selection_screen.bmp")
fretboard_image = pygame.image.load("fretboard2.bmp")
fretboard_image.set_colorkey(FRET_KEY)

hit_note = pygame.image.load("hit_note.bmp")
hit_note.set_colorkey(BLACK)
hit_list.append(hit_note)
hit_note_two = pygame.image.load("hit_note_two.bmp")
hit_note_two.set_colorkey(BLACK)
hit_list.append(hit_note_two)
hit_note_three = pygame.image.load("hit_note_three.bmp")
hit_note_three.set_colorkey(BLACK)
hit_list.append(hit_note_three)
hit_note_four = pygame.image.load("hit_note_four.bmp")
hit_note_four.set_colorkey(BLACK)
hit_list.append(hit_note_four)
hit_note_five = pygame.image.load("hit_note_five.bmp")
hit_note_five.set_colorkey(BLACK)
hit_list.append(hit_note_five)
hit_note_six = pygame.image.load("hit_note_six.bmp")
hit_note_six.set_colorkey(BLACK)
hit_list.append(hit_note_six)


font = pygame.font.SysFont('Calibri',50,True,False)

pygame.display.set_caption("Normac130 Clone Clone Hero")

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if playing:
                if not autoplay:
                    if event.key == pygame.K_a:
                        orange = True
                        for note in note_list_o:
                            if note.rect.centery < 515 and note.rect.centery > 390:
                                note.rect.centery = 1000
                                all_sprites_list.remove(note)
                                score += 100

                    elif event.key == pygame.K_s:
                        blue = True
                        for note in note_list_b:
                            if note.rect.centery < 515 and note.rect.centery > 390:
                                note.rect.centery = 1000
                                all_sprites_list.remove(note)
                                score += 100

                    elif event.key == pygame.K_d:
                        yellow = True
                        for note in note_list_y:
                            if note.rect.centery < 515 and note.rect.centery > 390:
                                note.rect.centery = 1000
                                all_sprites_list.remove(note)
                                score += 100

                    elif event.key == pygame.K_f:
                        red = True
                        for note in note_list_r:
                            if note.rect.centery < 515 and note.rect.centery > 390:
                                note.rect.centery = 1000
                                all_sprites_list.remove(note)
                                score += 100

                    elif event.key == pygame.K_g:
                        green = True
                        for note in note_list_g:
                            if note.rect.centery < 515 and note.rect.centery > 390:
                                note.rect.centery = 1000
                                all_sprites_list.remove(note)
                                score += 100

                if event.key == pygame.K_ESCAPE:

                    pygame.mixer.music.fadeout(600)
                    end_anim_play = True
                    closing = True
                    score = 0


        elif event.type == pygame.KEYUP:
            if playing:
                if event.key == pygame.K_a:
                    orange = False
                elif event.key == pygame.K_s:
                    blue   = False
                elif event.key == pygame.K_d:
                    yellow = False
                elif event.key == pygame.K_f:
                    red    = False
                elif event.key == pygame.K_g:
                    green  = False

        elif not playing:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[1] >= 375 and mouse_pos[1] <= 450 and not closing:
                    if mouse_pos[0] >= 80 and mouse_pos[0] <= 285:

                        music_ = pygame.mixer.music.load("1.mp3")
                        song = open("1.txt")
                        anim_play = True
                        first = True

                    elif mouse_pos[0] >= 350 and mouse_pos[0] <= 550:

                        music_ = pygame.mixer.music.load("2.mp3")
                        song = open("2.txt")
                        anim_play = True
                        second = True

                    elif mouse_pos[0] >= 610 and mouse_pos[0] <= 810:

                        music_ = pygame.mixer.music.load("3.mp3")
                        song = open("3.txt")
                        anim_play = True
                        third = True

                    if anim_play:

                        closing = True
                        anim_y_change = 0

                        note_list = charter.chart(song)
                        song.close
                        all_sprites_list = pygame.sprite.Group()

                        note_list_g = note_list[0]
                        note_list_r = note_list[1]
                        note_list_y = note_list[2]
                        note_list_b = note_list[3]
                        note_list_o = note_list[4]
                        sustain_list = note_list[5]

                        all_sprites_list.add(sustain_list)
                        all_sprites_list.add(note_list_g)
                        all_sprites_list.add(note_list_r)
                        all_sprites_list.add(note_list_y)
                        all_sprites_list.add(note_list_b)
                        all_sprites_list.add(note_list_o)

                elif  mouse_pos[1] >= 485 and mouse_pos[1] <= 557:
                    if mouse_pos[0] >= 77 and mouse_pos[0] <= 430:
                        first_high = 0
                        second_high = 0
                        third_high = 0

                    elif mouse_pos[0] >= 468 and mouse_pos[0] <= 820:
                        if autoplay:
                            autoplay = False
                        else:
                            autoplay = True


    if autoplay:
        for note in note_list_g:
            if note.rect.centery < 465 and note.rect.centery > 440:
                note.rect.centery = 1000
                all_sprites_list.remove(note)
                score += 100
        for note in note_list_r:
            if note.rect.centery < 465 and note.rect.centery > 440:
                note.rect.centery = 1000
                all_sprites_list.remove(note)
                score += 100
        for note in note_list_y:
            if note.rect.centery < 465 and note.rect.centery > 440:
                note.rect.centery = 1000
                all_sprites_list.remove(note)
                score += 100
        for note in note_list_b:
            if note.rect.centery < 465 and note.rect.centery > 440:
                note.rect.centery = 1000
                all_sprites_list.remove(note)
                score += 100
        for note in note_list_o:
            if note.rect.centery < 465 and note.rect.centery > 440:
                note.rect.centery = 1000
                all_sprites_list.remove(note)
                score += 100
        for sustain in sustain_list:
            if sustain.pointy < 465 and sustain.pointy > 440:
                if sustain.variant == 1:
                    orange = True
                if sustain.variant == 2:
                    blue = True
                if sustain.variant == 3:
                    yellow = True
                if sustain.variant == 4:
                    red = True
                if sustain.variant == 5:
                    green = True



    screen.blit(background,[0,0])
    if fretboard:
        screen.blit(fretboard_image,[0,0])

    if anim_play or end_anim_play:
        screen.blit(screen_anim_top, [0,anim_y_top])
        screen.blit(screen_anim_bottom, [0,anim_y_bottom])



    if anim_play:

        if closing:
            anim_y_change += 0.25
        else:
            anim_y_change -= 0.25

        anim_y_top = -300 + (anim_y_change * anim_y_change)
        anim_y_bottom = 600 - (anim_y_change * anim_y_change)


        if anim_y_top >= 0 and closing:
            closing = False
            background = pygame.image.load("space_background.bmp")
            fretboard = True
            high_display = False

        elif anim_y_top <= -300 and not closing:
            anim_play = False
            playing = True
            pygame.mixer.music.play()

    if end_anim_play:

        if closing:
            anim_y_change += 0.25
        else:
            anim_y_change -= 0.25

        anim_y_top = -300 + (anim_y_change * anim_y_change)
        anim_y_bottom = 600 - (anim_y_change * anim_y_change)


        if anim_y_top >= 0 and closing:
            closing = False
            background = pygame.image.load("selection_screen.bmp")
            fretboard = False
            playing = False
            high_display = True
            orange = False
            blue = False
            yellow = False
            red = False
            green = False

        elif anim_y_top <= -300 and not closing:
            end_anim_play = False


    if playing:
        if len(all_sprites_list) == 0:
            pygame.mixer.music.fadeout(600)
            closing = True
            end_anim_play = True

            if not autoplay:
                if score > first_high and first:
                    first_high = score
                    first = False
                elif score > second_high and second:
                    second_high = score
                    second = False
                elif score > third_high and third:
                    third_high = score
                    third = False
            score = 0

        for note in all_sprites_list:
            if note.rect.centery > 1000:
                all_sprites_list.remove(note)

        for sustain in sustain_list:
            if sustain.note_done:

                if sustain.variant == 1:
                    orange = False
                if sustain.variant == 2:
                    blue = False
                if sustain.variant == 3:
                    yellow = False
                if sustain.variant == 4:
                    red = False
                if sustain.variant == 5:
                    green = False

                sustain.note_done = False

                all_sprites_list.remove(sustain)
                sustain.pointy = 1000

            elif sustain.pointy < 515 and sustain.pointy > 390:
                if green:
                    score += 2
                if red:
                    score += 2
                if yellow:
                    score += 2
                if orange:
                    score += 2
                if blue:
                    score += 2

        if orange:
            screen.blit(hit_list[random.randrange(0,5)],[122,360])
        if blue:
            screen.blit(hit_list[random.randrange(0,5)],[264,360])
        if yellow:
            screen.blit(hit_list[random.randrange(0,5)],[400,360])
        if red:
            screen.blit(hit_list[random.randrange(0,5)],[540,360])
        if green:
            screen.blit(hit_list[random.randrange(0,5)],[680,360])



        all_sprites_list.update(orange,blue,yellow,red,green)
        all_sprites_list.draw(screen)



    if not high_display:
        scoretxt = font.render(str(score),True, WHITE)
        screen.blit(scoretxt,[720,70])
    else:
        first_hightxt = font.render(str(first_high),True, BLACK)
        screen.blit(first_hightxt,[105,205])
        first_hightxt = font.render(str(first_high),True, WHITE)
        screen.blit(first_hightxt,[100,200])

        second_hightxt = font.render(str(second_high),True, BLACK)
        screen.blit(second_hightxt,[370,205])
        second_hightxt = font.render(str(second_high),True, WHITE)
        screen.blit(second_hightxt,[365,200])

        third_hightxt = font.render(str(third_high),True, BLACK)
        screen.blit(third_hightxt,[630,205])
        third_hightxt = font.render(str(third_high),True, WHITE)
        screen.blit(third_hightxt,[625,200])

        if autoplay:
            screen.blit(checkmark,[749,493])


    pygame.display.flip()

    clock.tick(60)

pygame.quit()