from pygame import *
from assets import *
from random import randint


mixer.init()
mixer.music.load(GAME_MUSIC)
mixer.music.play(-1)
fire_sound = mixer.Sound(FIRE_SOUND)
damage_sound = mixer.Sound(DAMAGE_SOUND)


img_back = GAME_BG_IMG
img_hero = ROCKET_IMG
img_enemy = ENEMY_IMG


font.init()
font2 = font.Font(None,36)
font1 = font.Font(None,80)
win = font1.render("YOU WIN",True,(255,255,255))
lose = font1.render("YOU LOSE!",True,(180,0,0))
score = 0 
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 


    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def fire(self):
        pass
class Enemy(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global lost
        if self.rect.y >win_width:
            self.rect.x = randint(80,win_width -80)
            self.rect.y = 0 
            lost = lost - 1

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load(img_back),(win_width,win_height))

ship = Player(img_hero,5,win_height - 100,80,100,10)
monsters = sprite.Group()
for i in range (1,6):
    monster = Enemy(img_enemy,randint(200,700), randint(-15,700),80,50,randint(1,5))
    monsters.add(monster)


finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run == False

    if not finish:
        window.blit(background,(0,0))
        text = font2.render("Рахунок:"+str(score),1,(255,255,255))
        window.blit(text,(10,20))
        text_lose = font2.render("Пропущено:"+str(lost),1,(255,255,255))
        window.blit(text_lose,(10,50))
        ship.update()
        monsters.update()
        ship.reset()
        monsters.draw(window)
        display.update()
    time.delay(50)