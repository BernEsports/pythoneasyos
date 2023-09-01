import os
from time import sleep


# TODO: Commands: help (list of all commands), creating folders, txt files

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
            "rdtxt": self.read_txt
        }

    def show_help(self):
        for command in self.commands:
            print(command)

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
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
        else:
            print("Incorrect path")

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

def main():
    terminal = Terminal()

    while True:
        user_input = input("Enter a command\n"
                           ">> ")
        
        if user_input.lower() == "exit":
            break
         
        if user_input in terminal.commands:
            terminal.commands[user_input]()
        else:
            print("Incorrect command, enter \"help\" for list of available commands\n"
                  "Or enter \"Exit\" to exit terminal")
        
if __name__ == "__main__":
    main()

