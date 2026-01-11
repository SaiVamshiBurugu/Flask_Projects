# Problem Statement: URL Shortener Web Application

## Overview
Develop a web-based URL shortener application that allows users to convert long URLs into shorter, more manageable links. The application should provide an intuitive interface for shortening URLs, storing them in a database, and retrieving a history of shortened URLs. The system must ensure URL validity and provide a seamless user experience for copying shortened links.

## Objectives
- **URL Shortening**: Users should be able to input a long URL and receive a shortened version that redirects to the original URL.
- **URL Storage and History**: All shortened URLs, along with their originals, should be saved in a database for user reference.
- **URL Validation**: Implement checks to verify that the entered URL is valid and reachable.
- **User Interface**: Provide a clean, responsive frontend using HTML, CSS, and Bootstrap for URL input, shortening, and history display.
- **Backend Functionality**: Use Flask (Python) as the backend framework, SQLAlchemy as the ORM, and SQLite as the database.

## Key Features
1. **Home Page**:
   - Input field for entering the original URL.
   - "Shorten" button to generate and display the shortened URL.
   - "Copy" button to copy the shortened URL to the clipboard.
   - Display of the shortened URL after processing.

2. **History Page**:
   - List all previously shortened URLs with their original counterparts.
   - Allow users to view and manage their URL history.

3. **URL Validation**:
   - Check if the entered URL is in a valid format (e.g., starts with http:// or https://).
   - Optionally, verify if the URL is reachable by attempting a connection.

4. **Database Integration**:
   - Store original URLs and their shortened versions.
   - Use migrations for database schema management.

## Technical Requirements
- **Frontend**: HTML, CSS, Bootstrap.
- **Backend**: Flask, Python.
- **ORM**: SQLAlchemy.
- **Database**: SQLite.
- **Additional Libraries**: Any necessary for URL validation (e.g., requests for reachability checks).

## Constraints
- The application should be lightweight and run locally or on a simple server.
- Ensure security by validating inputs to prevent malicious URLs.
- Handle edge cases like duplicate URLs or invalid inputs gracefully.

## Expected Outcome
A fully functional URL shortener that simplifies link sharing, with a user-friendly interface and reliable backend storage. Users can shorten URLs, copy them easily, and review their history without hassle.