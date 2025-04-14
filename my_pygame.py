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


# # __________  обработка событий клавиатуры  _________________________
# # event.type == pygame.KEYDOWN  -  клавиша нажата
# # event.type == pygame.KEYUP  -  клавиша отпущена
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# x = W // 2
# y = H // 2
# speed = 20
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#         elif event.type == pygame.KEYDOWN:  # обработка событий нажатия клавиатуры
#             if event.key == pygame.K_LEFT: # нажатие влево, смешаем по оси X влево
#                 x -= speed
#             elif event.key == pygame.K_RIGHT:  # нажатие вправо, смешаем по оси X вправо
#                 x += speed
#             elif event.key == pygame.K_UP:  # нажатие вверх, смешаем по оси X вверх
#                 y -= speed
#             elif event.key == pygame.K_DOWN:  # нажатие вниз, смешаем по оси X вниз
#                 y += speed
#
#     sc.fill(BLUE)  # заливка поверхности определенным цветом
#     pygame.draw.rect(sc, GREEN, (x, y, 50, 50))
#     pygame.display.update()
#     clock.tick(FPS)
#
# # чтобы добавить перемещение при зажатой клавише, необходимо сделать так, чтобы событие попадало в обработку событий
# # до тех пор, пока клавиша удерживается нажатой
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# x = W // 2
# y = H // 2
# speed = 10
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
#
# fl_left = fl_right = fl_up = fl_down = False  # создаем флаг, которой при не нажатой клавише имеет значение False
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 fl_left = True  #  при нажатой клавише, значение флага будет True
#             elif event.key == pygame.K_RIGHT:
#                 fl_right = True
#             elif event.key == pygame.K_UP:
#                 fl_up = True
#             elif event.key == pygame.K_DOWN:
#                 fl_down = True
#
#         elif event.type == pygame.KEYUP:  # создаем проверку, чтобы изменить значение флага при отпускании клавиши
#             if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
#                 fl_left = fl_right = fl_up = fl_down = False
#
#     # по этим флагам будем менять значение координаты
#     if fl_left:
#         x -= speed
#     elif fl_right:
#         x += speed
#     elif fl_up:
#         y -= speed
#     elif fl_down:
#         y += speed
#
#
#
#     sc.fill(BLUE)  # заливка поверхности определенным цветом
#     pygame.draw.rect(sc, GREEN, (x, y, 50, 50))
#     pygame.display.update()
#     clock.tick(FPS)
#
# # в pygame есть модуль key, в котором есть метод get_pressed(), который возвращает состояние клавиш в виде кортежа
# # pygame.K_RIGHT  - это константы, у каждой из которых есть свой индекс и по нему и определяется какая клавиша нажата (0, 0, 1, 0 ...)
# # при помощи него можно реализовать данный функционал гораздо проще
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# x = W // 2
# y = H // 2
# speed = 10
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     keys = pygame.key.get_pressed()  # получаем коллекцию нажатых клавиш
#
#     if keys[pygame.K_LEFT]: # если нажата влево - смещаемся влево
#         x -= speed
#     elif keys[pygame.K_RIGHT]:
#         x += speed
#     elif keys[pygame.K_UP]:
#         y -= speed
#     elif keys[pygame.K_DOWN]:
#         y += speed
#
#
#     sc.fill(BLUE)
#     pygame.draw.rect(sc, GREEN, (x, y, 50, 50))
#     pygame.display.update()
#     clock.tick(FPS)
#
# # но у этой функции нет идентификаторов для ctrl, shift, alt...
# поэтому с ними необходимо использовать первый вариант

