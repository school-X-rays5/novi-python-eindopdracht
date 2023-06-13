import atexit
import os

import company as company_struct
import globals as G
import inspector as inspector_struct
import menu
import report as report_struct

main_menu_active = True


def init():
    G.companies = company_struct.parse_companies(G.COMPANIES_PATH)
    G.inspectors = inspector_struct.parse_inspectors(G.INSPECTORS_PATH)
    G.reports = report_struct.parse_reports(G.REPORTS_PATH)


def save():
    print("exit")


def main():
    os.system("cls || clear")
    init()

    atexit.register(save)

    while main_menu_active:
        menu.main()
        os.system("cls || clear")


if __name__ == '__main__':
    main()
