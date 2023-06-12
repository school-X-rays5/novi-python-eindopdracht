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
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    inspectors = []
    for line in lines:
        try:
            inspectors.append(Inspector(int(line[0:3]), line[3:23].strip(), line[23:43].strip()))
        except ValueError:
            print("Invalid inspector data:", line)

    return inspectors
