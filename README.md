# PingPongfrom pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,):
        super().__init__()
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
win_wight = 700
win_height = 500

image = Surface((700,500))
image.fill((127, 255, 212))
rect = image.get_rect()

window = display.set_mode((700, 500))
display.set_caption('pinpong')

game = True
FPS = 60


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        
        if keys[K_DOWN] and self.rect.x < 700 - 80:
            self.rect.x += self.speed 

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        
        if keys[K_s] and self.rect.x < 700 - 80:
            self.rect.x += self.speed 

