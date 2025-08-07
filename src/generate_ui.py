import tkinter as tk
from tkinter import ttk
import webbrowser
from database import DatabaseInsertFetch

"""The second window that pops up"""

# an obj of this class has a tk object 
class GenerateRecipeUI:
    # root is the tk object
    def __init__(self, root, result_label, parent_recipe_app):
        self.root = root # parent window of the widgets 
        self.parent_recipe_app = parent_recipe_app

        self.back_button = ttk.Button(root, text="⬅ Back", command=self.go_back)
        self.back_button.pack(anchor="w", pady=10, padx=10, ipadx=10, ipady=10)

        label = ttk.Label(root, text="Select recipe type:")
        label.pack(pady=10)

        self.combo_box = ttk.Combobox(root, values=["Spicy", "Protein", "Any"], state="readonly")
        self.combo_box.pack(pady=5)

        self.generate_button = ttk.Button(root, text="Generate", command=self.generate_recipe)
        self.generate_button.pack(pady=10, ipadx=50, ipady=20)

        self.result_label = result_label
        self.link_label = tk.Label(root, text="", fg="blue", cursor="hand2", font=self.result_label.cget("font"))

        self.result_label.pack() # used to print recipe name
        self.link_label.pack(ipadx=10, ipady=10) # used to print recipe link


    def go_back(self):
        """Clear the UI and rebuild the RecipeApp UI"""

        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.parent_recipe_app.create_main_ui()


    def generate_recipe(self):
        choice = self.combo_box.get()

        with DatabaseInsertFetch("fetch", choice, None, None) as db_obj:
            name, type_, link = db_obj.fetch_recipe() 

        if (choice == "Protein") or (choice == "Spicy"):
            self.result_label.config(text=f"Here is a {choice} recipe!\nName: {name}")
        else:
            self.result_label.config(text=f"Here is a random recipe!\nName: {name}")

        self.link_label.config(text="Click here for the recipe link", fg="blue")
        self.link_label.bind("<Button-1>", lambda e, url=link: self.open_link(url)) # .bind() passes in an unused event object to the function being called


    def open_link(self, url):
        if url:
            webbrowser.open_new_tab(url)    