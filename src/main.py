from app_ui import RecipeApp
import tkinter as tk


def main():
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
