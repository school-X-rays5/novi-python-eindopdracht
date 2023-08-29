import util


class Inspector:
    def __init__(self, code: int, name: str, place: str):
        self.__code = code
        self.__name = name
        self.__place = place

    def get_code(self) -> int:
        return self.__code

    def get_name(self) -> str:
        return self.__name

    def get_place(self) -> str:
        return self.__place

    def print_data(self) -> None:
        print(f"Inspector Code: {self.__code}", end=", ")
        print(f"Name: {self.__name.strip()}", end=", ")
        print(f"Place: {self.__place.strip()}")


def parse_inspectors(file_path) -> list[Inspector]:
    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        print("The file with inspector data couldn't be found: ", file_path)
        exit(1)
        
    lines = file.readlines()
    file.close()

    # idx 0: code
    # idx 1: name
    # idx 2: place
    indices = [0, 4, 24, 44]

    inspectors = []
    for line in lines:
        values = [line[i:j] for i, j in zip(indices[:-1], indices[1:])]
        values = [value.strip() for value in values]

        try:
            inspectors.append(Inspector(util.str_int_safe(values[0]), values[1], values[2]))
        except ValueError:
            print("Invalid inspector data:", line)

    return inspectors
