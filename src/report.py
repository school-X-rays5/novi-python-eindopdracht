from datetime import datetime


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

    def get_company_code(self) -> int:
        return self.__company_code

    def get_visit_date(self) -> str:
        return self.__visit_date

    def get_report_date(self) -> str:
        return self.__report_date

    def get_status(self) -> str:
        return self.__status

    def get_comment(self) -> str:
        return self.__comment

    def print_data(self) -> None:
        visit_date = datetime.strptime(self.__visit_date.strip(), "%Y%m%d")
        report_date = datetime.strptime(self.__report_date.strip(), "%Y%m%d") if self.__report_date.strip() else None

        print(f"Inspector Code: {self.__inspector_code}", end=", ")
        print(f"Company Code: {self.__company_code}", end=", ")
        print(f"Visit Date: {visit_date}", end=", ")
        print(f"Report Date: {report_date}", end=", ")
        print(f"Status: {self.__status.strip()}", end=", ")
        print(f"Comment: {self.__comment.strip()}")


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
