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


def load_measurement_file():
    path = input("Path to measurement file: ")
    if not os.path.isfile(path):
        print("File not found")
        pause_terminal()
        measurement_file()
        return

    G.loaded_measurement = gasses.LoadGasses(path)


def plot_gas(idx: int):
    plot_data = G.loaded_measurement[:, idx + 2].reshape(100, 100)
    plt.imshow(plot_data)
    plt.colorbar()
    plt.show()


def plot_weighted():
    weighted_gasses = np.empty(10000)

    for i in range(10000):
        weighted_gasses[i] = gasses.calculate_weighted_emmissions(G.loaded_measurement[i][2],
                                                                  G.loaded_measurement[i][3],
                                                                  G.loaded_measurement[i][4],
                                                                  G.loaded_measurement[i][5])

    plt.imshow(weighted_gasses.reshape(100, 100))
    plt.colorbar()
    plt.show()


measurement_plot_options = {
    1: lambda: [plot_gas(0)],
    2: lambda: [plot_gas(1)],
    3: lambda: [plot_gas(2)],
    4: lambda: [plot_gas(3)],
    5: plot_weighted,
    6: lambda: []
}


def plot_measurement_data():
    print("1. co2"
          "\n2. ch4"
          "\n3. no2"
          "\n4. nh4"
          "\n5. weighted gasses"
          "\n6. Main menu")

    if not choose_option(measurement_plot_options):
        plot_measurement_data()
        return


def print_high_unknown_gas_concentration():
    gasses.get_high_unknown_gas_concentration(G.loaded_measurement).print_data()
    pause_terminal()


measurement_options = {
    1: load_measurement_file,
    2: plot_measurement_data,
    3: print_high_unknown_gas_concentration,
    4: lambda: []
}


def measurement_file():
    if G.loaded_measurement is None:
        load_measurement_file()

    print("1. Load other measurement file"
          "\n2. Plot data"
          "\n3. Find high unknown gas concentration"
          "\n4. Main menu")

    if not choose_option(measurement_options):
        measurement_file()
        return


main_options = {1: display_data,
                2: measurement_file}


def main():
    print("1. Display data"
          "\n2. Measurement file")

    if not choose_option(main_options):
        main()
        return
