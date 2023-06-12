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


def GetAreaAroundCoordinate(x, y, cord_range) -> Area:
    top_left = Coordinate(x - cord_range, y - cord_range)
    bottom_right = Coordinate(x + cord_range, y + cord_range)
    return Area(top_left, bottom_right)


def IsCoordinateInArea(coordinate, area) -> bool:
    return (
        area.get_top_left().get_x() <= coordinate.get_x() <= area.get_bottom_right().get_x()
        and area.get_top_left().get_y() <= coordinate.get_y() <= area.get_bottom_right().get_y()
    )


def GetOutsideCoordinates(area) -> list[Coordinate]:
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