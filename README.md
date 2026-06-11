# Event Reminder System

A desktop-based Event Reminder System developed using **Python**, **Tkinter**, **MySQL**, and **tkcalendar**. This application allows users to create, manage, search, and track upcoming events while receiving automatic reminders when an event is due.

---

## Features

- Add new events with title, description, date, and time
- Update existing event details
- Delete events from the database
- Search events by title
- View all events in a tabular format
- Dashboard showing upcoming events
- Automatic event reminders with notification popups
- Sound alert when an event time is reached
- MySQL database integration
- User-friendly graphical interface

---

## Technologies Used

- Python 3.x
- Tkinter
- MySQL
- mysql-connector-python
- tkcalendar
- winsound

---

## Project Structure

```text
Event Reminder System/
│
├── event_reminder_app.py
├── event_reminder_app.sql
├── README.md
```

---

## Database Setup

### Step 1: Create Database

```sql
CREATE DATABASE event_reminder_db;
USE event_reminder_db;
```

### Step 2: Create Events Table

```sql
CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(500),
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/event-reminder-system.git
cd event-reminder-system
```

### Install Required Libraries

```bash
pip install mysql-connector-python
pip install tkcalendar
```

---

## Configure Database Connection

Open the Python file and update your MySQL credentials:

```python
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="event_reminder_db"
    )
```

---

## Running the Application

```bash
python event_reminder_app.py
```

---

## Application Modules

### Add Event

- Enter event title
- Enter event description
- Select event date
- Enter event time
- Click **Add Event**

### Update Event

- Select an event from the table
- Modify details
- Click **Update Event**

### Delete Event

- Select an event
- Click **Delete Event**

### Search Event

- Enter event title keyword
- Click **Search**
- Use **Show All** to display all records

### Dashboard

Displays the next upcoming events sorted by date.

### Reminder System

- Checks events every minute
- Displays reminder popup when an event time is reached
- Plays notification sound using Windows Beep

---

## User Interface Components

- Event Dashboard
- Event Entry Form
- Date Picker Calendar
- Search Section
- Events Table
- Reminder Notifications
- Message Boxes

---

## Validation Features

- Event selection validation before update
- Event selection validation before delete
- Database-driven data consistency
- Automatic table refresh after operations

---

## Screenshots

Add screenshots of:

- Main Dashboard
- Add Event Form
- Search Functionality
- Event Table
- Reminder Notification Popup

---

## Future Enhancements

- Email reminders
- SMS notifications
- Event categories
- Recurring events
- Event priority levels
- Export events to Excel
- PDF event reports
- User authentication system
- Dark and Light themes

---

## Learning Outcomes

This project demonstrates:

- Python GUI Development
- MySQL Database Connectivity
- CRUD Operations
- Event Scheduling
- Reminder Automation
- Date and Time Handling
- Desktop Application Development

---

## Author

**Rahul Kulkarni**

Python Developer | MySQL Developer

---

## License

This project is developed for educational and learning purposes only.

---

## Project Overview

The Event Reminder System helps users organize important events and receive timely notifications. The application stores event data in a MySQL database, provides a simple graphical interface for event management, and automatically alerts users when scheduled events occur. It is an excellent project for learning Python GUI programming, database integration, and event scheduling concepts.
