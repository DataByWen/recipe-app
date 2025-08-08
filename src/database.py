import mysql.connector
from mysql.connector import Error
from typing import Union

"""A DatabaseInsertFetch object is instantiated only when adding to or fetching from the database. This ensures the connection is created only when needed."""

class DatabaseInsertFetch():

    def __init__(self, action: str, combobox_choice: str, entry_name, entry_link):
        self.action = action.lower()
        self.combobox_choice = combobox_choice
        self.entry_name = entry_name
        self.entry_link = entry_link
        self.db_name = "test_db" # TODO: edit database name

        self.connection = None
        self.cursor = None

        self._transform()


    # the __enter__ and __exit__ are special methods that define how an object should behave when it is used together with a context manager
    def __enter__(self):
        """Connects to the database and returns the object itself. The return value of __enter__ is assigned to the variable after "as" in a context manager"""
        self.db_connect()
        return self

    # ensures  database connection is always properly closed without needing to remember to call db_disconnect() manually
    def __exit__(self, exc_type, exc, tb):
        """Disconnects from the database when with-block ends"""
        self.db_disconnect()

    def _transform(self) -> None:
        """only remove whitespaces when you add in a recipe"""
        if self.action == "add":
            self.entry_name = self.entry_name.strip()
            self.entry_link = self.entry_link.strip()

    def db_connect(self) -> None:
        """Establishes a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host="localhost", 
                user="root",
                password="",  
                database=self.db_name 
            )
            print("Connection to database successful!\n")
        
        except Error as e:
            print(f"Error connecting to database: {e}")

    def db_disconnect(self) -> None:
        if self.cursor: # we don't end up using a cursor to insert into db if recipe name is not provided by user
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")  
    
    def insert_recipe(self) -> Union[str, None]:
        """Inserts a recipe/row into database. Returns error message if any. Returns None if successful."""

        if not self.entry_name.strip(): # if the user doesn't pass in a recipe name, then we can't add to database
            return "Recipe name is required."

        self.cursor = self.connection.cursor()

        # if the entry name and link is already in the db, we return an error message
        query = "SELECT 1 FROM recipes WHERE name = %s AND link = %s LIMIT 1"
        values = (self.entry_name, self.entry_link)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        
        if result:
            return "Recipe has already been added! Please add a new recipe."
        else:
            query = "INSERT INTO recipes (name, type, link) VALUES (%s, %s, %s)"
            values = (self.entry_name, self.combobox_choice, self.entry_link)
            self.cursor.execute(query, values)
            self.connection.commit()
            return None

    def fetch_recipe(self) -> tuple:
        """Fetches a recipe from database given the recipe type provided by the user and returns (name, type, link)"""
        # check if the table contains rows/recipes first
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM recipes;") 
        row_count = self.cursor.fetchone()[0]
        if row_count == 0:
            return (None, None, None) # name, type, link all empty
        
        if self.combobox_choice == "Any": 
            self.cursor.execute(
                """
                SELECT name, type, link 
                FROM recipes
                ORDER BY RAND()
                LIMIT 1;
                """
            )
            query_result = self.cursor.fetchone()

        elif self.combobox_choice == "Protein":
            self.cursor.execute(
                """
                SELECT name, type, link
                FROM recipes
                WHERE type = %s
                ORDER BY RAND()
                LIMIT 1
                """,
                ("Protein",)
            )
            query_result = self.cursor.fetchone()

        else: 
            self.cursor.execute(
                """
                SELECT name, type, link
                FROM recipes
                WHERE type = %s
                ORDER BY RAND()
                LIMIT 1
                """,
                ("Spicy",)
            )
            query_result = self.cursor.fetchone()

        return query_result
        