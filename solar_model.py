# coding: utf-8
# license: GPLv3

from math import*

g= 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        f = (g*body.m*obj.m)/r**2
        sin_angle = math.abs(body.y-obj.y)/math.sqrt((body.y - obj.y)**2 + (body.x-obj.x)**2)
        cos_angle = (body.x-obj.x)/math.sqrt((body.y - obj.y)**2 + (body.x-obj.x)**2)
        body.Fx += f*sin_angle # FIXME: нужно вывести формулу... done??
        body.Fy += f*cos_angle # FIXME: нужно вывести формулу... done??


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.Vx += ax*dt
    body.x += body.Vx  # FIXME: не понимаю как менять...
    ay= body.Fy/body.m
    body.Vy += ay*dt
    body.y += body.Vy
    # FIXME: not done recalculation of y coordinate! done??


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
