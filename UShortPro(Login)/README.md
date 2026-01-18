# URL Shortener Web App

A simple Flask-based URL shortener application With Register,Login and Logout features.

## Features
- Shorten long URLs to short codes
- Store and view history of shortened URLs
- Validate URLs before shortening
- Responsive UI with Bootstrap

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   python app.py
   ```

3. Open http://127.0.0.1:5000 in your browser.

## Usage
- Go to the home page, enter a URL, and click "Shorten URL".
- The shortened URL will be displayed.
- Visit the History page to see all shortened URLs.

## Database
- Uses SQLite (urls.db) for storage.
- Tables are created automatically on first run.