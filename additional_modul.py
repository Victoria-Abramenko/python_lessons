# import pygame
#
# class Ball(pygame.sprite.Sprite):  # создаем класс для работы с падающими шариками наследуемый от класса Sprite
#     def __init__(self, x, speed, filename):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(filename).convert_alpha() # изображение спрайта
#         self.rect = self.image.get_rect(center = (x, 0))  # размер и положение спрайта
#         self.speed = speed
#
#     def update(self, *args, **kwargs): # переопределяем метод из базового класса - он отвечает за обновление спрайта (изменение его координат)
#         if self.rect.y < args[0] - 50: # первым параметром передадим высоту клиентского окна
#             self.rect.y += self.speed
#         else:
#             self.rect.y = 0

# модифицируем класс для случайных значений
# import pygame
#
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, x, speed, surf, group):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = surf
#         self.rect = self.image.get_rect(center = (x, 0))
#         self.speed = speed
#         self.add(group)  # добавляем этот шар в группу
#
#     def update(self, *args, **kwargs):
#         if self.rect.y < args[0] - 50:
#             self.rect.y += self.speed
#         else:
#             self.kill() # метод для исключения шара из группы, когда он достигнет земли
#
# import pygame
#
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, x, speed, surf, score, group):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = surf
#         self.rect = self.image.get_rect(center = (x, 0))
#         self.speed = speed
#         self.score = score
#         self.add(group)  # добавляем этот шар в группу
#
#     def update(self, *args, **kwargs):
#         if self.rect.y < args[0] - 50:
#             self.rect.y += self.speed
#         else:
#             self.kill()