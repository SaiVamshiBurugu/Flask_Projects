# Flask Projects

This repository contains several Flask web applications developed during internship at Innomatics Research Labs.

## Projects

### Note Taking App
A simple web application for taking and displaying notes.

- **Location**: `note_taking_app/`
- **Main file**: `app.py`
- **Template**: `templates/home.html`
- **Additional**: `Debugging_report.pdf` (debugging report)
- **Features**: 
  - Add notes via a form submission
  - Display a list of all added notes

### Regex Tester
A web-based tool to test regular expressions against a test string.

- **Location**: `regex999/`
- **Main file**: `app.py`
- **Templates**: `templates/index.html`, `templates/index_improved.html`
- **Features**: 
  - Input a regular expression pattern
  - Input a test string
  - Find all matches using Python's `re.findall`
  - Display matches or error messages

### Task 1
A basic Flask application that provides personalized greetings.

- **Location**: `Task_1/`
- **Main file**: `app.py`
- **Features**: 
  - Greets users with "Hello Anonymous User!" by default
  - Provides personalized greeting if `username` query parameter is provided (e.g., `/?username=John`)

### URL Shortener
A simple Flask-based URL shortener application.

- **Location**: `UShortPro(NoLogin)/`
- **Main file**: `app.py`
- **Templates**: `templates/index.html`, `templates/layout.html`, `templates/history.html`
- **Features**: 
  - Shorten long URLs to short codes
  - Store and view history of shortened URLs
  - Validate URLs before shortening
  - Responsive UI with Bootstrap

## Setup and Running

Each project is a standalone Flask application. To run any of them:

1. Ensure Python 3.x is installed.
2. Install Flask: `pip install flask`
3. Navigate to the specific project folder (e.g., `cd note_taking_app`)
4. Run the application: `python app.py`
5. Open your browser and go to `http://127.0.0.1:5000/`

## Requirements
- Python 3.x
- Flask (`pip install flask`)

## Repository Structure
```
Flask_projects/
├── note_taking_app/
│   ├── app.py
│   ├── Debugging_report.pdf
│   └── templates/
│       └── home.html
├── regex999/
│   ├── app.py
│   └── templates/
│       ├── index.html
│       └── index_improved.html
├── Task_1/
│   ├── app.py
│   └── templates/
└── UShortPro(NoLogin)/
    ├── app.py
    ├── problem_statement.md
    ├── README.md
    ├── requirements.txt
    ├── templates/
    │   ├── history.html
    │   ├── index.html
    │   └── layout.html
    └── ref/
        ├── app_7/
        └── app_7 (signin)/
```