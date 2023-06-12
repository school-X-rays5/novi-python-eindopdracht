import globals as G
import company as company_struct
import inspector as inspector_struct
import report as report_struct

def init():
    G.companies = company_struct.parse_companies(G.COMPANIES_PATH)
    G.inspectors = inspector_struct.parse_inspectors(G.INSPECTORS_PATH)
    G.reports = report_struct.parse_reports(G.REPORTS_PATH)

def main():
    init()

if __name__ == '__main__':
    main()
