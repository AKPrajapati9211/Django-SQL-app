# 📚 Student Management System

The **Student Management System** is a backend-focused Django web application that uses **Django’s Inbuilt Authentication (DIA)** system with **SQL database integration**.  
It provides separate authentication and role-based access for **Students, Staff/Admin, and Superusers**, enabling secure CRUD-based management of student data.

---

## 🚀 Features

### 🔐 Authentication & Roles (Django Inbuilt Auth)
- Separate login pages for:
  - 👨‍🎓 **Students**
  - 👨‍💼 **Admin / Staff**
- Role-based permissions using Django Authentication System
- Admin can:
  - Add staff members
  - Assign CRUD permissions
  - Promote any staff member to **superuser**
  - Revoke or modify superuser status

### 👨‍🎓 Student Module
- Student registration via signup form
- Login using DIA authentication
- Student Dashboard
- Students can view **only their own details**

### 👨‍💼 Staff / Admin Module
- Staff login with assigned permissions
- Admin Dashboard
- View all student details
- Perform CRUD operations based on granted permissions

### 🗄️ Backend & Data
- SQL database
- Backend-only project
- Minimal UI using only HTML (no CSS/JS frameworks)

---

## 🛠️ Tech Stack

- **Framework:** Django
- **Auth System:** Django Inbuilt Authentication (DIA)
- **Database:** SQL (SQLite / MySQL)
- **Language:** Python
- **Templates:** HTML
- **Role Management:** Django Permissions & Superuser System

---

## 📂 Project Structure (Overview)

```
StudentManagementSystem/
│
├── accounts/        # Authentication & role logic
├── students/        # Student module & dashboard
├── staff/           # Staff & admin dashboard
├── templates/       # HTML templates
├── db.sqlite3       # Database (if using SQLite)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/student-management-system.git
cd student-management-system
```

### 2️⃣ Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```

### 3️⃣ Run Migrations
```bash
python manage.py migrate
```

### 4️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 5️⃣ Start Server
```bash
python manage.py runserver
```

---

## 👥 User Roles & Access Control

| Role | Access Level | Description |
|------|-------------|-------------|
| Student | View own details | Student Dashboard |
| Staff | CRUD (permission-based) | Manage student records |
| Admin | Manage staff & permissions | Full student data access |
| Superuser | Full system control | Can promote/remove superusers |

---

## 🔑 Key Highlights

- Separate **Student Login** and **Admin/Staff Login**
- Role-based access using Django permissions
- Admin can assign CRUD access to staff
- Superuser can promote or remove other superusers
- Secure and scalable backend architecture

---

## 🚧 Future Enhancements
- Frontend UI using Bootstrap / Tailwind
- REST API integration (Django REST Framework)
- Attendance & Results module
- Activity logs / audit tracking

---

## 🤝 Contribution
Contributions are welcome — feel free to fork the repo and submit a pull request.

---

## 📄 License
This project is created for learning and backend development purposes.  
You may modify and use it as needed.

---

## ⭐ Support
If you like this project, consider giving the repository a ⭐ on GitHub!
