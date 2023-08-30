import os


# TODO: Commands: help (list of all commands), creating folders, txt files

# dir = show directory ; chdir = change directory ; crf = create folder


class Terminal:
    def __init__(self):
        self.commands = {
            "help": self.show_help,
            "dir": self.show_dir,
            "chdir": self.change_dir,
            "crf": self.create_folder
        }

    def show_help(self):
        for command in self.commands:
            print(command)

    def show_dir(self):
        print(os.getcwd())
    
    def change_dir(self):
        path_change = input("Enter folder name\n"
                 ">> ")
        if os.path.exists(path_change) == True:
            os.chdir(path_change)
        else:
            print("Directory doesnt exists")
    
    def create_folder(self):
        folder_path = input("Enter folder name\n"
                            ">> ")
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
        else:
            print("Incorrect path")

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
            print("Incorrect command, enter \"help\" for list of available commands")
        
if __name__ == "__main__":
    main()
    
