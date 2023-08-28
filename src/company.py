import os

import coordinate
import gasses
import globals as G
import util

FINE_AMOUNT = 1000


def calculate_total_emissions(x, y):
    class_1_emissions = 0  # 100%
    class_2_emissions = 0  # 50%
    class_3_emissions = 0  # 25%

    class_2_xy_list = coordinate.get_outside_coordinates(coordinate.get_area_around_coordinate(x, y, 1))
    class_3_xy_list = coordinate.get_outside_coordinates(coordinate.get_area_around_coordinate(x, y, 2))

    for row in G.loaded_measurement:
        row_x = row[0]
        row_y = row[1]
        co2 = row[2]
        ch4 = row[3]
        no2 = row[4]
        nh4 = row[5]

        if row_x == x and row_y == y:
            class_1_emissions = gasses.calculate_weighted_emissions(co2, ch4, no2, nh4)
        elif coordinate.is_coordinate_in_list(row_x, row_y, class_2_xy_list):
            class_2_emissions += gasses.calculate_weighted_emissions(co2, ch4, no2, nh4) * 0.5
        elif coordinate.is_coordinate_in_list(row_x, row_y, class_3_xy_list):
            class_3_emissions += gasses.calculate_weighted_emissions(co2, ch4, no2, nh4) * 0.25

    total_emissions = class_1_emissions + class_2_emissions + class_3_emissions
    return total_emissions


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause_terminal():
    input("Press any key to continue...")


