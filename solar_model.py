# coding: utf-8
# license: GPLv3

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
        sin_angle = (obj.y-body.y)/r
        cos_angle = (obj.x-body.x)/r
        body.Fx += f*cos_angle # FIXME: нужно вывести формулу... done??
        body.Fy += f*sin_angle # FIXME: нужно вывести формулу... done??


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.Vx += ax*dt
    print(body.Vx)
    body.x += body.Vx*dt  # FIXME: не понимаю как менять... done??
    ay = body.Fy/body.m
    body.Vy += ay*dt
    body.y += body.Vy*dt
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
