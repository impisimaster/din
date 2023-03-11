from random import randint
import pygame
pygame.init()
import json 
import os
from time import *
from pygame import *
WIN_WIDTH=500
WIN_HEIGHT=500
New=(141,255,128)
WHITE =(255,255,255)
grey_outline = (165,165,165)
GRAY = (200,200,200)
New_outline = (77,191,107)
New_pause = (82,206,114)
mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))  #окно программы (main window)
pygame.display.set_caption("Dino Chrome")
clock = pygame.time.Clock()
BLUE = (0,0,255)
font_2 = pygame.font.SysFont('arial',70)
pause = font_2.render("PAUSE",True,BLUE)
adds = 0
cards = []
num_cards = 15
giants = True
loadint1 = pygame.transform.scale(pygame.image.load('loading_1.png'),(500,500)).convert()

timer = 0
game_over = False
eskape = False
s=5
white = (255,255,255)
grass = (0, 170, 0)
audio_jump = pygame.mixer.Sound('jump.wav')
audio_point = pygame.mixer.Sound('point.wav')
audio_ded = pygame.mixer.Sound('die.wav')
volume = 0.5
audio_ded.set_volume(volume)
audio_jump.set_volume(volume)
audio_point.set_volume(volume)
adsdsd = 1 
stop=0
jazikn =2
zvykn = 5
a=0
switch=0
alll = list()
zombie = list()
bullets = list()
RED = (255, 51, 0)
RED2= (240, 52, 5)
grey = (202, 224, 227)
blue = (111, 157, 163)
GREEN=(0, 255, 0)
GREEN_outline=(0, 245, 0)
GRAY = (191, 192, 194)
return_to_game = False
BLACK = (0,0,0)
dsasasasas = 1
game = ''
record = 0
ADR = 0
begi = False
mw.blit(loadint1,(0,0))
pygame.display.update()
clock.tick(60)
background_list = []
score_list = []
loadint2 = pygame.transform.scale(pygame.image.load('loading_2.png'),(500,500)).convert()
a = 0
speed = 1
FPS = 60
first_firts= 0
cactus_list=[]
cactus_name_list = [
    'cactus_1.png',
    'cactus_2.png',
    'cactus_3.png',
    'cactus_4.png',
    'cactus_5.png',
    'cactus_6.png',
    'cactus_7.png',
    'cactus_8.png'
]
meteor_name_list = [
    'meteor_1.png',
    'meteor_2.png',
    'meteor_3.png',
    'meteor_4.png',
    'meteor_5.png',
    'meteor_6.png',
    'meteor_7.png',
    'meteor_8.png',
    'meteor_9.png',
    'meteor_10.png',
    'meteor_11.png'
]
meteor_list = []
bird_list = []
meteor_down_list=[]
point = 100
trasi = True
x_first = 350
while a != 10:
    mw.blit(loadint2,(0,0))
    a+=1
    pygame.display.update()
    clock.tick(60)
 

######################################################################################################################################################################################


def import_def():
    global ADR, score_list,record, dict_record
    with open('record.json','r',encoding='utf-8') as results:
        dict_record = json.load(results)
    ADR = dict_record['ADR']
    score_list= dict_record['score']
    record= dict_record['record']

import_def()

def check_score():
    global record
    if score >= record:
        record = score

def export():
    score_all = 0
    for i in score_list:
        score_all += i
    dict_record['ADR'] = score_all/len(score_list) 
    dict_record['score'] = score_list
    dict_record['record'] = record
    with open('record.json','w',encoding='utf-8')as result:
        json.dump(dict_record,result,sort_keys=True,ensure_ascii=False) 



######################################################################################################################################################################################



