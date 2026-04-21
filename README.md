# 📝 Django Blog Application

A full-featured blogging platform built using Django, implementing real-world backend concepts like authentication, role-based access control, CRUD operations, and deployment.

## 🚀 Overview

This project is a production-style blog system where users can create, manage, and interact with blog content. It demonstrates practical Django development with a clean architecture and scalable structure.

---

## 🔥 Features

- 👥 Multi-role system (Admin / Manager / Editor / Author)
- ✍️ Create, Read, Update, Delete (CRUD) operations for blog posts and categories
- 🔐 Authentication (Login / Logout / Registration)
- 🛡️ Role-based Authorization using Django Groups & Permissions
- 💬 Comment system (only for authenticated users)
- 🧠 Search functionality with query retention
- 📊 Dashboards for Managers & Editors
- 🖼️ Image upload (Media handling)
- 🔗 SEO-friendly unique slug generation
- 📄 Pagination for blog posts
- ⚙️ Admin panel customization

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Database: SQLite (Development) 
- Frontend: HTML, CSS, Bootstrap

---

## 📁 Project Structure

blog_project/
│── blog/
│── users/
│── templates/
│── static/
│── media/
│── manage.py


---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/your-username/django-blog.git
cd django-blog

Create virtual environment


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt
Run migrations
python manage.py migrate
Create superuser
python manage.py createsuperuser
Run the server
python manage.py runserver
🔑 Roles & Permissions
Admin → Full control
Manager → Manage posts, users, dashboards
Editor → Edit and review content
Author → Create and manage own posts



For more details contact:
Aryan
flexaryan123@gmail.com
8299879214

📚 Learning Outcomes
Practical Django project structure
Authentication & authorization
Database relationships & models
Real-world backend logic
Deployment workflow
