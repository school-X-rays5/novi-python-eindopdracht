import numpy as np
import matplotlib.pyplot as plt
import inspector as inspector_struct
import company as company_struct
import report as report_struct

def main():
    inspectors = inspector_struct.parse_inspectors("input/inspectors.txt")
    for inspector in inspectors:
        print(inspector.get_code(), inspector.get_name(), inspector.get_place())

    companies = company_struct.parse_companies("input/companies.txt")
    for company in companies:
        print(company.get_code(), company.get_name(), company.get_city())

    reports = report_struct.parse_reports("input/reports.txt")
    for report in reports:
        print(report.get_company_code(), report.get_inspector_code(), report.get_visit_date(), report.get_status())

if __name__ == '__main__':
    main()
