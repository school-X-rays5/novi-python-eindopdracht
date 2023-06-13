import os

class Menu:
    def __init__(self, title, options, enter_action=None):
        self.title = title
        self.options = options
        self.enter_action = enter_action

    def display(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            print("\n" + self.title)

            for index, option in enumerate(self.options):
                print(f"{index + 1}. {option[0]}")

            if self.title != "Main Menu":
                print("0. Go Back")

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