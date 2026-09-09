# Job Application Tracker

A beginner-friendly Flask web application for organizing IT Ausbildung and job applications.

## Current features

- SQLite database for application data
- Application list on the main page
- Empty state when no applications exist

Application forms and other features will be added in later milestones.

## Run locally

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:

   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000` in a browser.
