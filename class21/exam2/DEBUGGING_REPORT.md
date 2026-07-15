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

## Bug 2 - Album model and display

**File:**
app.py

**Problem:**
The albums were not displaying because the model and query contained multiple mistakes.

**Fix:**
I changed they `year` column to an integer, changed the stock value to an integer, fixed the `in_stock` proeprty, updated the `__repr__()` method and changed `Album.query.all` to `Album.query.all()`.

**Test:**
I added an album and confirmed that it appeared on the home page.

## Bug 3 - Edit album

**File:**
app.py and edit_album.html

**Problem:**
The edit page did not show the album information correctly and updating an album did not work because some form fiels and redirects were wrong.

**Fix:**
I changed the template to use the correct album attributes, fixed the stock field name, converted the year and stock values to integers, added `db.session.commit() and redirected back to the home page after updating.

**Test:**
I edited an album, changed the stock value and confirmed the updated information appeared on the home page.

## Bug 4 - Delete album

**File:**
app.py and index.html

**Problem:**
Deleting an album did not work correctly because the delete route was missing a commit and the delete action needed to use a POST request.

**Fix:**
I changed the delete route to use POST, added `db.session.commit()` after deleting the album and updated the delete button to submit a form instead of using a link.

**Test:**
I deleted an album and confirmed it was removed from the database and no longer appeared on the home page after refreshing.