import os
from datetime import datetime

import util


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause_terminal():
    input("Press any key to continue...")


class Report:
    def __init__(self, inspector_code: int, company_code: int, visit_date: str, report_date: str, status: str,
                 comment: str):
        self.__inspector_code = inspector_code
        self.__company_code = company_code
        self.__visit_date = visit_date
        self.__report_date = report_date
        self.__status = status
        self.__comment = comment

    def get_inspector_code(self) -> int:
        return self.__inspector_code

    def set_inspector_code_input(self):
        clear_terminal()

        code = input("Enter inspector code: ")
        if not code:
            print("Inspector code cannot be empty")
            self.set_inspector_code_input()
            return

        if not (len(code) <= 3):
            print("Inspector code max length is 3 digits")
            self.set_inspector_code_input()
            return

        if not code.isdigit():
            print("Inspector code must be digits only")
            self.set_inspector_code_input()
            return

        self.__inspector_code = int(code)

    def get_company_code(self) -> int:
        return self.__company_code

    def set_company_code_input(self):
        clear_terminal()

        code = input("Enter company code: ")
        if not code:
            print("Company code cannot be empty")
            self.set_company_code_input()
            return

        if not (len(code) <= 4):
            print("Company code max length is 4 digits")
            self.set_company_code_input()
            return

        if not code.isdigit():
            print("Company code must be digits only")
            self.set_company_code_input()
            return

        self.__company_code = int(code)

    def get_visit_date(self) -> str:
        return self.__visit_date

    def set_visit_date_input(self):
        clear_terminal()

        date = input("Enter visit date (yyyy-mm-dd): ")
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            formatted_date = parsed_date.strftime("%d-%m-%Y")
            self.__visit_date = formatted_date
        except ValueError:
            print("Visit date must be in the format yyyy-mm-dd")
            self.set_visit_date_input()

    def get_report_date(self) -> str:
        return self.__report_date

    def set_report_date_input(self):
        clear_terminal()

        date = input("Enter report date (yyyy-mm-dd, optional): ")
        if date:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d")
                formatted_date = parsed_date.strftime("%d-%m-%Y")
                self.__report_date = formatted_date
            except ValueError:
                print("Report date must be in the format yyyy-mm-dd")
                self.set_report_date_input()

    def get_status(self) -> str:
        return self.__status

    def set_status_input(self):
        clear_terminal()

        check = input("Enter check status (d for finalized, v for not temporary): ")
        check = check.lower()  # Convert input to lowercase for case-insensitive comparison

        if check == "d":
            self.__status = "d"
            return
        elif check == "v" and not (self.__status == "d"):
            self.__status = "v"
            return
        elif not (self.__status == "d"):
            self.__status = ""
        else:
            print("Invalid input")
            pause_terminal()
            self.set_status_input()

    def get_comment(self) -> str:
        return self.__comment

    def set_comment_input(self):
        clear_terminal()

        comment = input("Enter comment (optional): ")
        if comment and not comment.isdigit():
            print("Comment must be digits only")
            self.set_comment_input()
            return

        self.__comment = comment

    def print_data(self) -> None:
        visit_date = datetime.strptime(self.__visit_date.strip(), "%d-%m-%Y")
        report_date = datetime.strptime(self.__report_date.strip(), "%d-%m-%Y") if self.__report_date.strip() else None

        print(f"Inspector Code: {self.__inspector_code}", end=", ")
        print(f"Company Code: {self.__company_code}", end=", ")
        print(f"Visit Date: {visit_date}", end=", ")
        print(f"Report Date: {report_date}", end=", ")
        print(f"Status: {self.__status.strip()}", end=", ")
        print(f"Comment: {self.__comment.strip()}")

    def save_str(self) -> str:
        # Save using zfill and ljust for correct padding

        inspector_code = str(self.__inspector_code)[:3].zfill(3)
        company_code = str(self.__company_code)[:4].zfill(4)
        visit_date = self.__visit_date[:8].ljust(8)
        report_date = self.__report_date[:8].ljust(8) if self.__report_date else "".ljust(8)
        status = self.__status
        comment = self.__comment[:100].ljust(100)

        save = f"{inspector_code}{company_code}{visit_date}{report_date}{status}{comment}"
        return save


def parse_reports(file_path) -> list[Report]:
    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        print("The file with report data couldn't be found: ", file_path)
        exit(1)

    lines = file.readlines()
    file.close()

    # idx 0: inspector code
    # idx 1: company code
    # idx 2: visit date
    # idx 3: report date
    # idx 4: status
    # idx 5: comment
    indices = [0, 4, 9, 20, 31, 42, 142]

    reports = []
    for line in lines:
        values = [line[i:j] for i, j in zip(indices[:-1], indices[1:])]
        values = [value.strip() for value in values]

        try:
            reports.append(Report(util.str_int_safe(values[0]), util.str_int_safe(values[1]), values[2], values[3],
                                  values[4], values[5]))
        except ValueError:
            print("Invalid report data:", line)

    # sort based on visit date
    reports.sort(key=lambda x: x.get_visit_date(), reverse=True)

    return reports


def create_empty_report() -> Report:
    return Report(0, 0, "", "", "", "")