class Company:
    def __init__(self, code: str, name: str, street: str, house_number: str, postal_code: str, city: str, x: str,
                 y: str, max_emissions: str, emissions: str, fine: str, check: str, check_freq: str,
                 contact_person: str):
        self.__code = util.str_int_safe(code)
        self.__name = name
        self.__street = street
        self.__house_number = house_number
        self.__postal_code = postal_code
        self.__city = city
        self.__x = util.str_int_safe(x)
        self.__y = util.str_int_safe(y)
        self.__max_emissions = util.str_int_safe(max_emissions)
        self.__emissions = util.str_int_safe(emissions) if emissions.strip() else 0
        self.__fine = util.str_int_safe(fine) if fine.strip() else 0
        self.__check = check
        self.__check_freq = util.str_int_safe(check_freq) if check_freq.strip() else 0
        self.__contact_person = contact_person if contact_person.strip() else ""

    def get_code(self) -> int:
        return self.__code

    def set_code(self, code: int):
        self.__code = code

    def set_code_input(self):
        clear_terminal()

        code = input("Enter code: ")
        if not (len(code) <= 4):
            print("Code max length is 4 digits")
            pause_terminal()
            self.set_code_input()
            return

        if not code.isdigit():
            print("Code must be digits only")
            pause_terminal()
            self.set_code_input()
            return

        self.__code = util.str_int_safe(code)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def set_name_input(self):
        clear_terminal()

        name = input("Enter name: ")
        if not (len(name) <= 20):
            print("Name max length is 20 characters long")
            pause_terminal()
            self.set_name_input()
            return

        self.__name = name

    def get_street(self) -> str:
        return self.__street

    def set_street(self, street: str):
        self.__street = street

    def set_street_input(self):
        clear_terminal()

        street = input("Enter street: ")
        if not (len(street) <= 30):
            print("Street max length is 30 characters long")
            pause_terminal()
            self.set_street_input()
            return

        self.__street = street

    def get_house_number(self) -> str:
        return self.__house_number

    def set_house_number(self, house_number: str):
        self.__house_number = house_number

    def set_house_number_input(self):
        clear_terminal()

        house_number = input("Enter house number: ")
        if not (len(house_number) <= 5):
            print("House number max length is 5 characters long")
            pause_terminal()
            self.set_house_number_input()
            return

        self.__house_number = house_number

    def get_postal_code(self) -> str:
        return self.__postal_code

    def set_postal_code(self, postal_code: str):
        self.__postal_code = postal_code

    def set_postal_code_input(self):
        clear_terminal()

        postal_code = input("Enter postal code: ")
        if not (len(postal_code) == 6 and postal_code[:4].isdigit() and postal_code[4:].isalpha()):
            print("Postal code must be in the format 'nnnncc'")
            pause_terminal()
            self.set_postal_code_input()
            return

        self.__postal_code = postal_code

    def get_city(self) -> str:
        return self.__city

    def set_city(self, city: str):
        self.__city = city

    def set_city_input(self):
        clear_terminal()

        city = input("Enter city: ")
        if not (len(city) <= 20):
            print("City max length is 20 characters long")
            pause_terminal()
            self.set_city_input()
            return

        self.__city = city

    def get_x(self) -> int:
        return self.__x

    def set_x(self, x: int):
        self.__x = x

    def set_x_input(self):
        clear_terminal()

        x = input("Enter x coordinate: ")
        if not (len(x) == 2):
            print("X coordinate must be 2 digits long")
            pause_terminal()
            self.set_x_input()
            return

        if not x.isdigit():
            print("X coordinate must be digits only")
            pause_terminal()
            self.set_x_input()
            return

        if util.str_int_safe(x) > 99 or util.str_int_safe(x) < 0:
            print("X coordinate must be between 0 and 99")
            pause_terminal()
            self.set_x_input()
            return

        self.__x = util.str_int_safe(x)

    def get_y(self) -> int:
        return self.__y

    def set_y(self, y: int):
        self.__y = y

    def set_y_input(self):
        clear_terminal()

        y = input("Enter y coordinate: ")
        if not (len(y) == 2):
            print("Y coordinate must be 2 digits long")
            pause_terminal()
            self.set_y_input()
            return

        if not y.isdigit():
            print("Y coordinate must be digits only")
            pause_terminal()
            self.set_y_input()
            return

        if util.str_int_safe(y) > 99 or util.str_int_safe(y) < 0:
            print("Y coordinate must be between 0 and 99")
            pause_terminal()
            self.set_y_input()
            return

        self.__y = util.str_int_safe(y)

    def get_max_emissions(self) -> int:
        return self.__max_emissions

    def set_max_emissions(self, max_emissions: int):
        self.__max_emissions = max_emissions

    def set_max_emissions_input(self):
        clear_terminal()

        max_emissions = input("Enter max emissions: ")
        if not (len(max_emissions) <= 10):
            print("Max emissions max length is 10 digits")
            pause_terminal()
            self.set_max_emissions_input()
            return

        if not max_emissions.isdigit():
            print("Max emissions must be digits only")
            pause_terminal()
            self.set_max_emissions_input()
            return

        self.__max_emissions = util.str_int_safe(max_emissions)

    def get_emissions(self) -> int:
        return self.__emissions

    def set_emissions(self, emissions: int):
        self.__emissions = emissions

    def set_emissions_input(self):
        clear_terminal()

        emissions = input("Enter emissions (leave empty for no value): ")
        if emissions.strip():
            if not (len(emissions) <= 10):
                print("Emissions max length is 10 digits")
                pause_terminal()
                self.set_emissions_input()
                return

            if not emissions.isdigit():
                print("Emissions must be digits only")
                pause_terminal()
                self.set_emissions_input()
                return

            self.__emissions = util.str_int_safe(emissions)
        else:
            self.__emissions = None

    def get_fine(self) -> int:
        return self.__fine

    def set_fine(self, fine: int):
        self.__fine = fine

    def set_fine_input(self):
        clear_terminal()

        fine = input("Enter fine (leave empty for no value): ")
        if fine.strip():
            if not (len(fine) <= 8):
                print("Fine max length is 10 digits")
                pause_terminal()
                self.set_fine_input()
                return

            if not fine.isdigit():
                print("Fine must be digits only")
                pause_terminal()
                self.set_fine_input()
                return

            self.__fine = util.str_int_safe(fine)
        else:
            self.__fine = None

    def get_check(self) -> str:
        return self.__check

    def set_check(self, check: str):
        self.__check = check

    def set_check_input(self):
        clear_terminal()

        check = input("Enter check status (j for inspected, n for not inspected): ")
        check = check.lower()  # Convert input to lowercase for case-insensitive comparison

        if check == "j":
            if self.__check == "n":
                self.__check = "j"
                print("Check status updated to 'inspected'")
                pause_terminal()
            else:
                print("Check status is already 'inspected' and cannot be changed")
                pause_terminal()
        elif check == "n":
            if self.__check == "j":
                print("Check status is already 'inspected' and cannot be changed to 'not inspected'")
                pause_terminal()
            else:
                self.__check = "n"
                print("Check status updated to 'not inspected'")
                pause_terminal()
        else:
            print("Invalid input. Enter 'j' for inspected, 'n' for not inspected")
            pause_terminal()
            self.set_check_input()

    def get_check_freq(self) -> int:
        return self.__check_freq

    def set_check_freq(self, check_freq: int):
        self.__check_freq = check_freq

    def set_check_freq_input(self):
        clear_terminal()

        check_freq = input("Enter check frequency (leave empty for no value): ")
        if check_freq.strip():
            if not (len(check_freq) <= 2):
                print("Check frequency max length is 2 digits")
                pause_terminal()
                self.set_check_freq_input()
                return

            if not check_freq.isdigit():
                print("Check frequency must be digits only")
                pause_terminal()
                self.set_check_freq_input()
                return

            check_freq_int = util.str_int_safe(check_freq)
            if check_freq_int < 1 or check_freq_int > 12:
                print("Check frequency must be between 1 and 12 (inclusive)")
                pause_terminal()
                self.set_check_freq_input()
                return

            self.__check_freq = check_freq_int
        else:
            self.__check_freq = None

    def get_contact_person(self) -> str:
        return self.__contact_person

    def set_contact_person(self, contact_person: str):
        self.__contact_person = contact_person

    def set_contact_person_input(self):
        clear_terminal()

        contact_person = input("Enter contact person (leave empty for no value): ")
        if contact_person.strip():
            if not (len(contact_person) <= 30):
                print("Contact person max length is 30 characters long")
                pause_terminal()
                self.set_contact_person_input()
                return

            self.__contact_person = contact_person
        else:
            self.__contact_person = None

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
        print(f"Contact Person: {self.__contact_person.strip() if self.__contact_person is not None else None}")

    def set_fine_from_loaded_measurements(self) -> int:
        self.__emissions = round(calculate_total_emissions(self.__x, self.__y))
        emissions_left = self.__max_emissions - self.__emissions
        if not (emissions_left < 0):
            return 0

        self.__fine = round(abs(emissions_left) * FINE_AMOUNT)
        return self.__fine

    def save_str(self) -> str:
        # Use zfill and ljust to align the output correctly

        code = str(self.__code)[:4].zfill(4)
        name = self.__name[:20].ljust(20)
        street = self.__street[:30].ljust(30)
        house_number = str(self.__house_number)[:5].ljust(5)
        postal_code = str(self.__postal_code)[:6].ljust(6)
        city = self.__city[:20].ljust(20)
        x = str(self.__x)[:2].zfill(2)
        y = str(self.__y)[:2].zfill(2)
        max_emissions = str(self.__max_emissions)[:10].ljust(10)
        emissions = str(self.__emissions)[:10].ljust(10)
        fine = str(self.__fine)[:8].ljust(8)
        check = str(self.__check)[:1].ljust(1)
        check_freq = str(self.__check_freq)[:2].ljust(2)
        contact_person = self.__contact_person[:20].ljust(20)

        save = f"{code}{name}{street}{house_number}{postal_code}{city}{x}{y}{max_emissions}{emissions}{fine}{check}{check_freq}{contact_person}"
        return save


