# # _________  pygame  _____________
# # библиотека для манипуляции графическими объектами
# # ее возможности:
# # - рисование графических объектов
# # - отслеживание различных событий (таймер, нажатие клавиатуры, мышки...)
# # - отслеживание изменений состояний объектов (создание анимации, контроль столкновений)
# # - быстрая отрисовка изменений на экране устройства пользователя
# # - работа со звуковыми эффектами
# # но в ней нет готовой обработки физических явлений и ракурсов камеры, так что полноценным игровым движком не является
# # ее необходимо установить при помощи команды pip install pygame, а затем импортировать
#
# import pygame
# pygame.init()  # импортирует все необходимые функции
#
# pygame.display.set_mode((600, 400))  # создает окно кортеж (по горизонтали, по вертикали) размеры окна в пикселях
#
# # чтобы окно не закрывалось необходимо создать главный цикл обработки событий
# while 1:  # бесконечный цикл
#     for event in pygame.event.get():  # отлавливает все события
#         if event.type == pygame.QUIT:  # если событие == выход из программы
#             exit() # выйти из приложения (но после исполнения этой функции - ничего выполняться не будет)

# # используется pygame.quit() если необходимо после завершения выполнить еще какой-то код
# import pygame
# pygame.init()
#
# pygame.display.set_mode((600, 400))
#
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()  # не завершает цикл(завершает pygame.init) поэтому возникает ошибка pygame.error:
#             # video system not initialized
#
# # чтобы все корректно работало необходимо цикл сделать не бесконечным
# import pygame
# pygame.init()
#
# pygame.display.set_mode((600, 400))
#
# flag_running = True
# while flag_running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             flag_running = False
#
# print('Программа завершилась с последующей обработкой кода') # Программа завершилась с последующей обработкой кода -
# # этот код выполнился после закрытия окна

# # главный цикл работает очень быстро, каждые миллисекунды он проверяет на какое-либо событие, обычно вполне достаточно
# # 60 кадров в секунду (для динамических игр 1 / 60 сек = 17 миллисекунд, для статических 1 / 30 сек = 34 миллисекунд)
# # есть 2 способа установить задержку
# # 1 - delay(миллисекунд) - напрямую установить задержку # но скорость будет разной на разных процессорах
# import pygame
# pygame.init()
#
# pygame.display.set_mode((600, 400))
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     pygame.time.delay(20) # задержка следующей итерации цикла на 20 мс
#     # но скорость будет разной на разных процессорах

# # 2 способ - при помощи специального класса Clock и его метода tick
# import pygame
# pygame.init()
#
# pygame.display.set_mode((600, 400))
#
# clock = pygame.time.Clock()
# FPS = 60
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS) # число кадров в секунду английское сокращение FPS - переменную часто именно так и называют

# # переименовать окно программы мы жно при помощи функции set_caption
# import pygame
#
# pygame.init()
#
# pygame.display.set_mode((600, 400))
# pygame.display.set_caption('Моя игра')
#
# clock = pygame.time.Clock()
# FPS = 60
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)

# # можно поменять и иконку set_icon
# import pygame
#
# pygame.init()
#
# pygame.display.set_mode((600, 400))
# pygame.display.set_caption('Моя игра')
# pygame.display.set_icon(pygame.image.load('ufo.JPG'))
#
#
# clock = pygame.time.Clock()
# FPS = 60
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)