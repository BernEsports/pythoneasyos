import os
from time import sleep
import re
from datetime import datetime
import shutil


# TODO: Exceptions for every method and help for commands,
# Cancel method for every func that will make it begin from start

class Terminal:
    def __init__(self):
        self.commands = {
            "help": self.show_help,
            "dir": self.show_dir,
            "chdir": self.change_dir,
            "crf": self.create_folder,
            "mktxt": self.make_txt,
            "rdtxt": self.read_txt,
            "time": self.time,
            "rename": self.rename,
            "copy": self.copy,
            "fsrch": self.fsrch,
            "delete": self.delete
        }

    def show_help(self):
        help_text = {
            "help": "Show available commands and their descriptions.",
            "dir": "Show the current working directory.",
            "chdir": "Change the current working directory. chdir 'Name\Of\Dir'",
            "crf": "Create a new folder. crf 'NameOfFolder'",
            "mktxt": "Create a new text file. mktxt 'txtname'",
            "rdtxt": "Read a text file. rdtxt 'txtname'",
            "time": "Show current date and time",
            "rename": "Rename file or folder, 'rename test1 test2'",
            "copy": "Copy a file, 'copy book library'",
            "delete": "Delete a file, 'delete filename'",
            "fsrch": "Search for file, 'search filename'"
        }
        for command in self.commands:
            print(f"{command}: {help_text.get(command, 'No description available')}")

    def show_dir(self):
        print(os.getcwd())
    
    
    def change_dir(self, path_change):
        if os.path.exists(path_change) == True:
            os.chdir(path_change)
        else:
            print("Directory doesnt exists")
    
    
    def create_folder(self, folder_path):
        try:
            # check if first symbol is number or special symbols in name
            if folder_path[0].isnumeric():
                print("Incorrect name, folder name can't start with a number")
            elif re.search(r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?/~`\\|]', folder_path):
                print("Incorrect name, folder name can't start with special character")
            else:
                os.makedirs(folder_path)
        except FileExistsError:
            print("File already exists")

    
    def make_txt(self):
        name_of_txt = input("Enter name of txt file you want to create\n>> ")
        try:
            txt_text = input("Enter text for txt\n>> ")
            with open(name_of_txt, "w") as f:
                f.write(txt_text)
        except FileNotFoundError:
            print("This directory not found")
    
    
    def read_txt(self, path_of_txt):
        try:
            with open(path_of_txt, "r") as f:
                print(f.readline())
                sleep(5)
        except FileNotFoundError:
            print("This file doesnt exists!")
            
    def time(self):
        # Days/Month/Year Hour:Minutes
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(current_time)
        
    
    def rename(self, old_name, new_name):
        if os.path.isfile(old_name) == False:
            print("This file is not exists")
        if os.path.isfile(new_name):
            print("This file already exists")
        else:
            os.rename(old_name, new_name)
    
    
    def fsrch(self, search_query):
        # search_query = input("Enter search query (e.g., '*.txt' for text files):\n>> ")
        results = []

        for root, dirs, files in os.walk(os.getcwd()):
            for item in dirs + files:
                if search_query in item:
                    results.append(os.path.join(root, item))

        if results:
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No files or directories found matching the search criteria.")
    
    
    def delete(self, remove_name):
        # check if file exists and gets user confirm
        if os.path.isfile(remove_name):
            confirm = input(f"You really want to delete '{remove_name}'\
                ? (Y or N)\n>> ")
            if confirm.lower() == "y":
                os.remove(remove_name)
            else:
                return 0
        else:
            print("This file doesnt exists")
    
    
    def copy(self, copy_from, copy_to_path):
        # check if file exists
        if os.path.isfile(copy_from):
            if copy_from in copy_to_path:
                print("This file already exists")
            shutil.copy(copy_from, copy_to_path)
        else:
            print("This file doesnt exists")
        

def main():
    # single class instance
    terminal = Terminal()
    while True:
        try:
            user_input = input("\nEnter a command\n>> ")

            if user_input.lower() == "exit":
                break

            # Разделяем ввод пользователя на команду и аргументы
            command_args = user_input.split()

            if command_args:
                command = command_args[0].lower()  # Command
                args = command_args[1:]  # Arguments of method

                if command in terminal.commands:
                    terminal.commands[command](*args)  # Give args to method
                else:
                    print("Incorrect command, enter \"help\" for list of available commands\n"
                          "Or enter \"Exit\" to exit terminal")

        except EOFError:
            print("Exiting...")
            sleep(1)
            break

        except KeyboardInterrupt:
            print("Incorrect command!")
        
        except TypeError:
            print("Incorrect args for a command!")
            
                
if __name__ == "__main__":
    main()

