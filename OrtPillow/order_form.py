from bottle import get, post, request, template
import json
import os
import re
from datetime import datetime

ORDERS_FILE = "orders.json"

def load_orders():
    """Load orders from JSON file using UTF-8 encoding"""
    try:
        if not os.path.exists(ORDERS_FILE):
            with open(ORDERS_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)
        
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Corrupted JSON. Resetting file.")
        with open(ORDERS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    except Exception as e:
        print(f"Loading error: {str(e)}")
        return []

def save_orders(data):
    """Save orders to JSON file with indentation"""
    try:
        with open(ORDERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Saving error: {str(e)}")
        raise

@get('/orders')
def show_orders():
    orders = load_orders()
    return template('orders.tpl',
                    sorted_orders=orders,
                    order_id='',
                    product='',
                    date='',
                    phone='',
                    order_id_error='',
                    product_error='',
                    date_error='',
                    phone_error='',
                    year=datetime.now().year)

@post('/orders')
def handle_order():
    order_id = request.forms.getunicode('order_id')
    product = request.forms.getunicode('product').strip()
    date = request.forms.getunicode('date').strip()
    phone = request.forms.getunicode('phone').strip()

    errors = {
        'order_id_error': '',
        'product_error': '',
        'date_error': '',
        'phone_error': ''
    }

    if not order_id:
        errors['order_id_error'] = "Order ID is required"
    elif not order_id.isdigit():
        errors['order_id_error'] = "Must be numeric"
    else:
        existing_ids = [str(o['order_id']) for o in load_orders()]
        if order_id in existing_ids:
            errors['order_id_error'] = "ID already exists"

    if not product:
        errors['product_error'] = "Product name required"
    elif len(product) < 3:
        errors['product_error'] = "Minimum 3 characters"

    if not validate_date(date):
        errors['date_error'] = "Invalid date (YYYY-MM-DD)"

    if not validate_phone(phone):
        errors['phone_error'] = "Invalid phone (+7XXXXXXXXXX)"

    if any(errors.values()):
        return template('orders.tpl',
                        order_id=order_id,
                        product=product,
                        date=date,
                        phone=phone,
                        sorted_orders=load_orders(),
                        **errors,
                        year=datetime.now().year)

    try:
        orders = load_orders()
        new_order = {
            'order_id': int(order_id),
            'product': product,
            'date': date,
            'phone': phone
        }
        orders.append(new_order)
        sorted_orders = sorted(orders, key=lambda x: x['date'], reverse=True)
        save_orders(sorted_orders)

        return template('orders.tpl',
                        order_id='',
                        product='',
                        date='',
                        phone='',
                        sorted_orders=load_orders(),
                        order_id_error='',
                        product_error='',
                        date_error='',
                        phone_error='',
                        year=datetime.now().year)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return template('orders.tpl',
                        order_id=order_id,
                        product=product,
                        date=date,
                        phone=phone,
                        sorted_orders=load_orders(),
                        **errors,
                        year=datetime.now().year)

def validate_phone(phone):
    """Validate Russian phone format (+7XXXXXXXXXX)"""
    return re.match(r'^\+7\d{10}$', phone) is not None

def validate_date(date_str):
    """Validate ISO date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    from bottle import run
    run(host='localhost', port=8080, debug=True, reloader=True)