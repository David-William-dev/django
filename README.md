# 📝 Django Blog Application

![Status](https://img.shields.io/badge/Status-Under%20Development-yellow)

A simple, clean, and modular **Django Blog** project built using Django,
Django Templates, and Django ORM.\
Supports both **SQLite** (default) and **MySQL**, and includes a
**custom data population script** using Django `management/commands`.

## 🌟 Features

-   Create, edit, delete blog posts\
-   Category-based filtering\
-   Responsive UI using Django Templates\
-   Django Admin customization\
-   SQLite (default) or MySQL support\
-   Reusable population script for seeding initial data\
-   Clean and modular folder structure

## 📁 Project Structure

    project_root/
    ├── blog/                 # Main blog app
    │   ├── migrations/
    │   ├── management/
    │   │   └── commands/
    │   │       └── pop_category.py   # Custom population script
    │   ├── templates/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── admin.py
    │
    ├── project/              # Django project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── db.sqlite3
    ├── manage.py
    └── README.md

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

``` bash
[git clone https://github.com/yourusername/your-django-blog.git](https://github.com/David-William-dev/django.git)
cd your-django-blog
```

### 2️⃣ Create & Activate Virtual Environment

#### On Linux / macOS:

``` bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

``` bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

## 🗄️ Database Setup (SQLite & MySQL)

### 🧩 Option A --- SQLite (Default)

``` python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

Run:

``` bash
python manage.py migrate
```

### 🗂️ Option B --- MySQL

Install:

``` bash
pip install mysqlclient
```

Update settings:

``` python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_db_name",
        "USER": "your_mysql_user",
        "PASSWORD": "your_mysql_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

Run:

``` bash
python manage.py migrate
```

## 🧪 Running the Population Script

Run:

``` bash
python manage.py pop_category
```

Ensure `management/` and `commands/` contain `__init__.py`.

## 🚀 Run the Development Server

``` bash
python manage.py runserver
```

## 🔐 Create Superuser

``` bash
python manage.py createsuperuser
```

## 📜 License

Add a LICENSE file such as MIT.
