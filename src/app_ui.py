import tkinter as tk
from tkinter import ttk, font
from generate_ui import GenerateRecipeUI
from add_ui import AddRecipeUI

"""The first window that pops up"""

class RecipeApp:
    def __init__(self, root): # root is the tk object 
        self.root = root # Composition: "a RecipeApp obj has a Tk obj"
        self.root.title("Recipe App")
        self.root.geometry("1200x600")

        self.main_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.big_font = font.Font(family="Helvetica", size=16, weight="bold")

        self.create_main_ui()

    def create_main_ui(self):
        self.clear_ui() # clear the ui whenever you go back to the main window

        style = ttk.Style()
        style.configure("Big.TButton", font=self.main_font, padding=(100,100))

        # the text for a label is initially empty until you click on a button. then text for the label is generated
        self.result_label = tk.Label(self.root, text="", font=self.big_font)

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.button_random = ttk.Button(
            self.frame, # the button's parent is frame
            text="Generate Recipe",
            command=self.show_random_ui, 
            width=15,
            style="Big.TButton"
        )
        self.button_random.pack(side="left", padx=30, pady=50)

        self.button_add = ttk.Button(
            self.frame,
            text="Add Recipe",
            command=self.show_add_ui,
            width=15,
            style="Big.TButton"
        )
        self.button_add.pack(side="left", padx=30, pady=50)

    # clear (hide) all the widgets in the root window
    def clear_ui(self):
        for widget in self.root.winfo_children(): 
            if widget is not self.result_label:
                widget.pack_forget()

    def show_random_ui(self):
        self.clear_ui()
        GenerateRecipeUI(self.root, self.result_label, self) # we pass the RecipeApp object itself to GenerateRecipeUI object since we want to reuse this object when we press on the back button

    def show_add_ui(self):
        self.clear_ui()
        AddRecipeUI(self.root, self.result_label, self)