from flask import flash, redirect, url_for, session, render_template, request
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint
import os  # נוסיף את המודול לניהול נתיבים

auth_bp = Blueprint('auth', __name__)

# פונקציה לקריאת המשתמשים מהקובץ
def load_users():
    try:
        users_file_path = os.path.join(os.path.dirname(__file__), '..', 'users.json')
        with open(users_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()

        # בדיקה אם שם המשתמש קיים ואם הסיסמה נכונה
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            flash('התחברת בהצלחה!', 'success')
            return redirect(url_for('home.home'))  # חזרה לעמוד הבית
        else:
            flash('שם המשתמש או הסיסמה שגויים הועברת להרשמה כמשתמש חדש', 'error')
            return redirect(url_for('register'))  # העברה לדף ההרשמה


    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        users = load_users()

        # בדיקה אם שם המשתמש תפוס
        if username in users:
            flash('אתה משתמש רשום, נסה להתחבר במקום זאת.', 'error')  # הודעה שהמשתמש כבר רשום
            return redirect(url_for('auth.login'))  # העברה לדף ההתחברות

        # הוספת המשתמש החדש
        users[username] = {
            'password': generate_password_hash(password),
            'email': email,  # שמירת המייל
            'address': address  # שמירת כתובת המגורים
        }

        # שמירת הנתונים עם נתיב דינאמי
        users_file_path = os.path.join(os.path.dirname(__file__), '..', 'users.json')
        with open(users_file_path, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

        flash('ההרשמה הצליחה! כעת ניתן להתחבר.', 'success')
        session['username'] = username  # שמירת שם המשתמש ב-session
        return redirect(url_for('home.home'))

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)  # מחיקת המשתמש מה-session
    flash('התנתקת בהצלחה', 'success')
    return redirect(url_for('home.home'))