def create_empty_company() -> Company:
    return Company("0", "", "", "", "", "", "0", "0", "0", "", "", "", "", "")


def parse_companies(file_path) -> list[Company]:
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    # idx 0: code
    # idx 1: name
    # idx 2: street
    # idx 3: house number
    # idx 4: postal code
    # idx 5: city
    # idx 6: x
    # idx 7: y
    # idx 8: max emissions
    # idx 9: emissions
    # idx 10: fine
    # idx 11: check
    # idx 12: check freq
    # idx 13: contact person
    indices = [0, 5, 25, 55, 59, 67, 87, 90, 93, 108, 123, 135, 139, 142, 162]

    companies = []
    for line in lines:
        values = [line[i:j] for i, j in zip(indices[:-1], indices[1:])]
        values = [value.strip() for value in values]

        try:
            companies.append(
                Company(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7],
                        values[8],
                        values[9], values[10], values[11], values[12], values[13])
            )
        except ValueError as err:
            print("Invalid company data:", line, err)

    return companies


def from_xy(x, y) -> int:
    for i, company in enumerate(G.companies):
        if company.get_x() == x and company.get_y() == y:
            return i

    return None


def from_code(code) -> Company:
    for i, company in enumerate(G.companies):
        if company.get_code() == code:
            return company

    return create_empty_company()
