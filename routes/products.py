from flask import Blueprint, render_template, request, session, jsonify
from utils import load_products

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def products():
    category = request.args.get('category')
    products = load_products()
    if category:
        products = [p for p in products if p.get('category') == category]
    return render_template('products.html', products=products)

@products_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "המוצר לא נמצא", 404
    return render_template('product_detail.html', product=product)
