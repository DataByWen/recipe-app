from tkinter import ttk
from database import DatabaseInsertFetch

"""The second window that pops up"""

class AddRecipeUI:
    def __init__(self, root, result_label, parent_recipe_app):
        self.root = root
        self.parent_recipe_app = parent_recipe_app 
        
        self.back_button = ttk.Button(root, text="⬅ Back", command=self.go_back)
        self.back_button.pack(anchor="w", pady=10, padx=10, ipadx=10, ipady=10)

        recipe_label = ttk.Label(root, text="Enter recipe name: ")
        recipe_label.pack(pady=4)

        self.entry_recipe = ttk.Entry(root, width=40)
        self.entry_recipe.pack(pady=2)

        type_label = ttk.Label(root, text="Select recipe type: ")
        type_label.pack(pady=5)

        self.combo_box = ttk.Combobox(root, values=["Spicy", "Protein", "Any"], state="readonly")
        self.combo_box.pack(pady=5)

        link_label = ttk.Label(root, text="Enter link: ")
        link_label.pack(pady=5)

        self.entry_link = ttk.Entry(root, width=40)
        self.entry_link.pack(pady=5)

        self.add_button = ttk.Button(root, text="Add Recipe", command=self.add_recipe)
        self.add_button.pack(pady=10, ipadx=50, ipady=50)

        self.result_label = result_label
        self.result_label.pack()

    def go_back(self):
        """Clear the UI and goes back to main window"""
        for widget in self.root.winfo_children():
            widget.pack_forget()

        self.parent_recipe_app.create_main_ui()
        

    def add_recipe(self):
        '''
        1) Configure the recipe and link added. 2) Also adds to the database
        '''
        type_ = self.combo_box.get()
        name = self.entry_recipe.get()
        link = self.entry_link.get()

        with DatabaseInsertFetch("add", type_, name, link) as db_obj:
            error = db_obj.insert_recipe()  # returns a string if there is an error. else, None is returned
            if error:
                self.result_label.config(text=error)
            else:
                self.result_label.config(text=f"Recipe '{name}' added to database!")
