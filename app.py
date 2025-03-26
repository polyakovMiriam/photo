from flask import Flask
from routes.home import home_bp
from routes.products import products_bp
from routes.cart import cart_bp
from routes.orders import orders_bp
from routes.auth import auth_bp
from routes.contact import contact_bp

app = Flask(__name__)
app.secret_key = "dcbd4825d2fbbcec635d2fdd1ca5b750"
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# רישום ה-Blueprints באפליקציה
app.register_blueprint(home_bp)
app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(contact_bp)

if __name__ == '__main__':
    app.run(debug=True)
