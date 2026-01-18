import pygame
from projectile import Projectile
import animation
pygame.init()

# creer une premiere classe qui va representer notre jouer
class Player(animation.AnimateSprite):

    def __init__(self, game):
        self.game = game
        super().__init__('player')
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
           self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectlie(self):
        # creer une nouvelle instance de la classe Projectile
        self.all_projectles.add(Projectile(self))
        # demarrer l'animation du lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
           self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity