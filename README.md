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
- 📄 Testing with `pytest` (in progress)
- 🌐 Interactive docs via Swagger: `http://localhost:8000/docs`
  
- 📦 Tech Stack:
  - Backend: FastAPI, PostgreSQL (SQLAlchemy), JWT, Pydantic
  - Frontend: React, Redux (in progress)




Project's lucidchart schema:

<img width="770" alt="Screenshot 2025-05-09 at 16 00 09" src="https://github.com/user-attachments/assets/e6b61d5b-fbaf-43cf-8586-f36a2a570b73" />

*green fields are optional*


Project's folder hierarchy:

<img width="645" alt="Screenshot 2025-05-11 at 11 47 23" src="https://github.com/user-attachments/assets/f29ceee6-4af9-4085-8f5d-8cc1b90f08e3" />


