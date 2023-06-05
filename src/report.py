class Report:
    def __init__(self, inspector_code, company_code, visit_date, report_date, status, comment):
        self.__inspector_code = int(inspector_code)
        self.__company_code = int(company_code)
        self.__visit_date = visit_date
        self.__report_date = report_date
        self.__status = status
        self.__comment = comment

    def get_inspector_code(self):
        return self.__inspector_code

    def get_company_code(self):
        return self.__company_code

    def get_visit_date(self):
        return self.__visit_date

    def get_report_date(self):
        return self.__report_date

    def get_status(self):
        return self.__status

    def get_comment(self):
        return self.__comment

def parse_reports(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    reports = []
    for line in lines:
        reports.append(Report(line[0:3], line[3:7], line[7:15], line[15:23], line[23:24], line[24:124]))

    return reports
