import math


class Coordinate:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Area:
    def __init__(self, top_left_cord: Coordinate, bottom_right_cord: Coordinate):
        self.__top_left = top_left_cord
        self.__bottom_right = bottom_right_cord

    def get_top_left(self) -> Coordinate:
        return self.__top_left

    def get_bottom_right(self) -> Coordinate:
        return self.__bottom_right


def get_area_around_coordinate(x, y, cord_range) -> Area:
    top_left = Coordinate(x - cord_range, y - cord_range)
    bottom_right = Coordinate(x + cord_range, y + cord_range)
    return Area(top_left, bottom_right)


def is_coordinate_in_area(coordinate, area) -> bool:
    return (
            area.get_top_left().get_x() <= coordinate.get_x() <= area.get_bottom_right().get_x()
            and area.get_top_left().get_y() <= coordinate.get_y() <= area.get_bottom_right().get_y()
    )


def get_outside_coordinates(area) -> list[Coordinate]:
    outside_coordinates = []
    for x in range(area.get_top_left().get_x(), area.get_bottom_right().get_x() + 1):
        for y in range(area.get_top_left().get_y(), area.get_bottom_right().get_y() + 1):
            if (
                    x == area.get_top_left().get_x()
                    or x == area.get_bottom_right().get_x()
                    or y == area.get_top_left().get_y()
                    or y == area.get_bottom_right().get_y()
            ):
                outside_coordinates.append(Coordinate(x, y))
    return outside_coordinates


def is_coordinate_in_list(x, y, coordinate_list):
    for coord in coordinate_list:
        if coord.get_x() == x and coord.get_y() == y:
            return True
    return False


def get_surrounding_coordinates(x, y):
    surrounding_coordinates = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            surrounding_coordinates.append((x + dx, y + dy))

    return surrounding_coordinates


def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_nearest_company(x: int, y: int, coordinate_list: list[Coordinate]) -> None | Coordinate:
    if not coordinate_list:
        return None

    nearest_company = None
    min_distance = float('inf')

    for coordinate in coordinate_list:
        distance = get_distance(x, y, coordinate.get_x(), coordinate.get_y())
        if distance < min_distance:
            min_distance = distance
            nearest_company = coordinate

    return nearest_company
