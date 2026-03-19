CREATE DATABASE event_reminder_db;

USE event_reminder_db;

CREATE TABLE events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Demo Data
INSERT INTO events (title, description, event_date, event_time)
VALUES 
('Project Submission', 'Submit Python Project to College', '2026-02-20', '10:00:00'),
('Doctor Appointment', 'Annual Health Checkup', '2026-02-18', '18:30:00'),
('Friend Birthday', 'Buy Gift and Wish', '2026-02-25', '00:00:00');

