# ERP Portal — Academic Management System

> A full-stack academic ERP built with **FastAPI** + **PostgreSQL** on the backend and **Streamlit** on the frontend. Role-based access, JWT authentication, and a modern dark-glass UI.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Environment Variables](#environment-variables)
- [API Reference](#api-reference)
- [Database Schema](#database-schema)
- [System Flow](#system-flow)
- [Challenges & Solutions](#challenges--solutions)
- [Future Roadmap](#future-roadmap)
- [Author](#author)

---

## Overview

The **ERP Portal** is a full-stack application designed to manage student academic records for an institution. It provides a clean separation of roles - administrators manage all data, while students securely access their own results.

The backend exposes a RESTful API with JWT-protected endpoints. The frontend is a dark-glass Streamlit dashboard that consumes the API directly.

---

## Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Backend    | FastAPI, Python 3.11                |
| Database   | PostgreSQL 16                       |
| ORM        | SQLAlchemy 2.0                      |
| Auth       | JWT (python-jose), bcrypt (passlib) |
| Frontend   | Streamlit ≥ 1.35                    |
| Server     | Uvicorn                             |

---

## Features

### Authentication
- JWT Bearer token login
- Role-based access control — `admin` and `student`
- Bcrypt password hashing
- Token expiry and validation

### Admin
- Create and list students (with enroll number, email, semester)
- Create and list exams (name, year, semester, active flag)
- Create and list subjects (code, name, max marks, semester)
- Enter marks per student × exam × subject

### Student
- Secure login with their own credentials
- View marksheet filtered by exam
- Automatic percentage, grade, and pass/fail calculation
- Download marksheet as PDF

### System
- UUID primary keys throughout
- Unique constraint enforcement (no duplicate marks)
- Input validation — marks range, required fields
- Modular layered backend (router → service → model)

---

## Architecture

```
Request → FastAPI Router → Service Layer → SQLAlchemy ORM → PostgreSQL
                                ↓
                         Pydantic Schema (validation)
                                ↓
                         JSON Response → Streamlit UI
```

The backend follows a strict layered pattern:

| Layer      | Responsibility                          |
|------------|-----------------------------------------|
| `routers/` | HTTP endpoints, auth dependencies       |
| `services/`| Business logic, DB queries              |
| `models/`  | SQLAlchemy table definitions            |
| `schemas/` | Pydantic request/response models        |
| `utils/`   | JWT creation/decoding, password hashing |

---

## Project Structure

```
isi-ds-erp-portal/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── student.py
│   │   │   ├── exam.py
│   │   │   ├── subject.py
│   │   │   └── marks.py
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── admin.py
│   │   │   └── student.py
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── admin_service.py
│   │   │   └── student_service.py
│   │   ├── schemas/
│   │   │   ├── student.py
│   │   │   ├── exam.py
│   │   │   ├── subject.py
│   │   │   └── marks.py
│   │   ├── utils/
│   │   │   ├── jwt_handler.py
│   │   │   └── password.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   └── main.py
│   ├── schema.sql
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── components/
│   │   ├── theme.py
│   │   ├── sidebar.py
│   │   ├── header.py
│   │   └── ui.py
│   ├── views/
│   │   ├── login.py
│   │   ├── admin_dashboard.py
│   │   ├── admin_students.py
│   │   ├── admin_exams.py
│   │   ├── admin_subjects.py
│   │   ├── admin_marks.py
│   │   └── student_marksheet.py
│   ├── utils/
│   │   └── api_client.py
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## Setup & Installation

### Prerequisites

- Python 3.11+
- PostgreSQL 16
- Git

---

### 1. Clone the Repository

```bash
git clone https://github.com/Kajalmishra8/isi-ds-erp-portal.git
cd isi-ds-erp-portal
```

---

### 2. Backend Setup

```bash
cd backend
py -3.11 -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

### 3. Database Setup

Create the database and run the schema:

```bash
psql -U postgres -c "CREATE DATABASE erp_db;"
psql -U postgres -d erp_db -f schema.sql
```

The schema creates all tables, indexes, unique constraints, and auto-update triggers.

---

### 4. Environment Variables

Create `backend/.env`:

```env
DATABASE_URL=postgresql://erp_user:secret@localhost:5432/erp_db
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
APP_NAME=ERP Portal
DEBUG=False
```

---

### 5. Run the Backend

```bash
uvicorn app.main:app --reload
```

API available at: `http://localhost:8000`  
Swagger docs at: `http://localhost:8000/docs`

---

### 6. Frontend Setup

```bash
cd ../frontend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create `frontend/.streamlit/secrets.toml`:

```toml
API_BASE_URL = "http://localhost:8000"
```

Run the frontend:

```bash
streamlit run app.py
```

Frontend available at: `http://localhost:8501`

---


## Environment Variables

| Variable                      | Description                     | Default       |
|-------------------------------|---------------------------------|---------------|
| `DATABASE_URL`                | PostgreSQL connection string    | Required      |
| `SECRET_KEY`                  | JWT signing secret              | Required      |
| `ALGORITHM`                   | JWT algorithm                   | `HS256`       |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime in minutes       | `60`          |
| `APP_NAME`                    | Application display name        | `ERP Portal`  |
| `DEBUG`                       | Enable debug mode               | `False`       |

---

## API Reference

### Authentication

| Method | Endpoint          | Description         | Auth     |
|--------|-------------------|---------------------|----------|
| `POST` | `/api/auth/login` | Login, get JWT token | None    |

### Admin Endpoints

All admin routes require a valid JWT with `designation = admin`.

| Method | Endpoint                   | Description              |
|--------|----------------------------|--------------------------|
| `GET`  | `/api/admin/dashboard`     | Stats overview           |
| `POST` | `/api/admin/students`      | Create a student         |
| `GET`  | `/api/admin/students`      | List students (paginated)|
| `POST` | `/api/admin/exams`         | Create an exam           |
| `GET`  | `/api/admin/exams`         | List all exams           |
| `POST` | `/api/admin/subjects`      | Create a subject         |
| `GET`  | `/api/admin/subjects`      | List all subjects        |
| `POST` | `/api/admin/marks`         | Enter marks              |
| `GET`  | `/api/admin/marks/recent`  | Recent mark entries      |

### Student Endpoints

All student routes require a valid JWT with `designation = student`.

| Method | Endpoint                   | Description                  |
|--------|----------------------------|------------------------------|
| `GET`  | `/api/student/exams`       | List active exams for student|
| `GET`  | `/api/student/marksheet`   | Get marksheet by exam        |

---

## Database Schema

### Tables

| Table      | Primary Key | Key Fields                                         |
|------------|-------------|-----------------------------------------------------|
| `users`    | `user_id`   | username, password (bcrypt), designation, is_active |
| `admins`   | `adm_id`    | user_id (FK), first_name, last_name, email          |
| `students` | `std_id`    | user_id (FK), enroll_no, email, semester            |
| `exams`    | `exam_id`   | exam_name, year, semester, is_active                |
| `subjects` | `sub_id`    | sub_code, sub_name, max_marks, semester             |
| `marks`    | `mark_id`   | std_id (FK), exam_id (FK), sub_id (FK), marks_obtained |

### Key Constraints

- `marks (std_id, exam_id, sub_id)` — unique constraint prevents duplicates
- `students.enroll_no` — unique
- `students.email` — unique
- `users.username` — unique
- `subjects.sub_code` — unique

---

## System Flow

```
User visits http://localhost:8501
        │
        ▼
    Login Page
        │  POST /api/auth/login
        ▼
  JWT Token returned
        │
        ├── role = admin  ──▶  Admin Dashboard
        │                          ├── Students
        │                          ├── Exams
        │                          ├── Subjects
        │                          └── Marks Entry
        │
        └── role = student ──▶  Student Marksheet
                                   └── View Results by Exam
```

---

## Grading System

| Percentage | Grade |
|------------|-------|
| ≥ 90%      | A+    |
| ≥ 75%      | A     |
| ≥ 60%      | B     |
| ≥ 50%      | C     |
| < 50%      | F     |

Pass threshold: **40%**

---

## Challenges & Solutions

| Challenge                          | Solution                                                                                         |
|------------------------------------|--------------------------------------------------------------------------------------------------|
| UUID serialisation in API          | Used `str(uuid)` in token payload; parsed back with `uuid.UUID()` in dependencies                |
| Streamlit sidebar navigation       | Replaced `st.button` wrappers with native `st.radio()` — the only reliable Streamlit nav pattern |
| `pyarrow.lib` crash on Windows     | Replaced all `st.dataframe()` calls with `st.table()` — zero pyarrow dependency                  |
| Schema mismatch (missing columns)  | Added `ALTER TABLE` migrations for `semester`, `is_active`, `email` columns                      |
| JWT role mapping                   | Embedded `role` field directly in token payload; frontend reads it on login response             |

---

## Future Roadmap

- [ ] React-based frontend with Vite
- [ ] Advanced analytics dashboard (charts, trends)
- [ ] Bulk marks upload via CSV
- [ ] Email notifications for result release
- [ ] Cloud deployment — AWS ECS or Railway
- [ ] Unit and integration test suite
- [ ] Audit log for admin actions

---

## Author

**Kajal Mishra**  
GitHub: [@Kajalmishra8](https://github.com/Kajalmishra8)  
Project: [isi-ds-erp-portal](https://github.com/Kajalmishra8/isi-ds-erp-portal)

---

*Built with FastAPI · PostgreSQL · Streamlit*
