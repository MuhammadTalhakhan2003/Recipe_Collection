
# Recipe Collection

A simple Django-based web application for storing and managing recipes. This project is designed to help users manage their recipes with features like adding, viewing, and editing recipe details.

## Project Overview

This project is built using **Django** and utilizes a SQLite database. It focuses on basic CRUD operations (Create, Read, Update, Delete) for managing recipes.

## Features

- Add, edit, and delete recipes.
- View a list of all recipes.
- Detailed view of each recipe, including ingredients and instructions.

## Tech Stack

- **Backend:** Django 4.2.16
- **Frontend:** HTML, CSS, and Bootstrap
- **Database:** SQLite

## Setup Instructions

### Prerequisites

- Python 3.12.x installed on your system.
- Git for version control.
- Virtual environment (optional but recommended).

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MuhammadTalhakhan2003/Recipe_Collection.git
   cd Recipe_Collection
   ```

2. **Create and activate a virtual environment (optional):**

   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Run the following commands to create the database tables:

   ```bash
   python manage.py makemigrations
   python manage.py makemigrations recipes
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000`.

### Environment Variables

Ensure you set up the `DJANGO_SECRET_KEY` environment variable before running the server:

- On Windows (CMD):

   ```bash
   set DJANGO_SECRET_KEY='your-unique-secret-key'
   ```

- On Windows (PowerShell):

   ```bash
   $env:DJANGO_SECRET_KEY='your-unique-secret-key'
   ```

## Usage

- Visit the `/admin` page to manage recipes (you'll need to create a superuser first using `python manage.py createsuperuser`).
- Add new recipes or edit existing ones from the admin panel.
- Browse recipes through the main interface.

## Commands for Database Setup & Server

- **Make migrations for database:**

   ```bash
   python manage.py makemigrations
   python manage.py makemigrations recipes
   ```

- **Show applied migrations:**

   ```bash
   python manage.py showmigrations
   ```

- **Run the server:**

   ```bash
   python manage.py runserver
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django Documentation
- Bootstrap for styling the frontend
- GitHub for version control and hosting
