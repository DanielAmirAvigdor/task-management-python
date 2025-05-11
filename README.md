# 📝 Task Management API

A FastAPI-based backend for managing users, projects, and tasks with full JWT-based authentication and role-based access control.

---

## 🚀 Features

- 🔐 JWT Auth (Login, Register, Protected Routes)
- 👥 Users can:
  - View and update their own profile (`/users/me`)
  - See other users in shared projects
- 📁 Projects:
  - Created by users
  - Participants can be added with roles (admin/user)
  - Admins can edit/delete projects
- ✅ Tasks:
  - Linked to projects and assigned users
  - View/edit/delete only if authorized (assignee or project admin)
- 📦 SQLAlchemy + PostgreSQL
- 📄 Pydantic validation
- 🧪 Ready for testing with `pytest` and `httpx` (in progress)
- 🌐 Interactive docs via Swagger: `http://localhost:8000/docs`



project's lucidchart schema:
<img width="770" alt="Screenshot 2025-05-09 at 16 00 09" src="https://github.com/user-attachments/assets/e6b61d5b-fbaf-43cf-8586-f36a2a570b73" />

backend/
└── app/
├── main.py # FastAPI entry point
├── models/ # SQLAlchemy models
├── routers/ # Route definitions
├── schemas/ # Pydantic schemas
├── logic/ # Business logic layer
├── data/ # DB interaction layer
├── auth/ # JWT, hashing, dependencies
├── utils/ # permissions, helpers, etc...
└── db.py # DB session management
