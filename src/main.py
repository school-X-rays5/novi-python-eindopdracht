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
    print("")
    choice = input("Save changes? (y/n) ")
    if choice.lower() == "y":
        print("Saving...")
    elif choice == "n":
        return
    else:
        print("Invalid choice.")
        save()
        return


def main():
    os.system("cls" if os.name == "nt" else "clear")
    init()

    atexit.register(save)

    while main_menu_active:
        menu.main()
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == '__main__':
    main()
