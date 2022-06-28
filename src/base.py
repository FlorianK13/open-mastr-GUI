from tkinter import *

from os.path import expanduser
import os
from utils.handle_credentials import Window_save_credentials, read_credentials
from utils.handle_download import start_download
import configparser

logo_path = "C:\\Users\\kotthoff\\Documents\\Course Material\\TKinter_Codemy\\img\\logo_open_mastr.ico"
window_title = "open-MaStR Desktop"
credentials_file_path = os.path.join(
    expanduser("~"), ".open-MaStR", "config", "credentials2.cfg"
)

root = Tk()
root.title(window_title)
root.iconbitmap(logo_path)
root.geometry("400x400")


"""Frame Credentials"""
frame_credentials = Frame(root, padx=10, pady=10)
frame_credentials.pack(padx=5, pady=5)

mastr_nr, mastr_token = read_credentials(credentials_file_path)
label_mastr_nr = Label(frame_credentials, text=f"MaStR-Nr.: {mastr_nr}")
label_mastr_token = Label(frame_credentials, text=f"Token: {mastr_token}")

label_mastr_nr.grid(row=0, column=0)
label_mastr_token.grid(row=1, column=0)

save_credentials_button = Button(
    frame_credentials,
    text="Edit MaStR Credentials",
    command=lambda: Window_save_credentials(
        window_title=window_title,
        logo_path=logo_path,
        credentials_file_path=credentials_file_path,
        label_mastr_nr=label_mastr_nr,
        label_mastr_token=label_mastr_token,
    ),
)
save_credentials_button.grid(row=2, column=0)


"""Frame Download"""
frame_download = Frame(root, padx=10, pady=10)
frame_download.pack(padx=5, pady=5)

download_button = Button(
    frame_download,
    text="Download MaStR",
    command=lambda: start_download(),
)
download_button.grid(row=2, column=0)


# Create event loop
root.mainloop()
