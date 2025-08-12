# 🍽️ Recipe App
**“Stop overthinking dinner — let your app decide!”**

A GUI-based recipe app built with Tkinter that lets you add new recipes and generate random recipes from a database. Perfect for when you’re hungry but indecisive.

## Motivation
I often spend way too much time trying to decide what to eat, scrolling through recipe websites, and searching old bookmarks. This app was born out of the need to make that process faster, simpler, and a little more fun. To save time (and avoid decision fatigue), I decided to build an app that stores my favorite recipes and can randomly suggest one with a single click.

## App Video Demo
https://github.com/user-attachments/assets/ff23916a-650a-4826-b525-f2a64e660185

## Tech Stack
* Python — Core programming language.
* Tkinter — For creating the GUI.
* MySQL — Stores and retrieves recipes.

## Installation
1. Clone the repository:  ```git clone https://github.com/yourusername/recipe-generator-app.git```
2. Change to the directory: ```cd recipe-generator-app```
3. Install dependencies: ```pip install mysql-connector-python```
4. Open your MySQL client or terminal and run:  
```sql
CREATE DATABASE test_db;
USE test_db;
SOURCE sql/schema.sql;
```
5. Run the app: ```python src/main.py```






