from pygame import *
from random import randint
# подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.SysFont("Arial", 80)
win1 = font1.render('PLAYER 1 WIN', False, (255, 255, 255))

win2 = font1.render('PLAYER 2 WIN', True, (255, 255, 255))

font2 = font.Font(None, 36)


# нам нужны такие картинки:
img_back = "sky.png" # фон игры
 
img_hero = "rocket.png" # герой
img_enemy = "ball.png" # враг
 
score = 0 # сбито кораблей
goal = 10 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 3 # проиграли, если пропустили столько
 
# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

speed_x = 5
speed_y = 5

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 40:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 40:
            self.rect.y += self.speed

class Enemy(GameSprite):
    # движение врага
    def update(self):
        global speed_x , speed_y
        self.rect.y += speed_y
        self.rect.x += speed_x
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height - 40 or self.rect.y < 0:
           speed_y *= -1


 
 
win_width = 700
win_height = 500
display.set_caption("Pin-Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ball = Enemy(img_enemy, 350, 250, 35, 35, 5)
rocket1 = Player(img_hero, 10, 250, 25, 50, 5)
rocket2 = Player(img_hero, 625, 250, 25, 50, 5)

finish = False
run = True 
while run:
    if ball.rect.x > 700 :
        window.blit(win1, (200,200))
        finish = True

    if ball.rect.x < 0:
        window.blit(win2, (200,200))
        finish = True
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
 

    if not finish:
        window.blit(background, (0,0))
        ball.reset()
        ball.update()
        rocket1.reset()
        rocket1.update1()
        rocket2.reset()
        rocket2.update2()
        display.update()







    time.delay(50)