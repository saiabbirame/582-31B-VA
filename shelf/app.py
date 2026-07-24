import os
from dotenv import load_dotenv

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import ( LoginManager, current_user, login_required, login_user, logout_user )

from models import db, User, Book

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shelf.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

with app.app_context():
    db.create_all()

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("books"))
    
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        errors = []

        if not username:
            errors.append("Username is required.")

        if not email:
            errors.append("Email is required.")

        if not password:
            errors.append("Password is required.")

        if User.query.filter_by(username=username).first():
            errors.append("That username is already in use.")

        if User.query.filter_by(email=email).first():
            errors.append("That email is already registered.")

        if errors:
            for error in errors:
                flash(error, "error")

            return render_template(
                "register.html",
                username=username,
                email=email,
            )
        
        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully.", "success")

        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("books"))
    
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password:
            flash("Invalid username or password.", "error")
            return render_template("login.html", username=username)
        
        login_user(user)

        flash("Logged in successfully.", "success")

        return redirect(url_for("books"))
    
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()

    flash("Logged out successfully.", "success")

    return redirect(url_for("login"))

@app.route("/books")
@login_required
def books():
    books = Book.query.filter_by(user_id=current_user.id).all()

    return render_template("books.html", books=books)

@app.route("/books/add", methods=["GET", "POST"])
@login_required
def add_book():
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form["note"].strip()   
        status = request.form["status"]

        errors = []

        if not title:
            errors.append("Title is required.")

        if not author:
            errors.append("Author is required.")

        if status not in ["Want to Read", "Reading", "Finished"]:
            errors.append("Please select a valid status.")

        if errors:
            for error in errors:
                flash(error, "error")

            return render_template(
                "book_form.html",
                title=title,
                author=author,
                note=note,
                status=status
            )
        
        book = Book(
            title=title,
            author=author,
            note=note,
            status=status,
            user_id=current_user.id
        )

        db.session.add(book)
        db.session.commit()

        flash("Book added successfully.", "success")

        return redirect(url_for("books"))
    
    return render_template("book_form.html")

@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.filter_by(
        id=book_id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form["note"].strip()
        status = request.form["status"]

        errors = []

        if not title:
            errors.append("Title is required.")

        if not author:
            errors.append("Author is required.")

        if status not in ["Want to Read", "Reading", "Finished"]:
            errors.append("Please select a valid status.")

        if errors:
            for error in errors:
                flash(error, "error")

            return render_template(
                "book_edit.html",
                book=book,
                title=title,
                author=author,
                note=note,
                status=status
            )
        
        book.title = title
        book.author = author
        book.note = note
        book.status = status

        db.session.commit()

        flash("Book updated successfully.", "success")

        return redirect(url_for("books"))
    
    return render_template("book_edit.html", book=book)
