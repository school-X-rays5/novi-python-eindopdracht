import os
import globals as G
from typing import Union
import company as company_struct
import inspector as inspector_struct
import report as report_struct


def clear_terminal():
    os.system("cls || clear")


def pause_terminal():
    os.system("pause")


def choose_option(options) -> bool:
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Input not a number")
        pause_terminal()
        clear_terminal()
        return False

    if choice < 1 or choice > len(options):
        print("Invalid choice")
        pause_terminal()
        return False

    options[choice]()
    return True


def print_data(data: Union[list[company_struct], list[inspector_struct], list[report_struct]]):
    for i in data:
        i.print_data()
    pause_terminal()

def print_reports_per_inspector():
    inspector_reports = dict[int, list[report_struct]]
    inspector_reports = {}

    for report in G.reports:
        inspector_code = report.get_inspector_code()
        if inspector_code not in inspector_reports:
            inspector_reports[inspector_code] = []

        inspector_reports[inspector_code].append(report)

    for k,v in inspector_reports.items():
        print("Reports for inspector with code", k, "\n")
        for report in v:
            report.print_data()
        print("\nEnd of reports for inspector with code", k, "\n\n")
    pause_terminal()


def print_reports_per_company():
    company_reports = dict[int, list[report_struct]]
    company_reports = {}

    for report in G.reports:
        company_code = report.get_company_code()
        if company_code not in company_reports:
            company_reports[company_code] = []

        company_reports[company_code].append(report)

    for k,v in company_reports.items():
        print("Reports for company with code", k, "\n")
        for report in v:
            report.print_data()
        print("\nEnd of reports for company with code", k, "\n\n")
    pause_terminal()

display_report_filtered_options = {
    1: print_reports_per_inspector,
    2: print_reports_per_company,
    3: lambda: []
}

def display_report_filtered():
    clear_terminal()
    print("1. Print reports per inspector"
          "\n2. Print reports per company"
          "\n3. Main menu")

    if not choose_option(display_report_filtered_options):
        display_report_filtered()
        return




data_display_options = {1: lambda: [print_data(G.inspectors)],
                        2: lambda: [print_data(G.companies)],
                        3: display_report_filtered,
                        4: lambda: []}


def display_data():
    clear_terminal()
    print("1. Print inspector data"
          "\n2. Print company data"
          "\n3. Report filtered data"
          "\n4. Main menu")

    if not choose_option(data_display_options):
        display_data()
        return


main_options = {1: display_data}

def main():
    print("1. Display data"
          "\n2. ")

    if not choose_option(main_options):
        main()
        return