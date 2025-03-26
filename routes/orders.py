import os
from flask import Blueprint, request, flash, redirect, url_for, jsonify
from utils import load_orders, save_orders
from werkzeug.utils import secure_filename

orders_bp = Blueprint('orders', __name__)

UPLOAD_FOLDER = 'static/uploads/'

@orders_bp.route('/upload_images/<int:product_id>', methods=['POST'])
def upload_images(product_id):
    if 'images' not in request.files:
        flash('לא נבחרו תמונות.', 'error')
        return redirect(request.referrer)

    images = request.files.getlist('images')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    image_paths = []

    for image in images:
        if image.filename:
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(image_path)
            image_paths.append(image_path)

    orders = load_orders()
    orders.append({
        "product_id": product_id,
        "images": image_paths
    })
    save_orders(orders)

    flash('התמונות הועלו בהצלחה!', 'success')
    return redirect(url_for('products.product_detail', product_id=product_id))