# # ____________________  обработка событий от мышки ________________________
# # pygame.MOUSEBUTTONDOWN - нажатие на кнопку мыши
# # pygame.MOUSEBUTTONUP - отпускание кнопки мыши
# # pygame.MOUSEBUTTONMOTION - перемещение курсора
# # pygame.MOUSEBUTTONWHEEL - вращения колесиком
# # .MOUSEBUTTONDOWN
# # event.button : чтобы отследить кнопку мыши
# # 1 - нажатие левой клавиши мыши
# # 2 - нажатие средней клавиши мыши
# # 3 - нажатие правой клавиши мыши
# # 4 - вращение колесика вперед
# # 5 - вращение колесика назад
# # .MOUSEBUTTONMOTION
# # event.pos : чтобы отследить позицию курсора - абсолютная позиция (относительно экрана)
# # event.rel : относительная позиция (относительно предыдущей позиции)
#
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# x = W // 2
# y = H // 2
# speed = 10
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# PINK = (242, 76, 90)
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print('мышка нажата', event.button)
#         elif event.type == pygame.MOUSEMOTION:
#             print('координаты курсора', event.rel)
#
#     sc.fill(BLUE)
#     pygame.draw.rect(sc, GREEN, (x, y, 50, 50))
#     pygame.display.update()
#     clock.tick(FPS)
# # ...
# # координаты курсора (-1, -3)
# # координаты курсора (-1, -2)
# # мышка нажата 3
# # мышка нажата 2
# # координаты курсора (1, 0)
# # ...
#
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# x = W // 2
# y = H // 2
# speed = 10
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# PINK = (242, 76, 90)
#
# fl_start_draw = False # флаг для рисования
# sp = ep = None # начальная и конечная координаты рисуемого прямоугольника
#
# sc.fill(BLUE)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # отслеживаем нажатие левой кнопки мыши
#             fl_start_draw = True  # флаг рисования изменяем на истина
#             sp = event.pos  # начальная координата равна текущей позиции
#
#         elif event.type == pygame.MOUSEMOTION:  # обрабатываем перемещение курсора
#             if fl_start_draw:  # Если флаг True
#                 pos = event.pos
#
#                 width = pos[0] - sp[0]
#                 height = pos[1] - sp[1]
#
#                 sc.fill(BLUE)  # снова закрашиваем клиентскую область, чтобы стереть предыдущий прямоугольник
#                 pygame.draw.rect(sc, PINK, (sp[0], sp[1], width, height)) # рисуем прямоугольник заданной ширины
#                 pygame.display.update()
#
#         elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # отслеживание отпускания кнопки
#             fl_start_draw = False # снова изменяем значение на False
#
#     clock.tick(FPS)
#
# # в комментариях предложен способ для отрисовывания и в отрицательную сторону

# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# x = W // 2
# y = H // 2
# speed = 10
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# PINK = (242, 76, 90)
#
# fl_start_draw = False
# sp = ep = None
#
# sc.fill(BLUE)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             fl_start_draw = True
#             sp = event.pos
#
#         elif event.type == pygame.MOUSEMOTION:
#             if fl_start_draw:
#                 pos = event.pos
#
#                 x, y = min(sp[0], pos[0]), min(sp[1], pos[1])
#
#                 width = max(pos[0], sp[0]) - x
#                 height = max(pos[1], sp[1]) - y
#
#                 sc.fill(BLUE)
#                 pygame.draw.rect(sc, PINK, (x,y, width, height))
#                 pygame.display.update()
#
#         elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#             fl_start_draw = False
#
#     clock.tick(FPS)

# # в pygame есть специальный модуль mouse - для отслеживаний событий мышки, метод get_pressed, она возвращает кортеж,
# # какие кнопки нажаты (1, 0, 0)
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# x = W // 2
# y = H // 2
# speed = 10
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# PINK = (242, 76, 90)
#
#
# sp = None
#
# sc.fill(BLUE)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     pressed = pygame.mouse.get_pressed()
#     if pressed[0]:  # нажата ли левая кнопка мыши - индекс 0
#         pos = pygame.mouse.get_pos()  # получает текущую позицию курсора
#
#         if sp is None: # значит мы еще не начали рисовать прямоугольник, а текущая позиция будет начальной
#             sp = pos
#         x, y = min(sp[0], pos[0]), min(sp[1], pos[1])
#
#         width = max(pos[0], sp[0]) - x
#         height = max(pos[1], sp[1]) - y
#
#         sc.fill(BLUE)
#         pygame.draw.rect(sc, PINK, (x,y, width, height))
#         pygame.display.update()
#     else: # сработает как только кнопка мыши будет отпущена
#         sp = None
#
#     clock.tick(FPS)

# в модуле mouse есть специальные функции?
# set_visible со значением False скроет курсор мыши

# # ____________  поверхности в pygame  _________________
# # клиентская область - базовая поверхность .set_mode((width, height))
# # поверхность - .Surface((width, height)), чтобы ее закрасить также используется метод fill(color), а чтобы отобразить
# # эту поверхность в клиентской области, используется метод blit(), к той переменной, которой была присвоена поверхность,
# # в качестве параметров передаются - поверхность и координаты, где ее расположить.
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
#
# sc.fill(BLUE)
#
# surf = pygame.Surface((200, 200))
# surf.fill(GREEN)
# sc.blit(surf, (50, 50))
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)
#
# # метод set_alpha задает степень прозрачности от 0 - 255 (прозрачная - непрозрачная)

# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# sc.fill(BLUE)
#
# surf = pygame.Surface((200, 200))
# surf.fill(GREEN)
#
# surf_alpha = pygame.Surface((W, 100))
# pygame.draw.circle(surf_alpha, RED,(100, 100), 80)
# surf_alpha.set_alpha(128)
# surf.blit(surf_alpha, (0, 50))
# sc.blit(surf, (50, 50))
#
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)

# # пример анимации поверхности
# import pygame
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# sc.fill(BLUE)
#
# surf = pygame.Surface((W, 200))
# bita = pygame.Surface((50, 10))
#
# surf.fill(GREEN)
# bita.fill(RED)
#
# bx, by = 0, 150 # положение биты
# x, y = 0, 0 # положение поверхности
#
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     surf.fill(GREEN)  # закрашиваем поверхность
#     surf.blit(bita, (bx, by))  # наносим на поверхность другую поверхность
#
#     if bx < W:
#         bx += 5
#     else:
#         bx = 0
#
#     if y < H:
#         y += 1
#     else:
#         y = 0
#
#     sc.fill(BLUE)
#     sc.blit(surf, (x, y))
#     pygame.display.update()
#
#     clock.tick(FPS)

# # _____________прямоугольная область Rect - это класс для обработки границ и столкновений, а не для рисования ______
# import pygame
#
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# hero = pygame.Surface((40, 50)) # создаем поверхность персонажа ширина 40px, высота 50px
# hero.fill(GREEN)
# rect = hero.get_rect()  # этот метод возвращает прямоугольник, который занимает эта поверхность
# print(rect)
#
# sc.fill(BLUE)
# sc.blit(hero, (100, 50))
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)
#
# #  у экземпляров класса Rect есть определенные свойства - координаты верхнего левого угла, а также точки углов и
# #  середин всех граней прямоугольника
# # (x, y)  |  top  |  topright
# # left  |  center  |  right
# # bottomleft  |  bottom  | bottomright
# # можно методу get_rect() задать координаты topleft=(200, 50), по умолчанию (0, 0)
# # import pygame
# #
# # pygame.init()
# #
# # W,H = 600, 400
# # sc = pygame.display.set_mode((W, H))
# # FPS = 60
# # clock = pygame.time.Clock()
# #
# # GREEN = (35, 41, 26)
# # BLUE = (54, 158, 180)
# # RED = (250, 100, 190)
# #
# # hero = pygame.Surface((40, 50)) #
# # hero.fill(GREEN)
# # # rect = hero.get_rect(topleft=(200, 50))
# # rect = hero.get_rect(center=( W // 2, H // 2)) # разместить этот прямоугольник по центру окна
# # print(rect)
# #
# # sc.fill(BLUE)
# # sc.blit(hero, rect)  # здесь уже не координаты, а полученный прямоугольник передаем в параметрах для позиционирования
# # pygame.display.update()
# #
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             exit()
# #
# #     clock.tick(FPS)
#
# # В классе Rect есть специальные методы
# # Rect.move(x, y) - возвращает новый прямоугольник со смещениями x, y
# # Rect.move_ip(x, y) - меняет координаты текущего прямоугольника со смещениями x, y
# # Rect.clip(Rect) - обрезает границы прямоугольника по указанным размерам переданного прямоугольника
# # Rect.union(Rect) - возвращает новый прямоугольник с результатами объединения двух прямоугольников
# # Rect.union_ip - объединяет два прямоугольника в один, меняет в текущем прямоугольнике
# # Rect.fit(Rect) - возвращает новый прямоугольник смещенный и обрезанный по размеру переданного прямоугольника
# # Rect.contains(Rect) - проверяет, содержится ли один прямоугольник внутри другого
# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# rect1 = pygame.Rect((0, 0, 30, 30))
# rect2 = pygame.Rect((30, 30, 30, 30))
#
# rect2.move_ip(20, 20)
# print(rect2)  # <rect(50, 50, 30, 30)>
# rect3 = rect2.union(rect1)
# print(rect3)  # <rect(0, 0, 80, 80)>
#
# sc.fill(BLUE)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)

