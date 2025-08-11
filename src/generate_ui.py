import tkinter as tk
from tkinter import ttk
import webbrowser
from database import DatabaseInsertFetch

"""The second window that pops up"""

class GenerateRecipeUI:
    """Creates the UI."""
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

        # used to print recipe name
        self.result_label.pack() # used to print recipe name
        self.link_label.pack(ipadx=10, ipady=10) # used to print recipe link

        self.notes_box = tk.Text(self.root, height=20, width=70) # read-only text box
        self.notes_box.config(state=tk.DISABLED)  # start locked 


    def go_back(self) -> None:
        """Clear the UI and rebuild the RecipeApp UI."""

        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.parent_recipe_app.create_main_ui()


    def generate_recipe(self) -> None:
        """Creates a DatabaseInsertFetch object to retrieve a recipe from the database. Updates labels and the textbox with the correct information."""
        choice = self.combo_box.get()

        with DatabaseInsertFetch("fetch", choice, None, None, None) as db_obj:
            name, type_, link, user_notes = db_obj.fetch_recipe() 

        if (choice == "Protein") or (choice == "Spicy"):
            self.result_label.config(text=f"Here is a {choice} recipe!\nName: {name}")
        else:
            self.result_label.config(text=f"Here is a random recipe!\nName: {name}")

        # Update notes box
        self.notes_box.config(state=tk.NORMAL) # unlock for editing 
        self.notes_box.delete("1.0", tk.END) # clear old text
        self.notes_box.insert("1.0", user_notes or "No notes available.")
        self.notes_box.pack() # now you display the notes
        self.notes_box.config(state=tk.DISABLED) # lock again

        if link:
            self.link_label.config(text="Click here for the recipe link", fg="blue")
            self.link_label.bind("<Button-1>", lambda e, url=link: self.open_link(url)) # .bind() passes in an unused event object to the function being called
        
        # don't display link label if there is link is NULL and clear the previous link
        else: 
            self.link_label.config(text="")


    def open_link(self, url) -> None:
        if url:
            webbrowser.open_new_tab(url)    