class Company:
    def __init__(self, code, name, street, house_number, postal_code, city, x_worth, y_worth, max_emissions, emissions, fine, check, check_freq, contact_person):
        self.__code = int(code)
        self.__name = name.strip()
        self.__street = street.strip()
        self.__house_number = house_number.strip()
        self.__postal_code = postal_code.strip()
        self.__city = city.strip()
        self.__x_worth = int(x_worth)
        self.__y_worth = int(y_worth)
        self.__max_emissions = max_emissions.strip()
        self.__emissions = emissions.strip()
        self.__fine = fine.strip()
        self.__check = check
        self.__check_freq = int(check_freq) if check_freq.strip() else 0
        self.__contact_person = contact_person.strip()

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_street(self):
        return self.__street

    def get_house_number(self):
        return self.__house_number

    def get_postal_code(self):
        return self.__postal_code

    def get_city(self):
        return self.__city

    def get_x_worth(self):
        return self.__x_worth

    def get_y_worth(self):
        return self.__y_worth

    def get_max_emissions(self):
        return self.__max_emissions

    def get_emissions(self):
        return self.__emissions

    def get_fine(self):
        return self.__fine

    def get_check(self):
        return self.__check

    def get_check_freq(self):
        return self.__check_freq

    def get_contact_person(self):
        return self.__contact_person

def parse_companies(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    companies = []
    for line in lines:
        try:
            companies.append(Company(line[0:4], line[4:24], line[24:54], line[54:59], line[59:65], line[65:85], line[85:87], line[87:89], line[89:99], line[99:109], line[109:117], line[117:118], line[118:120], line[120:140]))
        except ValueError:
            print("Invalid data found when parsing", line[4:24])

    return companies
