from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
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

############# Creating a Model #################
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