class Area():
    def __init__(self, x=0, y=0, width=20, height=10, color=None):
        self.rect = pygame.Rect((x, y), (width, height))
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color
 
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    
    def outline(self, flame_color, thickness):
        pygame.draw.rect(mw, flame_color, self.rect, thickness)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont("verdana", fsize).render(text,True,text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


######################################################################################################################################################################################


class Background():
    def __init__(self,x):
        self.x = x
        self.background = pygame.transform.scale(pygame.image.load('background.png'),(1500,730)).convert()
        background_list.append(self)
        self.y = -10
    def update(self): 
        global background
        mw.blit(self.background,(self.x,self.y))
        if game == 'animation':
            if trasi:
                qwe = randint(1,4)
                if qwe == 1:
                    if self.x >= -5:
                        self.x -= 3
                        player.x -= 3
                    else:
                        self.x += 3
                        player.x += 3
                if qwe == 2:
                    if self.x >= 5:
                        self.x += 3
                        player.x += 3
                    else:
                        self.x -= 3
                        player.x -= 3

                if qwe == 3:
                    if self.y >= -5:
                        self.y -= 1.5
                        player.y -= 1.5
                    else:
                        self.y += 1.5
                        player.y += 1.5

                if qwe == 4:
                    if self.y >= 5:
                        self.y += 1.5
                        player.y += 1.5
                    else:
                        self.y -= 1.5
                        player.y -= 1.5
        if game == '' or game == 'animation' and not trasi:
            self.x -= 3
        if abs(self.x) == 1500:
            background = Background(self.x+3000) 
            background_list.remove(self)


        

background_f = Background(-11)
background = Background(1488)



######################################################################################################################################################################################




class Player():  
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.y_kor = 0
        self.health = 3
        self.direction = 'down'
        self.menatsa = 0
        self.menats = 2
        self.menatsa_down = 10
        self.menats_down = 2
        self.ded = 0
        self.down = False
        self.y_need = 435
        self.god = False
        self.god_time = 0
        self.x_foran = 1000
        self.dino = pygame.transform.scale(pygame.image.load('dino.png'),(75,100)).convert_alpha()
    def update(self):   
        global switch, mw, game,adsdsd, background_f, meteor_first, score
        if game == 'animation':
            mw.blit(self.dino,(self.x_foran,self.y))
            if begi:
                self.y = 435
                self.x_foran -= 1
                if self.menatsa == 10:
                    self.menatsa = 0
                    if self.menats == 1:
                        self.dino = pygame.transform.scale(pygame.image.load('dino1.png'),(75,100)).convert_alpha()
                        self.menats = 2
                    elif self.menats == 2:
                        self.dino = pygame.transform.scale(pygame.image.load('dino2.png'),(75,100)).convert_alpha()
                        self.menats = 1
                self.menatsa += 1
                if self.x_foran == 100:
                    game = ''
        else:
            if not self.health == 0:
                mw.blit(self.dino,(100,self.y))
            if game == '':
                if self.god_time >= 0:
                    self.god_time -= 1
                if self.god_time <= 0:
                    self.god = False
                keys_p = key.get_pressed()
                if keys_p[K_DOWN]:     
                    self.down = True
                    if self.direction == 'down':
                        self.y = 485
                        if self.menatsa_down == 10:
                            self.menatsa_down = 0
                            if self.menats_down == 1:
                                self.dino = pygame.transform.scale(pygame.image.load('dino_down1.png'),(100,50)).convert_alpha()
                                self.menats_down = 2
                            elif self.menats_down == 2:
                                self.dino = pygame.transform.scale(pygame.image.load('dino_down2.png'),(100,50)).convert_alpha()
                                self.menats_down = 1
                        self.menatsa_down += 1

                for i in cactus_list:
                    if self.down:
                        if i.x+i.w-10>self.x-50 and i.x-i.w+10<self.x+50 and i.y-i.h+10<self.y:
                            if not self.god:
                                audio_ded.play()
                                self.health -= 1
                                self.god = True
                                if speed > 10:
                                    self.god_time = 90 * 10
                                if speed < 10:
                                    self.god_time = 90 * speed
                    elif i.x+i.w-30>self.x and i.x-i.w+10<self.x and i.y-i.h+10<self.y:
                        if not self.god:
                            audio_ded.play()
                            self.health -= 1
                            self.god = True
                            if speed > 10:
                                self.god_time = 90 * 10
                            if speed < 10:
                                self.god_time = 90 * speed
                for i in bird_list:
                    if i.x+i.w-10>self.x and i.x-i.w+10<self.x and i.y+i.h-10>self.y and i.y-i.h+10<self.y:
                        if not self.god:
                            if i.y == 380 and not self.down:
                                if not self.y+75 < i.y:
                                    audio_ded.play()
                                    self.health -= 1
                                    self.god = True
                                    if speed > 10:
                                        self.god_time = 90 * 10
                                    if speed < 10:
                                        self.god_time = 90 * speed
                            if i.y == 320 and self.direction != 'down':
                                if not self.y+75 < i.y:
                                    audio_ded.play()
                                    self.health -= 1
                                    self.god = True
                                    if speed > 10:
                                        self.god_time = 90 * 10
                                    if speed < 10:
                                        self.god_time = 90 * speed
                            else:
                                audio_ded.play()
                                self.health -= 1
                                self.god = True
                                if speed > 10:
                                    self.god_time = 90 * 10
                                if speed < 10:
                                    self.god_time = 90 * speed
                for i in meteor_down_list:
                    if i.x-25>self.x and i.x-10<self.x+25 and i.y-55<self.y:
                        if not self.god:
                            audio_ded.play()
                            self.health -= 1
                            self.god = True
                            if speed > 10:
                                self.god_time = 90 * 10
                            if speed < 10:
                                self.god_time = 90 * speed
                        
                if not self.down:
                    if self.direction == 'down':
                        self.y = 435
                        self.y_kor = 0
                    self.menatsa_down = 10

                if keys_p[K_UP] and self.direction == 'down':
                    if not self.down:
                        audio_jump.play()
                        self.y_kor = 220
                        self.direction = 'up'

                if keys_p[K_SPACE] and self.direction == 'down':
                    if not self.down:
                        audio_jump.play()
                        self.y_kor = 220
                        self.direction = 'up'
                if keys_p[K_F1]:
                    score += 10
                if keys_p[K_F2]:
                    self.health = 3

                if self.direction != 'down':
                    self.dino = pygame.transform.scale(pygame.image.load('dino.png'),(75,100)).convert_alpha()
                    if self.y_kor <= -100:
                        if not self.down:
                            self.y_kor = -100
                    if self.down:
                        self.y_kor = -100
                    self.y -= (self.y_kor/9.5)/speed
                    self.y_kor -= abs(self.y_kor/9.5)/speed
                    if self.y_kor < 5 and self.y_kor > 0:
                        self.y_kor = -10
                    if self.y >= 435:
                        self.y = 435
                        self.direction = 'down'
                        self.dino = pygame.transform.scale(pygame.image.load('dino1.png'),(75,100)).convert_alpha()

                if self.direction == 'down':
                    if not self.down:
                        if self.menatsa == 10:
                            self.menatsa = 0
                            if self.menats == 1:
                                self.dino = pygame.transform.scale(pygame.image.load('dino1.png'),(75,100)).convert_alpha()
                                self.menats = 2
                            elif self.menats == 2:
                                self.dino = pygame.transform.scale(pygame.image.load('dino2.png'),(75,100)).convert_alpha()
                                self.menats = 1
                        self.menatsa += 1
                    if self.down:
                        self.menatsa = 10

            if self.health == 0:
                if self.ded == 0:
                    check_score()
                    score_list.append(score)
                    audio_ded.play()
                self.dino_ded = pygame.transform.scale(pygame.image.load('dino_ded.png'),(75,100)).convert_alpha()
                mw.blit(self.dino_ded,(100,self.y))
                self.ded +=1
                game = 'stop'
                if self.ded == 96:
                    background_f = Background(-11)
                    background = Background(1488)
                    self.x_foran = 1000
                    meteor_first = Meteor(True)
                    game = 'animation'
                    switch = 0
                    WIN_WIDTH=500
                    WIN_HEIGHT=500
                    mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
                    self.ded = 0
                    self.health = 3
                    adsdsd = 1
                    game = ''
            self.down = False


player = Player(100,435)       
        


######################################################################################################################################################################################


class Cactus():
    def __init__(self,distans):
        global x_first
        self.distans = distans
        a = randint(1,8)                
        if a == 1:
            self.y = 440
            self.w = 50
            self.h = 100
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_1.png'),(50,100)).convert_alpha()
        if a == 2:
            self.y = 440
            self.w = 50
            self.h = 100
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_2.png'),(50,100)).convert_alpha()
        if a == 3:
            self.y = 440
            self.w = 50
            self.h = 100
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_3.png'),(50,100)).convert_alpha()
        if a == 4:
            self.y = 440
            self.w = 50
            self.h = 100
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_4.png'),(50,100)).convert_alpha()
        if a == 5:
            self.y = 440
            self.w = 50
            self.h = 100
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_5.png'),(50,100)).convert_alpha()
        if a == 6:
            self.w = 30
            self.h = 60
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_6.png'),(30,60)).convert_alpha()
            self.y = 480
        if a == 7:
            self.w = 80
            self.h = 100
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_7.png'),(80,100)).convert_alpha()
            self.y = 440
        if a == 8:
            self.y = 440
            self.w = 50
            self.h = 100
            self.cactus = pygame.transform.scale(pygame.image.load('cactus_8.png'),(50,100)).convert_alpha()
        cactus_list.append(self)
        self.x = x_first+self.distans
        x_first = self.x
        
    def update(self):
        if game != 'animation':
            mw.blit(self.cactus,(self.x,self.y))
        if game == '':
            self.x -= 3
            if self.x < -100:
                cactus_list.remove(self)
                if score > 5000:
                    cactus = Cactus(randint(1500,3000))
                elif score > 2500:
                    cactus = Cactus(randint(750, 2000))
                elif score > 1000:
                    cactus = Cactus(randint(int(150*(speed/1.1)),int(350*speed/1.1)))
                elif score > 500:
                    cactus = Cactus(randint(int(200*(speed/1.1)),int(400*speed/1.1)))
                else: 
                    cactus = Cactus(randint(300,500))

    def respawn(self):
        cactus_list.remove(self)
        
        if score > 5000:
            cactus = Cactus(randint(1500,3000))
        elif score > 2500:
            cactus = Cactus(randint(750, 2000))
        elif score > 1000:
            cactus = Cactus(randint(int(150*(speed/1.1)),int(350*speed/1.1)))
        elif score > 500:
            cactus = Cactus(randint(int(200*(speed/1.1)),int(400*speed/1.1)))
        else: 
            cactus = Cactus(randint(300,500))

for i in range(10):
    cactus = Cactus(randint(300,700))



######################################################################################################################################################################################


                                
class Bird():
    def __init__(self,x):
        self.x = x
        a = randint(1,3)                
        if a == 1:
            self.y = 435
        if a == 2:
            self.y = 380
        if a == 3:
            self.y = 320
        self.menatsa = 0
        self.menats = 2
        self.w = 100
        self.h = 75
        self.bird = pygame.transform.scale(pygame.image.load('bird.png'),(100,75)).convert_alpha()
        bird_list.append(self)

    def update(self):
        mw.blit(self.bird,(self.x,self.y))
        if game == '':
            self.x -= 5
            if self.menatsa == 15:
                self.menatsa = 0
                if self.menats == 1:
                    self.bird = pygame.transform.scale(pygame.image.load('bird.png'),(100,75)).convert_alpha()
                    self.y -= 25
                    self.menats = 2
                elif self.menats == 2:
                    self.bird = pygame.transform.scale(pygame.image.load('bird1.png'),(100,75)).convert_alpha()
                    self.y += 25
                    self.menats = 1
            self.menatsa += 1
            if self.x < -100:
                bird_list.remove(self)
                bird = Bird(randint(2500,8000))

bird = Bird(randint(9000,21000))


######################################################################################################################################################################################



class Hp():
    def __init__(self):
        self.health = pygame.transform.scale(pygame.image.load('health.png'),(50,50)).convert_alpha()

    def update(self):
        
        if player.health == 3:
            mw.blit(self.health, (20,10))
            mw.blit(self.health, (80,10))
            mw.blit(self.health, (140,10))
        if player.health == 2:
            mw.blit(self.health, (20,10))
            mw.blit(self.health,(80,10))
        if player.health == 1:
            mw.blit(self.health,(20,10))

hp = Hp()


######################################################################################################################################################################################


class Meteor():
    def __init__(self,animatons=False):
        self.y = -200
        self.menatsa = 0
        self.animation = 0
        self.gradus = 0
        self.animations = animatons
        self.a = randint(1,4)
        self.b = randint(1,3)
        if self.animations:
            self.meteor = pygame.transform.scale(pygame.image.load('meteor_1.png'),(400,400)).convert_alpha() 
            self.x = -750
            self.y = -750
        else:
            self.d = 1
            self.r = True
            meteor_list.append(self)
            if self.a == 1:
                self.x = 250
            if self.a == 2:
                self.x = 500
            if self.a == 3:
                self.x = 760
            if self.a == 4:
                self.x = 1000
            self.meteor = pygame.transform.scale(pygame.image.load('meteor_1.png'),(100,100)).convert_alpha()
            if self.a == 1 and self.b == 2:
                self.meteor = pygame.transform.rotate(self.meteor,-35)
    def update(self):
        global trasi,begi
        mw.blit(self.meteor,(self.x,self.y))
        if game == 'animation':
            if self.y == 150:
                self.x += 185
                self.y += 185
                self.meteor = pygame.transform.scale(pygame.image.load('meteor.png'),(200,200)).convert_alpha()
                trasi = False
                background_f.x = 0
                background_f.y = -10
            if self.y >= 150:
                self.meteor = pygame.transform.scale(pygame.image.load('meteor.png'),(200,200)).convert_alpha()
                self.meteor = pygame.transform.rotate(self.meteor,self.gradus)
                if self.gradus < 0 and self.gradus > -46 or self.gradus < -90 and self.gradus > -136 or self.gradus < -180 and self.gradus > -226 or self.gradus < -270 and self.gradus > -316:  
                    self.y -= 1
                    self.x-=1
                else: 
                    self.y += 1
                    self.x+=1
                self.gradus -= 1
                if self.gradus == -360:
                    self.gradus = 0
                self.x -= 1
                begi = True
            else:
                self.x += 2
                self.y += 2
                if self.menatsa == 7:
                    self.menatsa = 0
                    self.meteor = pygame.transform.scale(pygame.image.load(meteor_name_list[self.animation]),(400,400)).convert_alpha() 
                    self.animation += 1
                    if self.animation == 11:
                        self.animation = 0
                self.menatsa += 1
        if game == '':
            if self.r:
                if self.a == 1 and self.b == 1:
                    self.x += 1
                    self.y += 2.9
                if self.a == 2 and self.b == 1:
                    self.x += 2.5
                    self.y += 1.74
                if self.a == 3 and self.b == 1:
                    self.x += 1.52
                    self.y += 0.87
                if self.a == 4 and self.b == 1:
                    self.x += 4
                    self.y += 1.74

                if self.a == 1 and self.b == 2:
                    self.x -= 0.1
                    self.y += 1.9
                if self.a == 2 and self.b == 2:
                    self.x += 1.5
                    self.y += 0.74
                if self.a == 3 and self.b == 2:
                    self.x += 0.52
                    self.y += 0.13
                if self.a == 4 and self.b == 2:
                    self.x += 3
                    self.y += 0.74

                if self.a == 1 and self.b == 3:
                    self.x += 2
                    self.y += 3.9
                if self.a == 2 and self.b == 3:
                    self.x += 3.5 
                if self.a == 3 and self.b == 3:
                    self.x += 2.52
                    self.y += 1.87
                if self.a == 4 and self.b == 3:
                    self.x += 5
                    self.y += 2.74
                if self.menatsa == 7:
                    self.menatsa = 0
                    self.meteor = pygame.transform.scale(pygame.image.load(meteor_name_list[self.animation]),(100,100)).convert_alpha() 
                    if self.a == 1 and self.b == 2:
                        self.meteor = pygame.transform.rotate(self.meteor,-35)
                    self.animation += 1
                    if self.animation == 11:
                        self.animation = 0
                self.menatsa += 1
            if self.y > 432 and self.y < 438:
                if self.d == 1:
                    self.y = 435
                    self.r = False
                    self.meteor = pygame.transform.scale(pygame.image.load('meteor.png'),(50,50)).convert_alpha() 
                    self.y +=50 
                    meteor_down_list.append(self)
                    self.d +=1
            if not self.r:
                self.x -= 3

            if speed > 10:
                if self.x < -500:
                    meteor_list.remove(self)
                    meteor = Meteor()
            elif speed < 10:
                if self.x < -5000//speed:
                    meteor_list.remove(self)
                    meteor = Meteor()

######################################################################################################################################################################################
 
meteor_first = Meteor(True)


language = 'eng'
def jazikklas():
    global language
    global vved
    if jazikn==0:
        language='ukr'
        nastr.set_text('Налаштування', 40)
        jaziknat.set_text('Мова', 30)
        zvyk.set_text('Гучність', 30)
        ready.set_text('Готово', 45)
        k1.set_text('Почати', 35)
        k2.set_text('Налаштування', 20)
        k3.set_text('Рекорди', 13)
        k4.set_text('Вийти', 15)
        savess.set_text('Рекорди', 50)
        resume.set_text('Продовжити', 25)
        settings.set_text('Налаштування', 25)
        exit_to_menu.set_text('Вихід у меню', 25)
        record_text.set_text('Рекорд',40)
        ADR_text.set_text('Середній забіг',40)
        num_run_text.set_text('Кількість забігів',40)
    if jazikn==1:
        language='pol'
        nastr.set_text('Ustawienia', 40)
        jaziknat.set_text('Język', 30)
        zvyk.set_text('Głośność', 30)
        ready.set_text('Gotowy', 40)
        k1.set_text('Rozpocząć', 30)
        k2.set_text('Ustawienia', 30)
        k3.set_text('Rekord ', 13)
        k4.set_text('Wychod', 12)
        savess.set_text('Rekord ', 50)
        resume.set_text('Kontynuować', 25)
        settings.set_text('Ustawienia', 30)
        exit_to_menu.set_text('Wyjdź do menu', 25)
        record_text.set_text('Rekord',40)
        ADR_text.set_text('Przeciętny wyścig',40)
        num_run_text.set_text('Liczba wyścigów',40)
    if jazikn==2:
        language='eng'
        nastr.set_text('Settings', 40)
        jaziknat.set_text('Language', 30)
        zvyk.set_text('Volume', 30)
        ready.set_text('Ready', 45)
        k1.set_text('Start', 40)
        k2.set_text('Settings', 30)
        k3.set_text('Records', 15)
        k4.set_text('Exit', 20)
        savess.set_text('Records', 50)
        resume.set_text('Continue', 30)
        settings.set_text('Settings', 40)
        exit_to_menu.set_text('Exit to menu', 30) 
        record_text.set_text('Record',40)
        ADR_text.set_text('Average race',40)
        num_run_text.set_text('Number of runs',40) 

    

    
loadint3 = pygame.transform.scale(pygame.image.load('loading_3.png'),(500,500)).convert()

a = 0
while a != 5:
    mw.blit(loadint3,(0,0))
    a+=1
    pygame.display.update()
    clock.tick(60)
 

######################################################################################################################################################################################


score_text = Label(1200, 20,0, 0, New)
score_text.color(New)
score_text.set_text('0', 35)

exit = Label(25, 25,30, 30, New)
exit.color(New)
exit.set_text('<', 35)

nastr = Label(120, 20,80, 55, New)
nastr.color(New)
nastr.set_text('Налаштування', 40)

resume = Label(535, 270, 250, 80, New_pause)
resume.color(New_pause)
resume.set_text('Continue', 30)

settings = Label(535, 390,250, 80, New_pause)
settings.color(New_pause)
settings.set_text('Settings', 40)

exit_to_menu = Label(535, 510, 250, 80, New_pause)
exit_to_menu.color(New_pause)
exit_to_menu.set_text('Exit to menu', 30) 


jaziknat = Label(50, 90,80, 55, New)
jaziknat.color(New)
jaziknat.set_text('Мова', 30)

left5 = Label(240, 80,50, 50, New)
left5.color(New)
left5.set_text('<', 50)

jazikmen = Label(285, 90,80, 55, New)
jazikmen.color(New)
jazikmen.set_text('', 30)

right5 = Label(450, 80,50, 50, New)
right5.color(New)
right5.set_text('>', 50)


zvyk = Label(20, 140,80, 55, New)
zvyk.color(New)
zvyk.set_text('Гучність', 30)

left6 = Label(240, 130,50, 50, New)
left6.color(New)
left6.set_text('<', 50)

zvyka = Label(285, 140,80, 55, New)
zvyka.color(New)
zvyka.set_text('', 30)

right6 = Label(450, 130,50, 50, New)
right6.color(New)
right6.set_text('>', 50)


savess = Label(150, 10, 80, 70, New)
savess.color(New)
savess.set_text('Скіни', 50)


ready = Label(155, 350,200, 70, GREEN)
ready.color(GREEN)
ready.set_text('Готово', 50)

k1 = Label(150, 150,200, 70, RED)
k1.color(RED)
k1.set_text('Почати', 35)

k2 = Label(150, 250,200, 70, RED)
k2.color(RED)
k2.set_text('Налаштування', 20)

k3 = Label(150, 350,80, 70, RED)
k3.color(RED)
k3.set_text('Скіни', 30)

k4 = Label(270, 350,80, 70, RED)
k4.color(RED)
k4.set_text('Вийти', 15)

record_text = Label(20, 90,80, 55, New)
record_text.color(New)
record_text.set_text('Рекорд:', 30)

ADR_text = Label(20, 140,80, 55, New)
ADR_text.color(New)
ADR_text.set_text('Средний пробег:', 30)

num_run_text = Label(20, 190,80, 55, New)
num_run_text.color(New)
num_run_text.set_text('Количество забегов:', 30)


######################################################################################################################################################################################


jazik=[
    'Україньска',
    'Polski',
    'English'
]
klas_for_zvyk={
    'ukr':[
        'вимкн',
        '10%',
        '20%',
        '30%',
        '40%',
        '50%',
        '60%',
        '70%',
        '80%',
        '90%',
        '100%'
    ],
    'eng':[
        'off',
        '10%',
        '20%',
        '30%',
        '40%',
        '50%',
        '60%',
        '70%',
        '80%',
        '90%',
        '100%'
    ],
    'pol':[
        'wył',
        '10%',
        '20%',
        '30%',
        '40%',
        '50%',
        '60%',
        '70%',
        '80%',
        '90%',
        '100%'
    ]
}

######################################################################################################################################################################################

loadint4 = pygame.transform.scale(pygame.image.load('loading_4.png'),(500,500)).convert()
a = 0
while a != 10:
    mw.blit(loadint4,(0,0))
    a+=1
    pygame.display.update()
    clock.tick(60)
 

jazikklas()
while not game_over:
    #--------------------------MENU-------------------------------    
    if switch==0:
        mw.fill(New)
        t = Label(50,50,100,50,New)
        t.set_text('Dino Chrome 2',70,RED)
        t.draw(-20,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                export()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                
                if k1.collidepoint(x,y):
                    switch = 1.1
                        
                elif k2.collidepoint(x,y):
                    switch = 2
                elif k3.collidepoint(x,y):
                    switch = 3
                elif k4.collidepoint(x,y):
                    game_over = True
                    mw.fill(white)
        if jazikn == 2:
            k1.draw(35,10)
        else:
            k1.draw(25,10)
        k1.outline(RED2,10) 
        if jazikn == 2:
            k2.draw(30,15)
        elif jazikn == 1:
            k2.draw(22,15)
        else:
            k2.draw(15,20)
        k2.outline(RED2,10) 
        k3.draw(10,20)
        k3.outline(RED2,10) 
        k4.draw(15,20)
        k4.outline(RED2,10) 
#--------------------------NASTROIKI-------------------------------               
    if switch == 2:
        mw.fill(New)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                export()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if exit.collidepoint(x,y):
                    if return_to_game:
                        switch=1.1
                        WIN_WIDTH=1280
                        WIN_HEIGHT=720
                        window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
                    else:
                        switch = 0
                if left5.collidepoint(x,y):
                        jazikn-=1
                        if jazikn == -1:
                            jazikn=2
                        jazikklas()
                elif right5.collidepoint(x,y):
                        jazikn+=1
                        if jazikn == 3:
                            jazikn=0
                        jazikklas()
                if left6.collidepoint(x,y):
                        if zvykn == 0:
                            break
                        zvykn-=1
                        
                        volume-=0.1
                elif right6.collidepoint(x,y):
                        if zvykn == 10:
                            break
                        zvykn+=1
                        volume+=0.1

        audio_ded.set_volume(volume)
        audio_jump.set_volume(volume)
        audio_point.set_volume(volume)
        pygame.mixer.music.set_volume(volume)
        

        jazikmen.set_text(jazik[jazikn],30)  
        left5.draw()
        right5.draw()
        if jazikn == 0:
            jazikmen.draw(5,0)      
        else:
            jazikmen.draw(30,0) 
        jaziknat.draw(10,0)    

        zvyka.set_text(klas_for_zvyk[language][zvykn],30)  
        left6.draw()
        right6.draw()
        zvyk.draw(40,0)      
        zvyka.draw(40,0)

        exit.draw()
        if jazikn == 0:
            nastr.draw()
        else:
            nastr.draw(30,0)
#--------------------------REKORDI-------------------------------    
    if switch == 3:
        mw.fill(New)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if True:
                    if exit.collidepoint(x,y):
                        switch=0
            if event.type == pygame.QUIT:
                game_over = True
                export()


        score_all = 0
        for i in score_list:
            score_all += i
        ADR_ = score_all/len(score_list) 

        if jazikn==0:
            record_text.set_text('Рекорд: '+str(record),35)
            ADR_text.set_text('Середній забіг: '+str(round(ADR_,2)),35)
            num_run_text.set_text('Кількість забігів: '+str(len(score_list)),35)
        if jazikn==1:
            record_text.set_text('Rekord: '+str(record),35)
            ADR_text.set_text('Przeciętny wyścig: '+str(round(ADR_,2)),35)
            num_run_text.set_text('Liczba wyścigów: '+str(len(score_list)),35)
        if jazikn==2:
            record_text.set_text('Record: '+str(record),35)
            ADR_text.set_text('Average race: '+str(round(ADR_,2)),35)
            num_run_text.set_text('Number of runs: '+str(len(score_list)),35) 

        ADR_text.draw()
        record_text.draw()
        num_run_text.draw()
        savess.draw()
        exit.draw()
    
#-----------------------START GAME----------------------------------
    if switch == 1.1:
        if adsdsd == 1:
            WIN_WIDTH=1280
            WIN_HEIGHT=720
            window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
            score = 0
            player.health = 3
            xforscore = -150
            speed = 1
            score_time = 0
            mw.fill(white)
            adsdsd +=1 
            game = 'animation'
            if not first_firts == 0:
                for i in cactus_list:
                    i.respawn()
                x_first = 1000
            first_firts += 1
                    

    
        if game == '':
            if score == 1000:
                meteor = Meteor()
                meteor = Meteor()
                meteor = Meteor()
                xforscore = -175
                point = 1000
            if score == 5000:
                meteor = Meteor()
            if score >= 10000:
                xforscore = -200
                point = 1000
                if score >= 100000:
                    xforscore = -225
            if score_time == 3:
                score += 1
                score_time = 0
                speed += 0.0005
            score_time +=1  
        for i in background_list:
            if game != 'animation' or not trasi:
                i.update()
        if game == 'animation':
            if trasi:
                background_f.update()
            meteor_first.update()
        for i in bird_list:
            i.update()
        for i in cactus_list:
            i.update()

        player.update()
        hp.update()
        if game != 'animation':
            for i in meteor_list:
                i.update()
        score_text.set_text(('Score: ' + str(score)), 35)
        score_text.draw(xforscore,0)
        if score%point == 0 and score != 0:
            audio_point.play()

        if eskape:
            esk_w = pygame.Rect((485, 130), (350, 500)) 
            pygame.draw.rect(mw, GRAY, esk_w)
            pygame.draw.rect(mw, grey_outline, esk_w, 10)

            resume.draw(40,15)

            resume.outline(New_outline,10) 

            mw.blit(pause,(560,160))

            settings.draw(30,10)
            settings.outline(New_outline,10) 
        
            exit_to_menu.draw(30,20)
            exit_to_menu.outline(New_outline,10)
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game = 'stop'
                            eskape = True  
                if event.type == pygame.QUIT:
                    game_over = True
                    export()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if eskape:
                        if resume.collidepoint(x,y):
                                game = ''
                                eskape = False 
                        elif settings.collidepoint(x,y):    
                            switch = 2
                            return_to_game = True
                            WIN_WIDTH=500
                            WIN_HEIGHT=500
                            mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
                        elif exit_to_menu.collidepoint(x,y):
                            adsdsd = 1
                            switch = 0
                            WIN_WIDTH=500
                            WIN_HEIGHT=500
                            mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
            

    pygame.display.update()
    clock.tick(FPS*speed)
 
