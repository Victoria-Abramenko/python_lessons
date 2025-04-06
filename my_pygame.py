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

# # _____ рисование графических примитивов _________
# # pygame.draw.rect(surface,...) - рисование прямоугольника
# # pygame.draw.line(surface,...) - рисование линии
# # pygame.draw.aaline(surface,...) - рисование сглаженной линии
# # pygame.draw.lines(surface,...) - рисование ломанной линии
# # pygame.draw.aalines(surface,...) - рисование ломанной сглаженной линии
# # pygame.draw.circle(surface,...) - рисование окружности
# # pygame.draw.ellipse(surface,...) - рисование эллипса
# # pygame.draw.arc(surface,...) - рисование дуги
#
# # направление осей x вправо y вниз
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
#
# pygame.draw.rect(sc,(252, 125, 155), (10, 10, 50, 100)) # поверхность, цвет, размеры прямоугольника (x, y, width, height)
# # но прямоугольника не будет видно, так как он рисуется на задней поверхности плоскости, поэтому ее необходимо перевернуть
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
# # отрисовка происходит на задней стороне поверхности для того, чтобы визуально пользователь не видел отображения отрисовки,
# # в случае анимации
# # есть метод update он перерисовывает только ту область, которая указана в нем, если не указано - то вся клиентская область
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
#
# pygame.draw.rect(sc,(252, 125, 155), (10, 10, 50, 100), 2) # если добавить еще 1 параметр, это будет толщина обводки
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
# # цвет также принято указывать в виде константы
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
#
# PINK = (252, 125, 155)
# BLUE = (2, 4, 250)
# GREEN = (4, 245, 4)
# RED = (250, 8, 16)
# COP = (35, 41, 26)
#
# pygame.draw.rect(sc, PINK, (10, 10, 50, 100), 2)
# pygame.draw.ellipse(sc, BLUE, (150, 150, 200, 300), 4)
# pygame.draw.line(sc, GREEN, (120, 50), (180, 240), 5) # можно задать толщину
# pygame.draw.aaline(sc, GREEN, (70, 40), (130, 230), 5) # начальные и конечные координаты, толщина будет не более 1px
# pygame.draw.aalines(sc, RED, True, [(250, 60), (290, 90), (320, 70)], 3)
# pygame.draw.lines(sc, RED, False, [(250, 120), (290, 140), (320, 120)], 3)
# pygame.draw.polygon(sc, COP, [[420, 250], [400, 240], [430, 260], [410, 220], [450, 230]])
# pygame.draw.polygon(sc, COP, [[320, 250], [300, 240], [330, 260], [310, 220], [350, 230]], 3)
# pygame.draw.circle(sc, PINK, (500, 300), 40)
# pi = 3.14
# pygame.draw.arc(sc, BLUE, (450, 30, 50, 150), pi, 2 * pi, 5)  # прямоугольник в пределах которого рисуется, начальный угол, конечный угол, толщина
#
#
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()