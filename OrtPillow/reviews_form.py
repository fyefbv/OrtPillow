import json
import re
from datetime import datetime
from bottle import HTTPResponse, get, post, request, template

REVIEWS_FILE = "reviews.json"

# Функция загрузки отзывов из json-файла (возвращает список отзывов или пустой список при ошибках)
def load_reviews():
    try:
        with open(REVIEWS_FILE, 'r', encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Функция сохранения отзывов в json-файл
def save_reviews(reviews):
    sorted_reviews = sorted(reviews, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d / %H:%M'), reverse=True)
    with open(REVIEWS_FILE, 'w', encoding="utf-8") as f:
        json.dump(sorted_reviews, f, ensure_ascii=False, indent=2)

# Функция валидации всех данных (возвращает словарь с ошибками)
def validate_review_data(data):
    errors = {}
    
    author = data['author']
    error_message = validate_author(author)
    if error_message is not None:
        errors['author'] = error_message

    text = data['text']
    error_message = validate_text(text)
    if error_message is not None:
        errors['text'] = error_message

    phone = data['phone']
    error_message = validate_phone(phone)
    if error_message is not None:
        errors['phone'] = error_message
    
    return errors

# Функция проверки валидности имени автора
def validate_author(author):
    if not author.strip():
        return 'Name field is required'
    else:
        if len(author) < 3:
            return 'Name must be at least 3 characters'
        elif len(author) > 15:
            return 'Name cannot exceed 15 characters'

    return None

# Функция проверки валидности текста отзыва
def validate_text(text):
    if not text.strip():
        return 'Review field is required'
    else:
        if len(text) < 10:
            return 'Review must be at least 10 characters'
        elif len(text) > 1000:
            return 'Review cannot exceed 300 characters'

    return None

# Функция проверки формата номера телефона
def validate_phone(phone):
    if not phone.strip():
        return 'Phone field is required'
    elif not re.match(r'^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$', phone):
        return 'Invalid phone format'

    return None

@post('/reviews')
def handle_reviews_submission():
    # Формирование данных отзыва из запроса
    review_data = {
        'author': request.forms.getunicode('author', '').strip(),
        'text': request.forms.getunicode('text', '').strip(),
        'phone': request.forms.getunicode('phone', '').strip(),
        'date': datetime.now().strftime('%Y-%m-%d / %H:%M')
    }

    # Валидация полученных данных
    errors = validate_review_data(review_data)
    
    # При отсутствии ошибок сохраняем и показываем обновленный список
    if not errors:
        reviews = load_reviews()
        reviews.append(review_data)
        save_reviews(reviews)
        return HTTPResponse(
            status=303,
            headers={'Location': '/reviews'},
            body=''
        )
        
    # При наличии ошибок показываем форму с сообщениями об ошибках
    return template('reviews.tpl',
                    sorted_reviews=load_reviews(),
                    errors=errors,
                    author=review_data['author'],
                    text=review_data['text'],
                    phone=review_data['phone'],
                    date=review_data['date'],
                    year=datetime.now().year)