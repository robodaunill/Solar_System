# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:


    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == 'star':
                cel_body = Star()
                parse_obj_parameters(line, cel_body)
                objects.append(cel_body)
            elif object_type == 'planet':
                cel_body = Planet()
                parse_obj_parameters(line, cel_body)
                objects.append(cel_body)

            else:
                print("Unknown space object")

    return objects


def parse_obj_parameters(line, cel_body):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    parsed_line = line.split()  # FIXED
    cel_body.R = float(parsed_line[1])
    cel_body.color = str(parsed_line[2])
    cel_body.m = float(parsed_line[3])
    cel_body.x = float(parsed_line[4])
    cel_body.y = float(parsed_line[5])
    cel_body.Vx = float(parsed_line[6])
    cel_body.Vy = float(parsed_line[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if isinstance(obj, Star):
                out_file.write(f"Star {obj.r} {obj.color} {obj.m} {obj.x} {obj.y} {obj.Vx} {obj.Vy}\n")
            elif isinstance(obj, Planet):
                out_file.write(f"Planet {obj.r} {obj.color} {obj.m} {obj.x} {obj.y} {obj.Vx} {obj.Vy}\n")


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
