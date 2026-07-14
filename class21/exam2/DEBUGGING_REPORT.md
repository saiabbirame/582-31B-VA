# Debugging Report

## Bug 1 - Flask and database setup

**File:**
app.py

**Problem:**
The database configuration and setup were not written correctly. The configuration used `SQLALCHEMY_DATABASE_URL` instead of `SQLALCHEMY_DATABASE_URI`, SQLAlchemy was not connected to the Flask app and `app_context` was missing parentheses.

**Fix:**
I changed the configuration to `SQLALCHEMY_DATABASE_URI`, initialized the database with `SQLAlchemy(app)` and changed `app.app_context` to `app.app_context()`.

**Test:**
I restarted the app. It started successfully and showed the local server URL. 