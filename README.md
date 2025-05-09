# Grocery Store Django Web Application 🛒

A role-based grocery store management web application built with **Django**, featuring customer/staff login, product management, basket approvals, and purchase history tracking.

---

## 🧩 Project Overview

This project was developed as part of a final exam to demonstrate proficiency in:

- Django MVT architecture
- Role-based access control
- Form handling and validation
- Bootstrap 5 responsive design
- Session and authentication management

---

## 🚀 Features

### 👥 User Roles
- **Customer**:
  - Sign up and log in
  - Add products to basket
  - View basket and purchase history
  - Change password
- **Staff**:
  - Log in
  - Add/update product information
  - View all customers' baskets
  - Approve or deny customer baskets

### 🛠 Admin (Django Admin)
- Superuser can access `/admin/` panel to manage all models.

---

## ⚙️ Tech Stack

- **Language**: Python 3.12
- **Framework**: Django 5.2
- **Styling**: Bootstrap 5
- **Database**: SQLite3 (default Django DB)
- **Version Control**: Git & GitHub

---

## 📁 Project Structure (Simplified)

```
grocery_store/
├── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           ├── signup.html
│           ├── password_change.html
│           └── password_change_done.html
│
├── basket/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── basket/
│           ├── add_to_basket.html
│           ├── all_baskets.html
│           ├── my_basket.html
│           └── purchase_history.html
│
├── products/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── products/
│           ├── product_list.html
│           ├── product_create.html
│           └── product_update.html
│
├── grocery_store/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   ├── home.html
│   └── master.html
│
├── db.sqlite3
├── manage.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 💻 How to Run the Project Locally

```bash
# 1. Clone the repo
git clone https://github.com/Changgwon-Cho/grocery_store.git
cd grocery_store

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional for admin access)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Access the app at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ✅ Credentials for Testing (Optional)

```
Username: testuser  
Password: testpass123
```

---

## 📝 Author

- **Name**: Changgwon Cho (Jay)
- **School**: Tamwood Careers – Web Development
- **Date**: May 2025

---

## 🧠 Future Improvements

- Add product image support
- Export purchase history to CSV
- Email notifications on basket approval

---

## 📜 License

This project is for educational use only.