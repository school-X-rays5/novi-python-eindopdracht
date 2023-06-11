class Inspector:
    def __init__(self, code, name, place):
        self.__code = code
        self.__name = name
        self.__place = place

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_place(self):
        return self.__place
    
    def print_data(self):
         print(self.__code, self.__name, self.__place)


def parse_inspectors(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    inspectors = []
    for line in lines:
        try:
            inspectors.append(Inspector(int(line[0:3]), line[3:23].strip(), line[23:43].strip()))
        except ValueError:
            print("Inspector code for", line[3:23].strip(), "is nan")

    return inspectors
