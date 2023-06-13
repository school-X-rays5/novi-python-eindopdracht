import os
from datetime import datetime
from typing import Union

import matplotlib.pyplot as plt
import numpy as np

import company as company_struct
import gasses
import globals as G
import inspector as inspector_struct
import report as report_struct
import menu_controller


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def pause_terminal():
    input("Press Enter to continue...")


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


def get_date_range_input() -> None | tuple[datetime, datetime] | tuple[None, None] | tuple[
    datetime | None, datetime | None]:
    begin_date = input("Enter begin date (yyyy-mm-dd) (leave blank to skip): ")
    end_date = ""
    if begin_date:
        end_date = input("Enter end date (yyyy-mm-dd): ")
        if not end_date:
            print("End date is required when begin date is provided.")
            return get_date_range_input()
    else:
        return None, None

    begin: None | datetime = None
    end: None | datetime = None
    try:
        if begin_date:
            begin = datetime.strptime(begin_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date")
        pause_terminal()

        return None

    return begin, end


def print_reports_per_inspector():
    clear_terminal()
    try:
        inspector_code = int(input("Enter inspector code: "))
    except ValueError:
        print("Input not a number")
        print_reports_per_inspector()
        return

    begin, end = None, None
    while True:
        result = get_date_range_input()
        if not (result is None):
            begin, end = result
            break

    for report in G.reports:
        if report.get_inspector_code() == inspector_code:
            visit_date = datetime.strptime(report.get_visit_date(), "%Y%m%d")
            if begin is not None and end is not None:
                if not (begin <= visit_date <= end):
                    continue

            report.print_data()

    pause_terminal()


def print_reports_per_company():
    clear_terminal()
    try:
        company_code = int(input("Enter company code: "))
    except ValueError:
        print("Input not a number")
        print_reports_per_company()
        return

    begin, end = None, None
    while True:
        result = get_date_range_input()
        if not (result is None):
            begin, end = result
            break

    for report in G.reports:
        if report.get_company_code() == company_code:
            visit_date = datetime.strptime(report.get_visit_date(), "%Y%m%d")
            if begin is not None and end is not None:
                if not (begin <= visit_date <= end):
                    continue

            report.print_data()

    pause_terminal()

def load_measurement_file():
    path = input("Path to measurement file: ")
    if not os.path.isfile(path) or not path.endswith(".csv"):
        print("Invalid file")
        pause_terminal()
        load_measurement_file()
        return

    try:
        G.loaded_measurement = gasses.LoadGasses(path)
    except ValueError:
        print("Invalid file contents")
        load_measurement_file()


def plot_gas(idx: int):
    plot_data = G.loaded_measurement[:, idx + 2].reshape(100, 100)
    plt.imshow(plot_data)
    plt.colorbar()
    plt.show()


def plot_weighted():
    weighted_gasses = np.empty(10000)

    for i in range(10000):
        weighted_gasses[i] = gasses.calculate_weighted_emissions(G.loaded_measurement[i][2],
                                                                  G.loaded_measurement[i][3],
                                                                  G.loaded_measurement[i][4],
                                                                  G.loaded_measurement[i][5])

    plt.imshow(weighted_gasses.reshape(100, 100))
    plt.colorbar()
    plt.show()

def print_above_average_unknown_gas_concentration():
    for concentration in gasses.get_above_average_unknown_gas_concentrations(G.loaded_measurement):
        concentration.print_data()
    pause_terminal()

def print_high_unknown_gas_concentration():
    gasses.get_high_unknown_gas_concentration(G.loaded_measurement, gasses.get_company_areas()).print_data()
    pause_terminal()

def show_company_fines():
    for company in G.companies:
        fine = company.calculate_fine()
        print("Fine for", company.get_name().strip(), "is", format(fine, ','), "euro")
    pause_terminal()

def main():
    report_filtered_menu = menu_controller.Menu("Report filtered data", [
        ("Print reports per inspector", print_reports_per_inspector),
        ("Print reports per company", print_reports_per_company)
    ])
    display_data_menu = menu_controller.Menu("Display data", [
        ("Print inspector data", lambda: [print_data(G.inspectors)]),
        ("Print company data", lambda: [print_data(G.companies)]),
        ("Report filtered data", report_filtered_menu)
    ])


    plot_measurement_data_menu = menu_controller.Menu("Plot measurement data", [
        ("co2", lambda: [plot_gas(0)]),
        ("ch4", lambda: [plot_gas(1)]),
        ("no2", lambda: [plot_gas(2)]),
        ("nh4", lambda: [plot_gas(3)]),
        ("co2 equivalent", plot_weighted)
    ])

    high_gas_concentration_menu = menu_controller.Menu("Unknown high gas concentration", [
        ("All unknown above average", print_above_average_unknown_gas_concentration),
        ("Highest unknown", print_high_unknown_gas_concentration)
    ])

    measurement_file_menu = menu_controller.Menu("Measurement file", [
        ("Load other measurement file", load_measurement_file),
        ("Plot data", plot_measurement_data_menu),
        ("Find high gas concentration", high_gas_concentration_menu),
        ("Calculate fines", show_company_fines)
    ], lambda: [load_measurement_file() if G.loaded_measurement is None else None])


    main_menu = menu_controller.Menu("Main Menu", [
        ("Display data", display_data_menu),
        ("Measurement file", measurement_file_menu)
    ])

    main_menu.display()
