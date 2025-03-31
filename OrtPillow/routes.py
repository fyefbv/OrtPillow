"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    products = [
        {
            "image": "/static/images/ort_pillow1.png",
            "name": "Neck Support Pro",
            "description": "Advanced memory foam technology",
            "price": "$89.99"
        },
        {
            "image": "/static/images/ort_pillow2.png",
            "name": "Travel Comfort",
            "description": "Compact design for perfect sleep anywhere",
            "price": "$49.99"
        },
        {
            "image": "/static/images/ort_pillow3.png",
            "name": "Kids OrthoCare",
            "description": "For healthy spine development",
            "price": "$64.99"
        },
        {
            "image": "/static/images/ort_pillow4.png",
            "name": "Luxury Dream",
            "description": "Premium materials for ultimate comfort",
            "price": "$129.99"
        },
        {
            "image": "/static/images/ort_pillow5.png",
            "name": "Cooling Gel",
            "description": "Stay cool all night with gel-infused foam",
            "price": "$79.99"
        },
        {
            "image": "/static/images/ort_pillow6.png",
            "name": "Side Sleeper",
            "description": "Ergonomic design for side sleepers",
            "price": "$59.99"
        },
        {
            "image": "/static/images/ort_pillow7.png",
            "name": "Bamboo Bliss",
            "description": "Eco-friendly bamboo cover with memory foam",
            "price": "$99.99"
        },
        {
            "image": "/static/images/ort_pillow8.png",
            "name": "Firm Support",
            "description": "Extra firm for proper spinal alignment",
            "price": "$74.99"
        },
        {
            "image": "/static/images/ort_pillow9.png",
            "name": "Pregnancy Comfort",
            "description": "Designed for expecting mothers",
            "price": "$109.99"
        },
        {
            "image": "/static/images/ort_pillow10.png",
            "name": "Adjustable Comfort",
            "description": "Customizable loft for personalized support",
            "price": "$89.99"
        },
        {
            "image": "/static/images/ort_pillow11.png",
            "name": "Pillow of the future",
            "description": "Futuristic design pillow",
            "price": "$49.99"
        },
        {
            "image": "/static/images/ort_pillow12.png",
            "name": "Oreo in reverse",
            "description": "Oreo Inspired Pillow",
            "price": "$99.99"
        }
    ]
    return dict(
        products=products,
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/history')
@view('history')
def history():
    return dict(
        title='Company History',
        year=datetime.now().year
    )
