# 🎓 Student Management System

A web-based Student Management System developed with **Python and Django** to simplify student record management and academic organization.

## 📌 Overview

This project provides a web interface for managing student information, organizing academic years and specialities, and handling study options.

It was developed as a practical project to apply web development, database management, and backend programming concepts.

## ✨ Features

* 👨‍🎓 Student record management
* 🏫 Academic year management
* 📚 Speciality and study option organization
* 🔎 Student search functionality
* 📝 Student registration through a web form
* 🗄️ Database integration using SQLite
* ⚙️ Django Admin integration for data administration

## 🛠️ Technologies Used

* **Backend:** Python, Django
* **Database:** SQLite
* **Frontend:** HTML, CSS, JavaScript
* **Styling:** Tailwind CSS

## 📂 Project Structure

```text
gestion-etudiants/
├── gestion_etudiants/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── etudiants/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd gestion-etudiants
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open your browser at:

`http://127.0.0.1:8000/`

## 🗄️ Database

The project uses SQLite as its database engine and Django ORM for database operations.

Database models include:

* **Etudiant:** Student information
* **Annee:** Academic years
* **Specialite:** Academic specialities
* **Option:** Study options associated with specialities

## 🎯 Project Objectives

* Practice Django application development.
* Design and manage relational database models.
* Implement CRUD-related functionality.
* Build a web interface connected to a database.
* Use Git and GitHub for source code management.

## 🔮 Future Improvements

* Add student profile editing and deletion.
* Improve authentication and user permissions.
* Add pagination and advanced search filters.
* Export student records to CSV or Excel.
* Improve responsive design and user experience.
* Add automated tests.

## 👨‍💻 Author

Developed as a practical web development project using Python and Django.

---

*This project is intended for educational and portfolio purposes.*
