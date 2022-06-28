from tkinter import *
import os
import time
import configparser

class Window_save_credentials():

    def __init__(self, window_title, logo_path, credentials_file_path, label_mastr_nr, label_mastr_token) -> None:
        self.top = Toplevel()
        self.top.title(window_title)
        self.top.iconbitmap(logo_path)

        self.credentials_file_path = credentials_file_path
        
        e1 = Entry(self.top)
        e2 = Entry(self.top)
        e1_label = Label(self.top, text="Enter MaStR-number: ")
        e2_label = Label(self.top, text="Enter MaStR-token: ")
        e1_label.grid(row=0, column=0)
        e2_label.grid(row=1, column=0)
        e1.grid(row=0, column=1, padx=30)
        e2.grid(row=1, column=1, padx=30)
        mastr_nr, mastr_token = read_credentials(credentials_file_path)
        e1.insert(0, mastr_nr)
        e2.insert(0, mastr_token)

        # First step: Creating a Label Widget
        my_button = Button(self.top, text="Save", command=lambda: self.save_credentials(e1, e2, label_mastr_nr, label_mastr_token))

        # Put label on grid
        my_button.grid(row=2, column=0)

    def save_credentials(self, e1, e2, label_mastr_nr, label_mastr_token):
        file_path = self.credentials_file_path
        global mastr_number
        global mastr_token
        mastr_number = e1.get()
        mastr_token = e2.get()
        if os.path.exists(file_path):
            os.remove(file_path)
        with open(file_path, "w") as file:
            file.write(
                "[MaStR] \n"
                f"user = {mastr_number}\n"
                f"token = {mastr_token}\n"
            )
        label_mastr_nr.config(text=f"MaStR-Nr.: {mastr_number}")
        label_mastr_token.config(text=f"Token: {mastr_token}")
        time.sleep(.3)
        self.top.destroy()

def read_credentials(credentials_file_path):
    config = configparser.ConfigParser()
    config.read(credentials_file_path)
    mastr_nr = config["MaStR"]["user"]
    mastr_token = config["MaStR"]["token"]

    return mastr_nr, mastr_token



