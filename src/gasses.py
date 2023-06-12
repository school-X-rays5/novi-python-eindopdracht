import numpy as np

import coordinate
import globals

CO2_WEIGHT = 1
CH4_WEIGHT = 25
NO2_WEIGHT = 5
NH3_WEIGHT = 1000


def calculate_weighted_emmissions(co2: float, ch4: float, no2: float, nh3: float) -> float:
    return (CO2_WEIGHT * co2) + (CH4_WEIGHT * ch4) + (NO2_WEIGHT * no2) + (NH3_WEIGHT * nh3)


class GasConcentration:
    def __init__(self, x: int, y: int, co2: float, ch4: float, no2: float, nh3: float):
        self.__x = x
        self.__y = y
        self.__co2 = co2
        self.__ch4 = ch4
        self.__no2 = no2
        self.__nh3 = nh3
        self.__weighted_emmissions = calculate_weighted_emmissions(co2, ch4, no2, nh3)

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_co2(self) -> float:
        return self.__co2

    def get_ch4(self) -> float:
        return self.__ch4

    def get_no2(self) -> float:
        return self.__no2

    def get_nh3(self) -> float:
        return self.__nh3

    def get_weighted_emmissions(self) -> float:
        return self.__weighted_emmissions

    def print_data(self):
        print(
            f"x: {self.__x}, y: {self.__y}, co2: {self.__co2}, ch4: {self.__ch4}, no2: {self.__no2}, nh3: {self.__nh3}, co2 equivalent: {self.__weighted_emmissions}")


def LoadGasses(file_path) -> np.ndarray:
    try:
        return np.loadtxt(file_path, delimiter=',', skiprows=1)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def get_high_unknown_gas_concentration(gasses_arr) -> GasConcentration:
    company_areas = []
    for company in globals.companies:
        company_areas.append(coordinate.GetAreaAroundCoordinate(company.get_x(), company.get_y(), 5))

    highest = GasConcentration(0, 0, 0, 0, 0, 0)
    for row in gasses_arr:
        x = row[0]
        y = row[1]
        if x < 2 or x > 97:
            continue
        elif y < 2 or y > 97:
            continue

        is_inside_area = False
        for company_area in company_areas:
            if coordinate.IsCoordinateInArea(coordinate.Coordinate(x, y), company_area):
                is_inside_area = True
                break  # Exit the loop when an intersection is found

        if is_inside_area:
            continue

        emissions = calculate_weighted_emmissions(row[2], row[3], row[4], row[5])
        if emissions > highest.get_weighted_emmissions():
            highest = GasConcentration(row[0], row[1], row[2], row[3], row[4], row[5])

    return highest
