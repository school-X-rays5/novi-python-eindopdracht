import numpy as np

import coordinate
import globals as G

CO2_WEIGHT = 1
CH4_WEIGHT = 25
NO2_WEIGHT = 5
NH3_WEIGHT = 1000


def calculate_weighted_emissions(co2: float, ch4: float, no2: float, nh3: float) -> float:
    return (CO2_WEIGHT * co2) + (CH4_WEIGHT * ch4) + (NO2_WEIGHT * no2) + (NH3_WEIGHT * nh3)


def calculate_average_weighted_emissions(gasses_arr):
    emissions = gasses_arr[:, 2:6]  # Extract columns 2 to 5 (CO2, CH4, NO2, NH3)
    weighted_emissions = np.apply_along_axis(lambda row: calculate_weighted_emissions(*row), 1, emissions)

    return np.mean(weighted_emissions)


class GasConcentration:
    def __init__(self, x: int, y: int, co2: float, ch4: float, no2: float, nh3: float):
        self.__x = x
        self.__y = y
        self.__co2 = co2
        self.__ch4 = ch4
        self.__no2 = no2
        self.__nh3 = nh3
        self.__weighted_emissions = calculate_weighted_emissions(co2, ch4, no2, nh3)

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

    def get_weighted_emissions(self) -> float:
        return self.__weighted_emissions

    def print_data(self):
        print(
            f"x: {self.__x}, y: {self.__y}, co2: {self.__co2}, ch4: {self.__ch4}, no2: {self.__no2}, nh3: {self.__nh3}, co2 equivalent: {self.__weighted_emissions}")


def load_gasses(file_path) -> np.ndarray:
    try:
        return np.loadtxt(file_path, delimiter=',', skiprows=1)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def get_company_areas():
    company_areas = []
    for company in G.companies:
        company_areas.append(coordinate.get_area_around_coordinate(company.get_x(), company.get_y(), 5))

    return company_areas


def is_coordinate_valid(x, y):
    if x < 2 or x > 97 or y < 2 or y > 97:
        return False

    return True


def is_coordinate_inside_area(cord, company_areas):
    for company_area in company_areas:
        if coordinate.is_coordinate_in_area(cord, company_area):
            return True

    return False


def get_unknown_emissions(row, company_areas):
    x = row[0]
    y = row[1]

    if not is_coordinate_valid(x, y):
        return 0

    if is_coordinate_inside_area(coordinate.Coordinate(x, y), company_areas):
        return 0

    return calculate_weighted_emissions(row[2], row[3], row[4], row[5])


def get_high_unknown_gas_concentration(gasses_arr: np.ndarray, company_areas):
    highest = GasConcentration(0, 0, 0, 0, 0, 0)

    for row in gasses_arr:
        emissions = get_unknown_emissions(row, company_areas)
        if emissions > highest.get_weighted_emissions():
            highest = GasConcentration(row[0], row[1], row[2], row[3], row[4], row[5])

    return highest


def get_above_average_unknown_gas_concentrations(gasses_arr: np.ndarray):
    company_areas = get_company_areas()
    average = calculate_average_weighted_emissions(gasses_arr)
    average += average / 10  # Add a small amount to avoid false positives
    found_items = []

    while True:
        concentration = get_high_unknown_gas_concentration(gasses_arr, company_areas)

        if concentration.get_weighted_emissions() > average:
            found_items.append(concentration)
            company_areas.append(coordinate.get_area_around_coordinate(concentration.get_x(), concentration.get_y(), 5))
        else:
            break

    return found_items
