import json

# פונקציה לקריאת פריטים מקובץ JSON
def load_products():
    with open('products.json', 'r', encoding='utf-8') as file:
        product = json.load(file)
    return product

# פונקציה לשמירת נתוני משתמשים לקובץ JSON
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

def load_orders():
    with open('orders.json', 'r', encoding='utf-8') as file:
        orders = json.load(file)
    return orders

def save_orders(orders):
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

