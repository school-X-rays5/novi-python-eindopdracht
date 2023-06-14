import os
from datetime import datetime


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

        date = input("Enter visit date (YYYY-MM-DD): ")
        if not (len(date) == 10):
            print("Visit date must be in the format YYYY-MM-DD")
            self.set_visit_date_input()
            return

        self.__visit_date = date.replace("-", "")

    def get_report_date(self) -> str:
        return self.__report_date

    def set_report_date_input(self):
        clear_terminal()

        date = input("Enter report date (YYYY-MM-DD, optional): ")
        if date and not (len(date) == 10):
            print("Report date must be in the format YYYY-MM-DD")
            self.set_report_date_input()
            return

        if date:
            self.__report_date = date.replace("-", "")

    def get_status(self) -> str:
        return self.__status

    def set_status_input(self):
        clear_terminal()

        check = input("Enter check status (d for finalized, v for not temporary): ")
        check = check.lower()  # Convert input to lowercase for case-insensitive comparison

        if check == "d":
            self.__status = "finalized"
            return
        elif check == "v" and not (self.__status == "finalized"):
            self.__status = "temporary"
            return
        elif not (self.__status == "finalized"):
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
        visit_date = datetime.strptime(self.__visit_date.strip(), "%Y%m%d")
        report_date = datetime.strptime(self.__report_date.strip(), "%Y%m%d") if self.__report_date.strip() else None

        print(f"Inspector Code: {self.__inspector_code}", end=", ")
        print(f"Company Code: {self.__company_code}", end=", ")
        print(f"Visit Date: {visit_date}", end=", ")
        print(f"Report Date: {report_date}", end=", ")
        print(f"Status: {self.__status.strip()}", end=", ")
        print(f"Comment: {self.__comment.strip()}")

    def save_str(self) -> str:
        inspector_code = str(self.__inspector_code)[:3].zfill(3)
        company_code = str(self.__company_code)[:4].zfill(4)
        visit_date = self.__visit_date[:8].ljust(8)
        report_date = self.__report_date[:8].ljust(8) if self.__report_date else "".ljust(8)
        status = self.__status
        comment = self.__comment[:100].ljust(100)

        save = f"{inspector_code}{company_code}{visit_date}{report_date}{status}{comment}"
        return save


def parse_reports(file_path) -> list[Report]:
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    reports = []
    for line in lines:
        try:
            reports.append(Report(int(line[0:3]), int(line[3:7]), line[7:15], line[15:23], line[23:24], line[24:124]))
        except ValueError:
            print("Invalid report data:", line)

    return reports


def create_empty_report() -> Report:
    return Report(0, 0, "", "", "", "")
