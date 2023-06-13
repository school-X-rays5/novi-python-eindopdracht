import coordinate
import gasses
import globals as G

FINE_AMOUNT = 1000

def calculate_total_emissions(x, y):
    class_1_emissions = 0  # 100%
    class_2_emissions = 0  # 50%
    class_3_emissions = 0  # 25%

    class_1_xy_list = [coordinate.Coordinate(x, y)]
    class_2_xy_list = coordinate.GetOutsideCoordinates(coordinate.GetAreaAroundCoordinate(x, y, 1))
    class_3_xy_list = coordinate.GetOutsideCoordinates(coordinate.GetAreaAroundCoordinate(x, y, 2))

    for row in G.loaded_measurement:
        row_x = row[0]
        row_y = row[1]
        co2 = row[2]
        ch4 = row[3]
        no2 = row[4]
        nh4 = row[5]

        if row_x == x and row_y == y:
            class_1_emissions += gasses.calculate_weighted_emissions(co2, ch4, no2, nh4)
        elif coordinate.IsCoordinateInList(row_x, row_y, class_2_xy_list):
            class_2_emissions += gasses.calculate_weighted_emissions(co2, ch4, no2, nh4) * 0.5
        elif coordinate.IsCoordinateInList(row_x, row_y, class_3_xy_list):
            class_3_emissions += gasses.calculate_weighted_emissions(co2, ch4, no2, nh4) * 0.25

    total_emissions = class_1_emissions + class_2_emissions + class_3_emissions
    return total_emissions

class Company:
    def __init__(self, code: str, name: str, street: str, house_number: str, postal_code: str, city: str, x: str, y: str, max_emissions: str, emissions: str, fine: str, check: str, check_freq: str, contact_person: str):
        self.__code = int(code)
        self.__name = name
        self.__street = street
        self.__house_number = house_number
        self.__postal_code = postal_code
        self.__city = city
        self.__x = int(x)
        self.__y = int(y)
        self.__max_emissions = int(max_emissions)
        self.__emissions = int(emissions) if emissions.strip() else 0
        self.__fine = int(fine) if fine.strip() else 0
        self.__check = check
        self.__check_freq = int(check_freq) if check_freq.strip() else 0
        self.__contact_person = contact_person if contact_person.strip() else ""

    def get_code(self) -> int:
        return self.__code

    def get_name(self) -> str:
        return self.__name

    def get_street(self) -> str:
        return self.__street

    def get_house_number(self) -> str:
        return self.__house_number

    def get_postal_code(self) -> str:
        return self.__postal_code

    def get_city(self) -> str:
        return self.__city

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_max_emissions(self) -> int:
        return self.__max_emissions

    def get_emissions(self) -> int:
        return self.__emissions

    def get_fine(self) -> int:
        return self.__fine

    def get_check(self) -> str:
        return self.__check

    def get_check_freq(self) -> int:
        return self.__check_freq

    def get_contact_person(self) -> str:
        return self.__contact_person

    def print_data(self) -> None:
        print(f"Company Code: {self.__code}", end=", ")
        print(f"Name: {self.__name.strip()}", end=", ")
        print(f"Street: {self.__street.strip()}", end=", ")
        print(f"House Number: {self.__house_number.strip()}", end=", ")
        print(f"Postal Code: {self.__postal_code.strip()}", end=", ")
        print(f"City: {self.__city.strip()}", end=", ")
        print(f"X: {self.__x}", end=", ")
        print(f"Y: {self.__y}", end=", ")
        print(f"Max Emissions: {self.__max_emissions}", end=", ")
        print(f"Emissions: {self.__emissions}", end=", ")
        print(f"Fine: {self.__fine}", end=", ")
        print(f"Check: {self.__check.strip()}", end=", ")
        print(f"Check Frequency: {self.__check_freq}", end=", ")
        print(f"Contact Person: {self.__contact_person.strip()}")

    def calculate_fine(self) -> int:
        self.__emissions = calculate_total_emissions(self.__x, self.__y)
        emissions_left = self.__max_emissions - self.__emissions
        if not (emissions_left < 0):
            return 0

        self.__fine = round(abs(emissions_left) * FINE_AMOUNT)
        return self.__fine


def parse_companies(file_path) -> list[Company]:
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    companies = []
    for line in lines:
        try:
            companies.append(Company(line[0:4], line[4:24], line[24:54], line[54:59], line[59:65], line[65:85], line[85:87], line[87:89], line[89:99], line[99:109], line[109:117], line[117:118], line[118:120], line[120:140]))
        except ValueError:
            print("Invalid company data:", line)

    return companies