# # имитация прыжка героя
# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# ground = H - 70 # уровень земли
# jump_force = 20  # сила прыжка
# move = jump_force +  1  # текущая вертикальная скорость
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# hero = pygame.Surface((40, 50)) #
# hero.fill(GREEN)
# rect = hero.get_rect(centerx=W // 2) # разместить этого персонажа по центру окна по x
# rect.bottom = ground # размещаем героя на поверхности земли
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and ground == rect.bottom:
#                 move = -jump_force
#
#     if move <= jump_force:
#         if rect.bottom + move < ground:
#             rect.bottom += move
#             if move < jump_force:
#                 move += 1  # замедление скорости прыжка
#         else:
#             rect.bottom = ground
#             move = jump_force + 1
#
#     sc.fill(BLUE)
#     sc.blit(hero, rect)
#     pygame.display.update()
#
#
#     clock.tick(FPS)
#
# #____________________ текст и шрифты. pygame.font ___________
# # для этого в pygame используется модуль font, в котором определены некоторые свойства и функции:
# # SysFont(имя шрифта, размер) - класс для предустановленного шрифта
# # Font(путь, размер) - класс для загрузки шрифта по указанному пути
# # get_fonts() - функция возвращающая имена предустановленных в системе шрифтов - коллекцию
# # match_font(имя шрифта) - функция возвращающая путь к шрифту по его имени
# import pygame
#
# pygame.init()
#
# print(pygame.font.get_fonts())
# # ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', 'comicsansms', 'consolas',
# # 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact',
# # 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic',
# # 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhenghei', 'microsoftjhengheiui', 'microsoftnewtailue',
# # 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyahei', 'microsoftyaheiui', 'microsoftyibaiti',
# # 'mingliuextb', 'pmingliuextb', 'mingliuhkscsextb', 'mongolianbaiti', 'msgothic', 'msuigothic', 'mspgothic', 'mvboli',
# # 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'sansserifcollection', 'segoefluenticons',
# # 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric',
# # 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'segoeuivariable', 'simsun', 'nsimsun', 'simsunextb',
# # 'sitkatext', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings',
# # 'yugothic', 'yugothicuisemibold', 'yugothicui', 'yugothicmedium', 'yugothicuiregular', 'yugothicregular',
# # 'yugothicuisemilight', 'holomdl2assets']
#
# import pygame
#
# pygame.init()
#
# f_sys = pygame.font.SysFont('tahoma', 20)
# # my_font = pygame.font.Font('font/comic.ttf', 25)  # чтобы установить свой шрифт

# # для подключаемых шрифтов
# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# f_sys = pygame.font.Font('fonts/tahoma.ttf', 20) # создаем ссылку на класс font
# text = f_sys.render('Text in the window', 1, GREEN, BLUE)  # формируется поверхность, на которой пишется текст,
# # 1 - значит текст сглаженный, цвет текста, цвет фона
# text_pos = text.get_rect(center=(W // 2, H // 2)) # отображение поверхности с текстом
#
# sc.fill(RED)
# sc.blit(text, text_pos)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)

# # если необходимо отобразить стандартный текст
# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# f_sys = pygame.font.SysFont('tahoma', 20)
# text = f_sys.render('Text in the window', 1, GREEN, BLUE)
# text_pos = text.get_rect(center=(W // 2, H // 2))
#
# sc.fill(RED)
# sc.blit(text, text_pos)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)

# # пример перемещения текста зависимо от мышки
# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# f_sys = pygame.font.SysFont('tahoma', 20)
# text = f_sys.render('Text in the window', 1, GREEN, BLUE)
# text_pos = text.get_rect(center=(W // 2, H // 2))
#
# def draw_text():
#     sc.fill(RED)
#     sc.blit(text, text_pos)
#     pygame.display.update()
#
# draw_text()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             pygame.mouse.get_rel()  # обнуляем первое смещение  (при повторном вызове ниже)
#
#     if pygame.mouse.get_focused() and text_pos.collidepoint(pygame.mouse.get_pos()):
#         btns = pygame.mouse.get_pressed()
#         if btns[0]:  # нажата левая кнопка мыши
#             rel = pygame.mouse.get_rel()  # получаем позицию смещения
#             text_pos.move_ip(rel)
#             draw_text()
#
#     clock.tick(FPS)

