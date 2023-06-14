import os
from datetime import datetime
from shutil import copyfile
from typing import Union

import matplotlib.pyplot as plt
import numpy as np

import company as company_struct
import coordinate
import gasses
import globals as G
import inspector as inspector_struct
import menu_controller
import report as report_struct


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
    gasses.get_high_unknown_gas_concentration(G.loaded_measurement).print_data()
    pause_terminal()


def show_company_fines():
    for company in G.companies:
        fine = company.set_fine_from_loaded_measurements()
        print("Fine for", company.get_name().strip(), "is", format(fine, ','), "euro")
    pause_terminal()


def select_company_from_xy() -> int:
    clear_terminal()

    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")

    if not x.isdigit() or not y.isdigit():
        print("Input not a number")
        pause_terminal()
        return select_company_from_xy()

    if (int(x) > 99 or int(x) < 0) or (int(y) > 99 or int(y) < 0):
        print("Invalid coordinates")
        pause_terminal()
        return select_company_from_xy()

    company_locations = []
    for company in G.companies:
        company_locations.append(coordinate.Coordinate(company.get_x(), company.get_y()))

    nearest = coordinate.get_nearest_coordinate(int(x), int(y), company_locations)
    if nearest is None:
        print("No company found")
        pause_terminal()
        return -1

    company = company_struct.from_xy(nearest.get_x(), nearest.get_y())
    if company is None:
        print("No company found")
        pause_terminal()
        return -1

    return company


def select_company_from_name() -> int:
    clear_terminal()
    name = input("Enter company name: ")

    for i, company in enumerate(G.companies):
        if name.lower() in company.get_name().strip().lower():
            return i

    print("Company not found")
    pause_terminal()
    return -1


def select_company() -> int:
    clear_terminal()
    print("1. Search company by x, y"
          "\n2. Search company by name")

    choice = input("\nEnter choice: ")
    if choice.isdigit() and (0 > int(choice) and int(choice) <= 3):
        print("Invalid choice")
        pause_terminal()
        return select_company()

    if choice == "1":
        return select_company_from_xy()
    elif choice == "2":
        return select_company_from_name()

    return -1


def add_company():
    clear_terminal()
    company = company_struct.create_empty_company()
    company.set_code_input()
    company.set_name_input()
    company.set_street_input()
    company.set_house_number_input()
    company.set_postal_code_input()
    company.set_city_input()
    company.set_x_input()
    company.set_y_input()
    company.set_max_emissions_input()
    company.set_emissions_input()
    company.set_fine_input()
    company.set_check_input()
    company.set_check_freq_input()
    company.set_contact_person_input()
    G.companies.append(company)
    print("Company added")
    company.print_data()
    pause_terminal()


def edit_company():
    selected = select_company()
    if selected == -1:
        return edit_company()

    clear_terminal()

    print("Selected company:", G.companies[selected].get_name().strip())

    print("1. Code"
          "\n2. Name"
          "\n3. Street"
          "\n4. House number"
          "\n5. Postal code"
          "\n6. City"
          "\n7. Max emissions"
          "\n8. Check"
          "\n9. Check frequency"
          "\n10. Contact person"
          "\n0. Cancel")

    choice = input("\nEnter choice: ")
    if not choice.isdigit() or not (0 < int(choice) <= 11):
        print("Invalid choice")
        pause_terminal()
        edit_company()
        return

    company = G.companies[selected]

    if choice == "1":
        company.set_code_input()
    elif choice == "2":
        company.set_name_input()
    elif choice == "3":
        company.set_street_input()
    elif choice == "4":
        company.set_house_number_input()
    elif choice == "5":
        company.set_postal_code_input()
    elif choice == "6":
        company.set_city_input()
    elif choice == "7":
        company.set_max_emissions_input()
    elif choice == "8":
        company.set_check_input()
    elif choice == "9":
        company.set_check_freq_input()
    elif choice == "10":
        company.set_contact_person_input()
    elif choice == "0":
        return

    print("Company updated")
    company.print_data()
    pause_terminal()


def delete_company():
    choice = select_company()

    should_delete = input("\nAre you sure you want to delete this company? (y/N): ")
    if should_delete.lower() == "y":
        del G.companies[int(choice)]
        print("Company deleted")
        pause_terminal()
        return
    else:
        print("Company not deleted")
        pause_terminal()
        return


