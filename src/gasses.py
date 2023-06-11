import numpy as np
import globals
import coordinate

class GasConcentration:
    def __init__(self, x, y, co2, ch4, no2, nh3):
        self.__x = x
        self.__y = y
        self.__co2 = co2
        self.__ch4 = ch4
        self.__no2 = no2
        self.__nh3 = nh3

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_co2(self):
        return self.__co2

    def get_ch4(self):
        return self.__ch4

    def get_no2(self):
        return self.__no2

    def get_nh3(self):
        return self.__nh3


def LoadGasses(file_path):
    return np.loadtxt(file_path, delimiter=',', skiprows=1)

def GetHighUnknownConcentration(gasses_arr):
    company_areas = []
    for company in globals.companies:
        company_areas.append(coordinate.GetAreaAroundCoordinate(company.get_x(), company.get_y(), 5))

    highest = GasConcentration(0,0,0,0,0,0)
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

        co2 = row[2]
        if co2 > highest.get_co2():
            highest = GasConcentration(row[0], row[1], row[2], row[3], row[4], row[5])

    return highest
