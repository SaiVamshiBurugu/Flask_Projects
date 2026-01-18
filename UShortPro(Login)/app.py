from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import string
import random
import requests

app = Flask(__name__)

############# SQL Alchemy Configuration #################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'urls.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

############# Creating Models #################

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, original_url, short_code):
        self.original_url = original_url
        self.short_code = short_code

    def __repr__(self):
        return f"Url(original='{self.original_url}', short='{self.short_code}')"
##############################################

with app.app_context():
    db.create_all()
##############################################

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def is_valid_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code < 400
    except:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('url')
        if not original_url:
            flash('Please enter a URL.')
            return redirect(url_for('index'))

        if not is_valid_url(original_url):
            flash('Invalid or unreachable URL.')
            return redirect(url_for('index'))

        # Check if URL already exists
        existing = Url.query.filter_by(original_url=original_url).first()
        if existing:
            shortened_url = request.host_url + existing.short_code
            return render_template('index.html', shortened_url=shortened_url)

        short_code = generate_short_code()
        while Url.query.filter_by(short_code=short_code).first():
            short_code = generate_short_code()

        new_url = Url(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()

        shortened_url = request.host_url + short_code
        return render_template('index.html', shortened_url=shortened_url)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = User(email=request.form.get('email'),
                    password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is not None and user.check_password(request.form.get('password')):
            login_user(user)
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('index')
            return redirect(next)
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_entry = Url.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url_entry.original_url)

@app.route('/history')
def history():
    urls = Url.query.order_by(Url.created_at.desc()).all()
    return render_template('history.html', urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
