from manager import ChecklistManager
from interface import TkinterInterface


def main():
    try:
        # Initialize standard backend file system manager logic
        tracker_manager = ChecklistManager("data.json")

        # Instantiate and transition application context window view targeting into Tkinter UI
        app_interface = TkinterInterface(tracker_manager)
        app_interface.start_loop()
    except FileNotFoundError as err:
        print(f"Error launching tracker application: {err}")
    except Exception as e:
        print(f"An unexpected initialization error occurred: {e}")


if __name__ == "__main__":
    main()