# _____________________   работа с изображениями в pygame   ________________
# родной формат графических изображений - bmp (несжатые пиксели - занимают много места)
# png - сжатие без потерь
# jpg - сжатие с потерями
# чтобы проверить, поддерживает ли на данном устройстве pygame другие форматы, используется функция get_extended()
# возвращает True / False
# для фотореалистичных изображений используется jpg
# png для изображений без фона, для однотонных областей

# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# print(pygame.image.get_extended())
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#
#     clock.tick(FPS)
# # True

# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# ufo_surf = pygame.image.load('img/ufo.JPG')  # загрузка изображения, возвращает поверхность, на которой отображено это изображение
# ufo_rect = ufo_surf.get_rect(center=(W // 2, H // 2))  # располагаем по центру экрана
#
# sky_surf = pygame.image.load('img/sky.JPG')
# sc.blit(sky_surf, (0, 0))
#
# sc.blit(ufo_surf, ufo_rect)  # отобразить изображение в клиентском окне
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)

# # в pygame можно задать белый цвет прозрачным при помощи set_colorkey((255, 255, 255))
# import pygame
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# ufo_surf = pygame.image.load('img/ufo.JPG').convert_alpha() # конвертация изображения в стандартный формат (alfa, так как используется прозрачность)
# sky_surf = pygame.image.load('img/sky.JPG').convert()
#
# ufo_rect = ufo_surf.get_rect(center=(W // 2, H // 2))
# ufo_surf.set_colorkey((255, 255, 255))  # указываем цвет, который сделать прозрачным
#
# sc.blit(sky_surf, (0, 0))  # blit преобразует пиксели перед тем, как отобразит на поверхности, чтобы сэкономить
# # время на конвертацию, можно провести ее сразу при загрузке изображения
# sc.blit(ufo_surf, ufo_rect)
# pygame.display.update()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(FPS)
#
# # для работы над изображением - его трансформации, используется модуль transform
# # масштабирование transform.scale(поверхность, (желаемая ширина, высота)) - возвращает новую отмасштабированную поверхность
# import pygame
# from pygame import K_LEFT, K_RIGHT, K_DOWN
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# ufo_surf = pygame.image.load('img/ufo.JPG').convert_alpha()
# sky_surf = pygame.image.load('img/sky.JPG').convert()
#
# ufo_surf.set_colorkey((255, 255, 255))
#
# # отрисуем изображение в разных ракурсах, использую вращение
# ufo_up = ufo_surf
# ufo_down = pygame.transform.flip(ufo_surf, 0, 1) # отзеркаливание по y
# ufo_left = pygame.transform.rotate(ufo_surf, 90)
# ufo_right = pygame.transform.rotate(ufo_surf, -90)
#
#
# ufo_surf = pygame.transform.scale(ufo_surf, (ufo_surf.get_width() // 3, ufo_surf.get_height() // 3)) # уменьшим изображение в 3 раза
#
# ufo_rect = ufo_surf.get_rect(center=(W // 2, H // 2))
#
#
# ufo = ufo_up  # текущее изображение персонажа - по умолчанию вверх
# speed = 10
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     bt = pygame.key.get_pressed()
#     if bt[pygame.K_LEFT]:
#         ufo = ufo_left  # используем изображение персонажа повернутого влево
#         ufo_rect.x -= speed  # смещаем по оси x на значение скорости
#         if ufo_rect.x < 0:  # чтобы персонаж не выходил за пределы окна
#             ufo_rect.x = 0
#
#     elif bt[pygame.K_RIGHT]:
#         ufo = ufo_right
#         ufo_rect.x += speed
#         if ufo_rect.x > W - ufo_rect.width:
#             ufo_rect.x = W - ufo_rect.width
#
#     elif bt[pygame.K_UP]:
#         ufo = ufo_up
#         ufo_rect.y -= speed
#         if ufo_rect.y < 0:
#             ufo_rect.y = 0
#
#     elif bt[pygame.K_DOWN]:
#         ufo = ufo_up
#         ufo_rect.y += speed
#         if ufo_rect.y > H - ufo_rect.height:
#             ufo_rect.y = H - ufo_rect.height
#
#     sc.blit(sky_surf, (0, 0))
#     sc.blit(ufo_surf, ufo_rect)
#
#     pygame.display.update()
#
#     clock.tick(FPS)

