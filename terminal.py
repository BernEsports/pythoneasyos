import os
from time import sleep
import re
from datetime import datetime
import shutil


# TODO: Exceptions for every method and help for commands,
# Cancel method for every func that will make it begin from start

# dir = show directory ; chdir = change directory ; crf = create folder
# mktxt = make txt file ; rdtxt = read txt file


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
            "chdir": "Change the current working directory.",
            "crf": "Create a new folder.",
            "mktxt": "Create a new text file.",
            "rdtxt": "Read a text file.",
            "time": "Show current date and time",
            "rename": "Rename file or folder",
            "copy": "Copy a file",
            "delete": "Delete a file",
            "fsrch": "Search for file"
        }
        for command in self.commands:
            print(f"{command}: {help_text.get(command, 'No description available')}")
    

    def show_dir(self):
        print(os.getcwd())
    
    def change_dir(self):
        path_change = input("Enter folder name\n>> ")
        if os.path.exists(path_change) == True:
            os.chdir(path_change)
        else:
            print("Directory doesnt exists")
    
    def create_folder(self):
        folder_path = input("Enter folder name\n>> ")
        if folder_path[0].isnumeric():
            print("Incorrect name, folder name can't start with a number")
        elif re.search(r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?/~`\\|]', folder_path):
            print("Incorrect name, folder name can't start with special character")
        else:
            os.makedirs(folder_path)

    def make_txt(self):
        name_of_txt = input("Enter name of txt file you want to create\n>> ")
        try:
            txt_text = input("Enter text for txt\n>> ")
            with open(name_of_txt, "w") as f:
                f.write(txt_text)
        except FileNotFoundError:
            print("This directory not found")
    
    def read_txt(self):
        path_of_txt = input("Enter path of txt file you want to read\n>> ")
        try:
            with open(path_of_txt, "r") as f:
                # TODO: file reading
                print(f.readline())
                sleep(5)
        except FileNotFoundError:
            print("This file doesnt exists!")
            
    def time(self):
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(current_time)
        
    def rename(self):
        old_name = input("Enter file name that you want to rename\n>> ")
        if os.path.isfile(old_name) == False:
            print("This file is not exists")
        new_name = input("Enter new name for a file\n>> ")
        if os.path.isfile(new_name):
            print("This file already exists")
        else:
            os.rename(old_name, new_name)
    
    def fsrch(self):
        search_query = input("Enter search query (e.g., '*.txt' for text files):\n>> ")
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
    
    def delete(self):
        remove_name = input("Enter name of a folder\n>> ")
        if os.path.isfile(remove_name):
            confirm = input(f"You really want to delete '{remove_name}'\
                ? (Y or N)\n>> ")
            if confirm.lower() == "y":
                os.remove(remove_name)
            else:
                return 0
        else:
            print("This file doesnt exists")
    
    
    def copy(self):
        copy_from = input("Enter name of a file you want to copy\n>> ")
        if os.path.isfile(copy_from):
            copy_to_path = input("Enter where do you want to copy this file\n>> ")
            if copy_from in copy_to_path:
                print("This file already exists")
            shutil.copy(copy_from, copy_to_path)
        else:
            print("This file doesnt exists")
        
    # TODO: renaming, search directory, deleting, copy files

def main():
    terminal = Terminal()

    while True:
        try:
            user_input = input("Enter a command\n"
                            ">> ")
            
            if user_input.lower() == "exit":
                break
            
            if user_input in terminal.commands:
                terminal.commands[user_input]()
            else:
                print("Incorrect command, enter \"help\" for list of available commands\n"
                    "Or enter \"Exit\" to exit terminal")
        except EOFError:
            print("Exiting...")
            sleep(1)
            break
        except KeyboardInterrupt:
            print("Incorrect command!")
            
            
            
            
            
if __name__ == "__main__":
    main()

