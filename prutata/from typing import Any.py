from typing import Any
from pygame import*
from random import randint
Bullet_na_livo = 'Bullet_na_livo.png'
Bullet_na_pravo = 'Bullet_na_pravo.png'
fon_pon = 'fon_pon.jpg'
ohotnik_na_livo_img = 'ohotnik_na_livo.png'
ohotnik_na_pravo = 'ohotnik_na_pravo.png'
zombe_na_livo = 'zombe_na_livo.png'
zombe_na_pravo = 'zombe_na_pravo.png'
back = (fon_pon)
class GameSprite(sprite.Sprite): 
 
    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(size_x , size_y))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset (self):
        window.blit(self.image,(self.rect.x , self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
            self.left=True
            self.right= False

        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
            self.left=False
            self.right= True
    def fire(self):
        pass   
        bullet = Bullet('Bullet_na_livo.png', self.rect.x, self.rect.y, 15, 2, -15)
        bullets.add(bullet)
bullets = sprite.Group()
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

skore = 0
lost = 0
class Enemi_r(GameSprite):
    def update(self):
        self.rect.x += self.speed
        global lost 
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
class Enemi_l(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global lost 
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

win_width = 700 
win_height = 500 


zombes = sprite.Group()
for i in range(1, 5):
    zombe_l = Enemi_l(zombe_na_livo,randint(80,win_width -80), 10, 50, 50, randint(1, 5))
    zombes.add(zombe_l)
    zombe_r = Enemi_r(zombe_na_pravo,randint(80,win_width -80), 10, 50, 50, randint(1, 5))
    zombes.add(zombe_r)
finish = False 
game = True
            
def fire(self):  
        pass  
        Bullet_na_livo = Bullet("bullet_na_livo.png", self.rect.x, self.rect.y, 10, 10, -15 ) 
        bullets.add(Bullet_na_livo) 
 
class Bullet(GameSprite): 
    def update(self): 
        self.rect.y +=  self.speed 
        #зникає, якщо дійде до краю екрану 
        if self.rect.y < 0: 
            self.kill() 
bullets = sprite.Group()
score = 0  
 
lost = 0  
class Enemy(GameSprite):  
    def update(self):  
        self.rect.y += self.speed  
        global lost   
  
        if self.rect.y > win_height:  
            self.rect.x = randint(5, win_width - 8)  
            self.rect.y = 0  
            lost = lost + 1  
#лічильник збитих і пропущ

window = display.set_mode((win_width, win_height))
display.set_caption("Shooter Game")
background = transform.scale(image.load("fon_pon.jpg"),(win_width, win_height))





FPS = 60
clock = time.Clock()
finish = False  


run = True  
ohotnik_na_livo = Player(ohotnik_na_livo_img, 0,  0, 50, 50, 20)
  
while run:  
  
      
    for e in event.get():  
        if e.type == QUIT:  
            run = False  
        #подія натискання на пробіл - спрайт стріляє 
        elif e.type == KEYDOWN: 
            if e.key == K_SPACE: 
                ohotnik_na_livo.fire() 
    if not finish:  

        window.blit(background, (0, 0)) 
        zombes.draw(window)
        zombes.update()
        ohotnik_na_livo.reset()

    display.update()
    clock.tick(FPS)