def select_visit_report() -> int:
    clear_terminal()

    company_list = {}

    for i, report in enumerate(G.reports):
        date_formatted = datetime.strptime(report.get_visit_date(), "%Y%m%d")
        print_str = f"{i + 1}. Company code: {report.get_company_code()}, Inspector code: {report.get_inspector_code()}, Visit date: {date_formatted}"
        if report.get_company_code() not in company_list:
            company_list[report.get_company_code()] = []

        company_list[report.get_company_code()].append(print_str)

    for k, v in company_list.items():
        print("")
        for company in v:
            print(company)
        print("")

    choice = input("Enter choice: ")
    if choice.isdigit() and (0 > int(choice) and int(choice) <= len(G.reports)):
        print("Invalid choice")
        pause_terminal()
        return select_visit_report()

    clear_terminal()
    return int(choice) - 1


def add_visit_report():
    clear_terminal()
    report = report_struct.create_empty_report()
    report.set_inspector_code_input()
    report.set_company_code_input()
    report.set_visit_date_input()
    report.set_report_date_input()
    report.set_status_input()
    report.set_comment_input()

    G.reports.append(report)
    print("Report added")
    report.print_data()
    pause_terminal()


def edit_visit_report():
    selected = select_visit_report()
    if G.reports[selected].get_status().lower() == "d":
        print("This report has been finalized")
        pause_terminal()
        return

    print("1. Visit date"
          "\n2. report date"
          "\n3. Status"
          "\n4. Comment"
          "\n0. Cancel")

    choice = input("\nEnter choice: ")
    if not choice.isdigit() or not (0 < int(choice) <= 4):
        print("Invalid choice")
        pause_terminal()
        edit_visit_report()
        return

    report = G.reports[selected]

    if choice == "1":
        report.set_visit_date_input()
    elif choice == "2":
        report.set_report_date_input()
    elif choice == "3":
        report.set_status_input()
    elif choice == "4":
        report.set_comment_input()
    elif choice == "0":
        return

    print("Report updated")
    report.print_data()
    pause_terminal()


def delete_visit_report():
    choice = select_visit_report()

    should_delete = input("\nAre you sure you want to delete this report? (y/N): ")
    if should_delete.lower() == "y":
        del G.reports[int(choice)]
        print("Report deleted")
        pause_terminal()
        return
    else:
        print("Report not deleted")
        pause_terminal()
        return


def save():
    if os.path.isfile(G.COMPANIES_PATH + ".bak"):
        os.remove(G.COMPANIES_PATH + ".bak")
    copyfile(G.COMPANIES_PATH, G.COMPANIES_PATH + ".bak")

    if os.path.isfile(G.INSPECTORS_PATH + ".bak"):
        os.remove(G.INSPECTORS_PATH + ".bak")
    copyfile(G.INSPECTORS_PATH, G.INSPECTORS_PATH + ".bak")

    # save inspectors
    file = open(G.COMPANIES_PATH, 'w')
    for company in G.companies:
        save_val = company.save_str()
        file.write(save_val)
        file.write("\n")
    file.close()

    file = open(G.INSPECTORS_PATH, 'w')
    for report in G.reports:
        save_val = report.save_str()
        file.write(save_val)
        file.write("\n")
    file.close()

    exit(0)


def main():
    report_filtered_menu = menu_controller.Menu("Visit report filtered data", [
        ("Print visit reports per inspector", print_reports_per_inspector),
        ("Print visit reports per company", print_reports_per_company)
    ])
    display_data_menu = menu_controller.Menu("Display data", [
        ("Print inspector data", lambda: [print_data(G.inspectors)]),
        ("Print company data", lambda: [print_data(G.companies)]),
        ("Visit report filtered data", report_filtered_menu)
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

    select_company_edit_menu = menu_controller.Menu("Edit company data", [
        ("Add company", add_company),
        ("Edit company", edit_company),
        ("Delete company", delete_company)
    ])

    select_visit_reports_menu = menu_controller.Menu("Select visit report", [
        ("Add visit report", add_visit_report),
        ("Edit visit report", edit_visit_report),
        ("Delete visit report", delete_visit_report)
    ])

    manage_data_menu = menu_controller.Menu("Manage data", [
        ("Manage company data", select_company_edit_menu),
        ("Manage visit report", select_visit_reports_menu)
    ])

    main_menu = menu_controller.Menu("Main Menu", [
        ("Display data", display_data_menu),
        ("Measurement file", measurement_file_menu),
        ("Manage data", manage_data_menu),
        ("Exit and save", save)
    ])

    main_menu.display()
