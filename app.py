from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import controller
from PIL import Image


# FONTS
PDF_FONT_BOLD = ("Opens Sans", 18, 'bold')
DIRECTORY_ENTRY_FONT_BOLD = ("Opens Sans", 20, 'bold')
TITLE_FONT_BOLD = ("Opens Sans", 26, 'bold')

# COLOR 
TITLE_BACKGROUND_COLOR = "#69696b"
BACKGROUND_COLOR = "#868687"
PDF_COLOR = "#851c36"
BUTTON_COLOR = "#fc3265"
BUTTON_HOVER_COLOR = "#991d3c"

# IMAGES
UP_ARROW_IMAGE=ctk.CTkImage(light_image=Image.open("assets/arror_up.jpg"), dark_image=Image.open("assets/arror_up.jpg"), size=((20,20)))
DOWN_ARROW_IMAGE=ctk.CTkImage(light_image=Image.open("assets/arror_down.jpg"), dark_image=Image.open("assets/arror_down.jpg"), size=((20,20)))

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PDF Merger")
        self.geometry("400x650")
        self.resizable(False, False)
        
        self.grid_rowconfigure((0,1,2), weight=1)

        self.pdfs=[]
        self.number_of_pdfs=0

        # FRAMES
        self.title_frame = ctk.CTkFrame(self, corner_radius=0, width=400, height=200, fg_color=TITLE_BACKGROUND_COLOR)
        self.title_frame.grid(row=0, column=0, sticky='nsew')
        self.title_frame.grid_columnconfigure(0, weight=1)

        self.pdfs_frame = ctk.CTkScrollableFrame(self, corner_radius=0, width=400, height=400, fg_color=BACKGROUND_COLOR)
        self.pdfs_frame.grid(row=1, column=0, sticky='nsew')
        self.pdfs_frame.grid_columnconfigure(0, weight=0)

        self.submit_frame = ctk.CTkFrame(self, corner_radius=0, width=400, height=300, fg_color=TITLE_BACKGROUND_COLOR)
        self.submit_frame.grid(row=2, column=0, sticky='nsew')
        self.submit_frame.grid_columnconfigure(0, weight=1)

        # TITLE FRAME WIDGETS
        self.title_label = ctk.CTkLabel(self.title_frame, text="PDF Merger", font=TITLE_FONT_BOLD, justify='center')
        self.title_label.grid(row=0,column=0, sticky='nswe', padx=10, pady=(20,0))

        # PDF FRAMES WIDGETS
        self.add_pdf_button = ctk.CTkButton(self.pdfs_frame, text="+", font=TITLE_FONT_BOLD, width=40, hover_color=BUTTON_HOVER_COLOR, fg_color=BUTTON_COLOR, command=self.add_pdf)
        self.add_pdf_button.grid(row=0,column=0, padx=5, pady=2)

        # SUBMIT FRAMES WIDGETS
        self.entry_variable = ctk.StringVar()
        self.entry_variable.set("result.pdf")

        self.result_name_entry = ctk.CTkEntry(self.submit_frame, placeholder_text="result.pdf", width=250, font=DIRECTORY_ENTRY_FONT_BOLD, textvariable=self.entry_variable)
        self.result_name_entry.grid(row=0, column=0, padx=5, pady=5)

        self.merge_button = ctk.CTkButton(self.submit_frame, text="Merge", height=50, fg_color=BUTTON_COLOR, font=TITLE_FONT_BOLD, hover_color=BUTTON_HOVER_COLOR, command=self.merge)
        self.merge_button.grid(row=1, column=0, padx=5, pady=5)

    def add_pdf(self):
        dir = filedialog.askopenfilename()
        current_pdf = dir.split("/")[-1]
        print(current_pdf)
        print(f"pdf number: {self.number_of_pdfs}")
        self.pdfs.append(current_pdf)
        
        ctk.CTkButton(self.pdfs_frame, text="", image=UP_ARROW_IMAGE, hover_color=BUTTON_HOVER_COLOR, fg_color='transparent', width=15).grid(row=self.number_of_pdfs*2, column=0)
        ctk.CTkButton(self.pdfs_frame, text="", image=DOWN_ARROW_IMAGE, hover_color=BUTTON_HOVER_COLOR, fg_color='transparent', width=15).grid(row=(self.number_of_pdfs*2)+1, column=0)

        ctk.CTkButton(self.pdfs_frame, text=current_pdf, text_color='white', font=PDF_FONT_BOLD, fg_color=PDF_COLOR, width=275, height=40, state=DISABLED, command=self.move_pdf).grid(row=self.number_of_pdfs*2, column=1, rowspan=2, padx=5, pady=3)
        ctk.CTkButton(self.pdfs_frame, text="-", font=TITLE_FONT_BOLD, width=40, height=40, hover_color=BUTTON_HOVER_COLOR, fg_color=BUTTON_COLOR, command=self.remove_pdf).grid(row=self.number_of_pdfs*2, column=2, rowspan=2,padx=5, pady=3)
        self.add_pdf_button.grid(row=(self.number_of_pdfs+1)*2,column=0, padx=5, pady=2)

        self.number_of_pdfs+=1

    def remove_pdf(self):
        self.clear_frame(self.pdfs_frame)
        self.display_pdfs()
        self.number_of_pdfs-=1

    def move_pdf(self):
        pass

    def display_pdfs(self):
        for idx, pdf in enumerate(self.pdfs):
            ctk.CTkButton(self.pdfs_frame, text="", image=UP_ARROW_IMAGE, hover_color=BUTTON_HOVER_COLOR, fg_color='transparent', width=15).grid(row=idx*2, column=0)
            ctk.CTkButton(self.pdfs_frame, text="", image=DOWN_ARROW_IMAGE, hover_color=BUTTON_HOVER_COLOR, fg_color='transparent', width=15).grid(row=(idx*2)+1, column=0)

            ctk.CTkButton(self.pdfs_frame, text=pdf, text_color='white', font=PDF_FONT_BOLD, fg_color=PDF_COLOR, width=275, height=40, state=DISABLED, command=self.move_pdf).grid(row=idx*2, column=1, rowspan=2, padx=5, pady=3)
            ctk.CTkButton(self.pdfs_frame, text="-", font=TITLE_FONT_BOLD, width=40, height=40, hover_color=BUTTON_HOVER_COLOR, fg_color=BUTTON_COLOR, command=self.remove_pdf).grid(row=idx*2, column=2, rowspan=2, padx=5, pady=3)
            self.add_pdf_button.grid(row=(idx+1)*2,column=0, padx=5, pady=2)


    def merge(self):
        print(self.pdfs)
        controller.merge_pdfs(pdfs=self.pdfs)

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()

