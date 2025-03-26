from flask import Blueprint, render_template, request

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"תודה {name}, ההודעה שלך התקבלה! אנחנו ניצור איתך קשר בהקדם."
    return render_template('contact.html')
