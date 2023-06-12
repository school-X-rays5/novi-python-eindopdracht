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
        self.__max_emissions = max_emissions
        self.__emissions = emissions if emissions.strip() else ""
        self.__fine = fine if fine.strip() else ""
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

    def get_max_emissions(self) -> str:
        return self.__max_emissions

    def get_emissions(self) -> str:
        return self.__emissions

    def get_fine(self) -> str:
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
        print(f"Max Emissions: {self.__max_emissions.strip()}", end=", ")
        print(f"Emissions: {self.__emissions.strip()}", end=", ")
        print(f"Fine: {self.__fine.strip()}", end=", ")
        print(f"Check: {self.__check.strip()}", end=", ")
        print(f"Check Frequency: {self.__check_freq}", end=", ")
        print(f"Contact Person: {self.__contact_person.strip()}")


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