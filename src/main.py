import numpy as np
import matplotlib.pyplot as plt
import coordinate
import globals
import company as company_struct
import inspector as inspector_struct
import report as report_struct

def init():
    globals.companies = company_struct.parse_companies(globals.COMPANIES_PATH)
    globals.inspectors = inspector_struct.parse_inspectors(globals.INSPECTORS_PATH)
    globals.reports = report_struct.parse_reports(globals.REPORTS_PATH)

def main():
    init()

if __name__ == '__main__':
    main()
