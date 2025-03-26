from flask import Blueprint, render_template, session, jsonify

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart_items.values())
    return render_template('cart.html', cart_items=cart_items.values(), total_price=total_price)

@cart_bp.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    from utils import load_products
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)

    if product:
        if 'cart' not in session:
            session['cart'] = {}

        if str(product_id) in session['cart']:
            session['cart'][str(product_id)]['quantity'] += 1
        else:
            session['cart'][str(product_id)] = {
                'name': product['name'],
                'price': product['price'],
                'image': product['image'],
                'quantity': 1
            }

        session.modified = True
        return jsonify({"success": True})

    return jsonify({"success": False})
