"# Python-Student-Records-Management-System" 
# Python-Student-Records-Management-System

## Overview

The Student Records Management System is a Django-based web application designed to manage student records, including personal details and marks. It provides an admin interface for managing students, subjects, and marks, as well as a user interface for viewing and editing student information.

## Features

- Add, edit, and delete student records
- Add, edit, and delete marks for students
- View detailed information about students and their marks
- Admin interface for managing students, subjects, and marks
- User-friendly interface with Bootstrap styling

## Project Structure

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Student-Records-Management-System.git
    cd Student-Records-Management-System
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv student_Environment
    source student_Environment/Scripts/activate  # On Windows
    # source student_Environment/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

### Admin Interface

1. Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
2. Use the admin interface to manage students, subjects, and marks.

### User Interface

1. Go to `http://127.0.0.1:8000/` to view the list of students.
2. Use the navigation bar to add new students or marks.
3. Click on a student's name to view detailed information and manage their marks.

## Models

### Student

- [first_name](http://_vscodecontentref_/26): CharField
- [last_name](http://_vscodecontentref_/27): CharField
- [date_of_birth](http://_vscodecontentref_/28): DateField
- [email](http://_vscodecontentref_/29): EmailField (unique)
- [phone_number](http://_vscodecontentref_/30): CharField (optional)

### Subject

- [name](http://_vscodecontentref_/31): CharField (unique)

### Mark

- [student](http://_vscodecontentref_/32): ForeignKey to Student
- [subject](http://_vscodecontentref_/33): ForeignKey to Subject
- [marks_obtained](http://_vscodecontentref_/34): DecimalField (validators for 0-100)

## Forms

### StudentForm

- Fields: [first_name](http://_vscodecontentref_/35), [last_name](http://_vscodecontentref_/36), [date_of_birth](http://_vscodecontentref_/37), [email](http://_vscodecontentref_/38), [phone_number](http://_vscodecontentref_/39)

### MarkForm

- Fields: [student](http://_vscodecontentref_/40), [subject](http://_vscodecontentref_/41), [marks_obtained](http://_vscodecontentref_/42)
- Validation: Marks must be between 0 and 100

## Views

### Student Views

- [StudentListView](http://_vscodecontentref_/43): List all students
- [StudentDetailView](http://_vscodecontentref_/44): View details of a student
- [StudentCreateView](http://_vscodecontentref_/45): Create a new student
- [StudentUpdateView](http://_vscodecontentref_/46): Edit an existing student
- [StudentDeleteView](http://_vscodecontentref_/47): Delete a student

### Mark Views

- [MarkCreateView](http://_vscodecontentref_/48): Add a new mark
- [MarkDetailView](http://_vscodecontentref_/49): View details of a mark
- [MarkDeleteView](http://_vscodecontentref_/50): Delete a mark

## Templates

- [base.html](http://_vscodecontentref_/51): Base template with navigation
- [student_list.html](http://_vscodecontentref_/52): List of students
- [student_detail.html](http://_vscodecontentref_/53): Student details
- [student_form.html](http://_vscodecontentref_/54): Form for creating/editing students
- [student_confirm_delete.html](http://_vscodecontentref_/55): Confirmation for deleting a student
- [mark_form.html](http://_vscodecontentref_/56): Form for creating/editing marks
- [mark_detail.html](http://_vscodecontentref_/57): Mark details
- [mark_confirm_delete.html](http://_vscodecontentref_/58): Confirmation for deleting a mark

## License

This project is licensed under the MIT License. See the LICENSE file for details.