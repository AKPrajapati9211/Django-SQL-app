###📚 Student Management System

The Student Management System is a backend-focused Django web application built using Django’s Inbuilt Authentication (DIA) system and SQL database integration.
It provides separate authentication and role-based access for Students, Staff, Admin, and Superusers, enabling secure CRUD-based student data management.

##🚀 Features
#🔐 Authentication & Roles (Django Inbuilt Auth)

Separate login pages for:

👨‍🎓 Students

👨‍💼 Admin / Staff

Role-based access and permissions using DIA

Admin can:

Add staff members

Assign CRUD permissions

Promote staff to superuser

Revoke superuser privileges or modify status

🧑‍🎓 Student Module

Student registration via signup form

Students can log in and access their dashboard

Students can only view their own details

👨‍💼 Staff / Admin Module

Staff login with assigned permissions

Access to Admin Dashboard

View list of all students and their details

Perform CRUD operations based on granted permissions

🗄️ Data & Backend

SQL database integration

Backend-only implementation

Minimal frontend (HTML only; no CSS/JS frameworks)

🛠️ Tech Stack

Backend: Django (Django Inbuilt Authentication)

Database: SQL (MySQL / SQLite)

Language: Python

Templates: HTML (no frontend libraries)

Role Management: Django Permissions & Superuser System

📂 Project Structure (Key Modules)
StudentManagementSystem/
│
├── students/         # Student module & dashboard
├── staff/            # Staff & admin dashboard
├── accounts/         # Authentication & role handling
├── templates/        # HTML templates
├── manage.py
└── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/student-management-system.git
cd student-management-system

2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3️⃣ Run Migrations
python manage.py migrate

4️⃣ Create Superuser
python manage.py createsuperuser

5️⃣ Start Development Server
python manage.py runserver

👥 User Roles & Access
Role	Access	Description
Student	View self profile	Dashboard with personal details
Staff	CRUD (based on permissions)	Manage student records
Admin	Manage staff & permissions	Full access to student data
Superuser	Full system control	Can promote/remove superusers
🔑 Authentication Workflow

Separate login pages for Student and Admin/Staff

Admin can:

Add Staff

Assign CRUD permissions via Django Admin

Promote Staff → Superuser

Revoke Superuser or modify privileges

🧾 Future Enhancements (Optional)

UI improvements using Bootstrap

Attendance & result modules

API integration (REST Framework)

Activity logs / audit trail

🤝 Contribution

Contributions are welcome!
Feel free to:

Fork the repo

Create a feature branch

Submit a pull request

📄 License

This project is for learning and development purposes.
You may modify and use it as needed.

⭐ Show Support

If you found this project helpful, don’t forget to ⭐ the repository!
