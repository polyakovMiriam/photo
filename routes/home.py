from flask import Blueprint, render_template, session

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    username = session.get('username')
    return render_template('home.html', username=username)

@home_bp.route('/about')
def about():
    return render_template('about.html')

@home_bp.route('/gallery')
def gallery():
    return render_template('gallery.html')
