from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import controller

# path C:\Users\nicag\Desktop\GitHub\Autonomous_Agents

directory = filedialog.askdirectory()



# FONTS
TIMER_FONT = ("Open Sans", 30)
BUTTON_FONT = ("Open Sans", 20, 'bold')
LETTER_LABEL_FONT = ("Open Sans", 20)
ENTRY_FONT = ("Open Sans", 18)
ENTRY_FONT_WIN =  ("Open Sans", 18, 'bold')

# WIDGET DIMENSIONS
BUTTON_HEIGHT = 18
BUTTON_WIDTH = 90

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Country Speedrun")
        self.resizable(False, False)
        
        self.grid_columnconfigure((0,1,2,3), weight=1)


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()

