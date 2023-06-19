import os

import globals as G


class Menu:
    def __init__(self, title: str, options: list[tuple[str, any]], enter_action=None):
        self.title = title
        self.options = options
        self.enter_action = enter_action

    def add_option(self, opt: tuple[str, any]):
        self.options.append(opt)

    def display(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            print("\n" + self.title)

            for index, option in enumerate(self.options):
                print(f"{index + 1}. {option[0]}")

            # Doing actions based on the title isn't the best way to do this, but it's the only way with this menu method.
            if self.title != "Main Menu":
                print("0. Go Back")

            if self.title == "Measurement file":
                if G.loaded_measurement is None:
                    return

            choice = input("\nEnter your choice: ")

            if choice == "0" and self.title != "Main Menu":
                return  # Return to the previous menu

            elif choice.isdigit() and int(choice) <= len(self.options):
                selected_option = self.options[int(choice) - 1]
                action = selected_option[1]

                if callable(action):
                    action()  # Call the function

                elif isinstance(action, Menu):
                    if callable(action.enter_action):
                        action.enter_action()  # Call the enter action for the submenu
                    action.display()  # Display the submenu

            else:
                print("Invalid choice. Please try again.")
