# # Алгоритм Кнута-Морриса-Пратта (КМП-алгоритм)
# # используется для нахождения подстроки в строке.
# # поиск сдвигается не по одному символу (прямой поиск), и не полностью от несовпавшего символа, а по максимальному префиксу.
# # в 1 этапе формируется массив (для сдвига по префиксам)
# # 2 этап поиск образа в строкеS
# # 1 формирование массива
# original_str = 'лилиласьлилилось лииллииллилилось'
# my_str = 'лииллиил' # подстрока
# p = [0] * len(my_str) # длина массива равна длине подстроки
# j = 0 # 1 счетчик
# i = 1 # 2 счетчик
#
# while i < len(my_str): # пока счетчик меньше длины образца
#     if my_str[j] == my_str[i]:
#         p[i] = j + 1
#         i += 1
#         j += 1
#
#     else:
#         if j == 0:
#             p[i] = 0
#             i += 1
#
#         else:
#             j = p[j - 1]
#
# print(p)  # [0, 0, 0, 1, 1, 2, 3, 4]
# # поиск образа в строке
# m = len(my_str)  # длина образца
# n = len(original_str)  # длина строки, в которой будем искать
#
# i = 0  # снова два счетчика
# j = 0
#
# while i < n: # пока не прошли строку до конца
#     if original_str[i] == my_str[j]:
#         i += 1
#         j += 1
#         if j == m:
#             print('Образ найден')
#             break
#     else:
#         if j > 0:
#             j = p[j - 1]
#         else:
#             i += 1
# if i == n:
#     print('Образ не найден')
# # Образ найден

# # _________   Алгоритм Дейкстры  ________
# # для нахождения наиболее короткого маршрута - вершин графа. Например, для передачи данных от компьютера к серверу
# # А веса его дуг могу обозначать скорость передач
# # сначала необходимо определиться со стартовой вершиной - для нее нулевой вес, так как мы уже в ней, а для остальных
# # максимальный, так как еще не определились с весами - это на 1 итерации
# # на 2 итерации - определяем вершины, до которых можно напрямую добраться от стартовой вершины, вес дуги складываем
# # с весом стартовой вершины (+0)
# #  затем из них выбирается вершина с минимальным весом - и затем смотрим в какую вершину из нее можно пройти напрямую,
# #  ту с которой вышли не рассматриваем, затем для этих вершин также рассчитываются веса - но!!! оставлять наименьшее
# #  (если предыдущее значение меньше, оставить его)
# # затем из них опять выбрать минимальное и т.д. Если из этой вершины больше никуда перейти нельзя, то это ее минимальный вес,
# #  и на следующей итерации она уже не будет участвовать. Из оставшихся выбираем с наименьшим весом и все так же.
# # представить таблицу с весами можно в виде матрицы смежности(строка 1-6, столбец от 1-6. вес на их пересечении)
# import math
#
# def get_link_v(v, D):
#     for i , weight in enumerate(D[v]):
#         if weight > 0:
#             yield i
#
# def arg_min(T, S):
#     amin = -1
#     m = max(T)
#     for i , t in enumerate(T):
#         if t < m and i not in S:
#             m = t
#             amin = i
#
#     return amin
#
# D = ((0, 3, 1, 3, 0, 0),
#      (3, 0, 4, 0, 0, 0),
#      (1, 4, 0, 0, 7, 5),
#      (3, 0, 0, 0, 0, 2),
#      (0, 0, 7, 0, 0, 4),
#      (0, 0, 5, 2, 4, 0))
#
# N = len(D)  # число вершин в графе
# T = [math.inf] * N # последняя строка таблицы
#
# v = 0 # стартовая вершина (так как нумерация с нуля)
# S = {v} # просмотренные вершины
# T[v] = 0 # нулевой вес для стартовой вершины
#
# while v != 1: # цикл пока не просмотрим все вершины
#     for j in get_link_v(v, D): # перебираем все связанные вершины, связанные с вершиной v
#         if j not in S:  # если вершина еще не просмотрена
#             w = T[v] + D[v][j]
#             if w < T[j]:
#                 T[j] = w
#
#     v = arg_min(T, S)  # выбираем следующий узел с наименьшим весом
#     if v > 0:  # выбрана следующая вершина
#         S.add(v)  # добавляем вершину в рассмотрение
#
# print(T)

# # ___________  Алгоритм Флойда ________________
# # также используется для поиска кратчайшего пути. Этот алгоритм может работать и с отрицательными весами дуг.
# # Находит сразу кратчайшие маршруты между вершинами графа. Решается динамическим путем (разбивается на несколько мелких задач)
# # веса также представляются в таблице в виде матрицы смежности (пустые графы - значение бесконечности)
# # рассматриваются суммы для всех пар вершин, выбираем наименьшее из того значения, что было в таблице, и полученной суммы пар вершин
# import math
# 
# def get_path(P, u, v):
#     path = [u]
#     while u != v:
#         u = P[u][v]
#         path.append(u)
# 
#     return path
# 
# V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
#      [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
#      [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
#      [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
#      [10, math.inf, 3, 8, math.inf, math.inf, 1, 0]
#      ]
# 
# N = len(V)  # число вершин в графе
# 
# P = [[v for v in range(N)] for u in range(N)]  # начальный список предыдущих вершин для поиска кратчайших маршрутов
# 
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             d = V[i][k] + V[k][j]
#             if V[i][j] > d:
#                 V[i][j] = d
#                 P[i][j] = k # номер промежуточной вершины при движении от i к j
# 
# # нумерация вершин начинается с нуля
# start = 0
# end = 7
# print(get_path(P, end, start))  # передаем коллекцию, в какую вершину прийти, с какой вершины выйти
# # [7, 6, 5, 4, 0]

# ________________  Алгоритм Форда-Фалкерсона  _________________________________
# позволяет определить максимальную пропускную способность потока в графе
# чем больше значение веса, тем выше пропускная способность дуги
# исток - откуда начинается поток, сток - вершина, куда направляется поток, значение веса целое неотрицательное число
# причем направление возможно только в одну сторону(в сторону стрелки), хотя рассчитать пропускную способность можно
# и против движения (по направлению стрелки +1, против стрелки - 1)
# максимальный вес потока будет равен самому узкому месту пути (наименьший вес на пути, на примере труб - самая узкая
# труба, пропускает меньше всего жидкости, поэтому пропускная способность всего пути будет зависеть от нее)

# вернуться к алгоритмам позже, пока не дается эта тема