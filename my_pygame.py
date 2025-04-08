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
