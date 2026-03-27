-- #backend>schema.sql

-- ERP Portal Database Schema (PostgreSQL)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users (central auth table)
CREATE TABLE users (
    user_id     UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username    VARCHAR(50) UNIQUE NOT NULL,
    password    VARCHAR(255) NOT NULL,           -- bcrypt hash
    designation VARCHAR(10) NOT NULL              -- 'admin' | 'student'
                CHECK (designation IN ('admin','student')),
    is_active   BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_designation ON users(designation);

-- Admins
CREATE TABLE admins (
    adm_id      UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id     UUID UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    phone       VARCHAR(20),
    email       VARCHAR(100) UNIQUE NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Students
CREATE TABLE students (
    std_id      UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id     UUID UNIQUE NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    enroll_no   VARCHAR(30) UNIQUE NOT NULL,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    phone       VARCHAR(20),
    email       VARCHAR(100) UNIQUE NOT NULL,
    semester    SMALLINT NOT NULL CHECK (semester BETWEEN 1 AND 12),
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_students_enroll ON students(enroll_no);
CREATE INDEX idx_students_semester ON students(semester);

-- Exams
CREATE TABLE exams (
    exam_id     UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    exam_name   VARCHAR(100) NOT NULL,
    year        SMALLINT NOT NULL,
    semester    SMALLINT CHECK (semester BETWEEN 1 AND 12),
    is_active   BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (exam_name, year, semester)
);
CREATE INDEX idx_exams_year ON exams(year);

-- Subjects
CREATE TABLE subjects (
    sub_id      UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sub_code    VARCHAR(20) UNIQUE NOT NULL,
    sub_name    VARCHAR(100) NOT NULL,
    max_marks   SMALLINT NOT NULL DEFAULT 100,
    semester    SMALLINT CHECK (semester BETWEEN 1 AND 12),
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_subjects_semester ON subjects(semester);

-- Marks  (1 row = 1 student x 1 subject x 1 exam)
CREATE TABLE marks (
    mark_id       UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    std_id        UUID NOT NULL REFERENCES students(std_id) ON DELETE CASCADE,
    exam_id       UUID NOT NULL REFERENCES exams(exam_id) ON DELETE CASCADE,
    sub_id        UUID NOT NULL REFERENCES subjects(sub_id) ON DELETE CASCADE,
    marks_obtained SMALLINT NOT NULL CHECK (marks_obtained >= 0),
    created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (std_id, exam_id, sub_id)   -- one row per combo
);
CREATE INDEX idx_marks_student ON marks(std_id);
CREATE INDEX idx_marks_exam    ON marks(exam_id);

-- Auto-update updated_at trigger
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = NOW(); RETURN NEW; END;
$$ LANGUAGE plpgsql;

DO $$ DECLARE t TEXT;
BEGIN FOR t IN SELECT unnest(ARRAY['users','admins','students','exams','subjects','marks'])
LOOP EXECUTE format('CREATE TRIGGER trg_%s BEFORE UPDATE ON %s FOR EACH ROW EXECUTE FUNCTION update_timestamp()', t, t);
END LOOP; END $$;