# ___________  спрайты - sprite  _____________________
# спрайт - любой подвижный объект. pygame.sprite ветка для работы с подвижными объектами
# для создания класса таких объектов используется класс Sprite модуля sprite
# создадим такой класс в отдельном модуле
# import pygame
# from additional_modul import Ball # подключаем созданный модуль
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# bg = pygame.image.load('img/sky.JPG')
#
# speed = 2
# # создаем экземпляр класса
# b1 = Ball(W // 2, speed, 'img/ball.png')  # передаем расположение по иксу и путь к файлу
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     sc.blit(bg, (0, 0))
#     sc.blit(b1.image, b1.rect)
#     pygame.display.update()
#
#     clock.tick(FPS)
#
#     # if b1.rect.y < H - 50:  # создаем эффект падения мяча, но реализовывать логику падения в главном цикле - плохая практика, лучше реализовать ее в классе (в модуле)
#     #     b1.rect.y += speed
#     # else:
#     #     b1.rect.y = 0
#
#     b1.update(H)

# # работа с несколькими спрайтами
# import pygame
# from additional_modul import Ball # подключаем созданный модуль
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# bg = pygame.image.load('img/sky.JPG')
#
# speed = 2
# # создаем экземпляр класса
# b1 = Ball(W // 2, speed, 'img/ball.png')  # передаем расположение по иксу и путь к файлу
# b2 = Ball(W // 2 - 250, 3, 'img/ball.png')
# b3 = Ball(W // 2 + 100, 4, 'img/ball.png')
#
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     sc.blit(bg, (0, 0))
#     sc.blit(b1.image, b1.rect)
#     sc.blit(b2.image, b2.rect)
#     sc.blit(b3.image, b3.rect)
#     pygame.display.update()
#
#     clock.tick(FPS)
#
#     b1.update(H)
#     b2.update(H)
#     b3.update(H)
#
# # чтобы избежать дублирование кода - спрайты объединяют в группу и обрабатывают единым образом - при помощи класса Group()
# import pygame
# from additional_modul import Ball
#
# pygame.init()
#
# W,H = 600, 400
# sc = pygame.display.set_mode((W, H))
# FPS = 60
# clock = pygame.time.Clock()
#
# bg = pygame.image.load('img/sky.JPG')
#
# speed = 2
# balls = pygame.sprite.Group() # создаем группу
# # # 1 способ - добавлять в группу по 1 шару
# # balls.add(Ball(W // 2, speed, 'img/ball.png'))
# # balls.add(Ball(W // 2 - 250, 3, 'img/ball.png'))
# # balls.add(Ball(W // 2 + 100, 4, 'img/ball.png'))
# # # 2 способ - указать все шары через запятую
# balls.add(Ball(W // 2, speed, 'img/ball.png'),
#           Ball(W // 2 - 250, 3, 'img/ball.png'),
#           Ball(W // 2 + 100, 4, 'img/ball.png'))
#
#
# GREEN = (35, 41, 26)
# BLUE = (54, 158, 180)
# RED = (250, 100, 190)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     sc.blit(bg, (0, 0))
#     balls.draw(sc) # вместо blit вызываем метод draw для группы и указываем плоскость
#     pygame.display.update()
#
#     clock.tick(FPS)
#
#     balls.update(H)  # метод также вызывается для группы

# изменим игру, сделаем так, чтобы шары появлялись каждые 2 секунды
import pygame
from additional_modul import Ball
from random import randint

pygame.init()

W,H = 600, 400
sc = pygame.display.set_mode((W, H))
FPS = 60
clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 2000) # создаем функцию, которая каждые 2000 миллисекунд (2 сек) будет генерировать событие USEREVENT

balls_images = ['ball_1.png', 'ball_2.png', 'ball_3.png'] # создаем коллекцию названий изображений шаров
balls_surf = [pygame.image.load('img/' + path).convert_alpha() for path in balls_images]# загружаем эти изображения при помощи генератора списка

def createBall(group): # создаем вспомогательную функцию, которая будет создавать новый шар со случайными значениями
    indx = randint(0, len(balls_surf) - 1)
    x = randint(20, W - 50)
    speed = randint(1, 4)
    
    return Ball(x, speed, balls_surf[indx], group)

bg = pygame.image.load('img/sky.JPG')

speed = 2
balls = pygame.sprite.Group()


GREEN = (35, 41, 26)
BLUE = (54, 158, 180)
RED = (250, 100, 190)

createBall(balls) # для создания первого шара

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.USEREVENT: # как только появилось это событие (каждые 2 сек)
            createBall(balls) # будет генерироваться новый мяч


    sc.blit(bg, (0, 0))
    balls.draw(sc)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)

