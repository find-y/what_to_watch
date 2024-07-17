# what_to_watch/opinions_app/api_views.py

# Импортируем метод jsonify:
from flask import jsonify, request

from . import app, db
from .models import Opinion


# def opinion_to_dict(opinion):
#     return dict(
#         id = opinion.id,
#         title = opinion.title,
#         text = opinion.text,
#         source = opinion.source,
#         timestamp = opinion.timestamp,
#         added_by = opinion.added_by
#     )

# Явно разрешаем метод GET:
@app.route('/api/opinions/<int:id>/', methods=['GET'])
def get_opinion(id):
    # Получаем объект по id или выбрасываем ошибку 404:
    opinion = Opinion.query.get_or_404(id)
    # Конвертируем данные в JSON и возвращаем JSON-объект и HTTP-код ответа:
    # data = opinion_to_dict(opinion) 
    return jsonify({'opinion': opinion.to_dict()}), 200


@app.route('/api/opinions/<int:id>/', methods=['PATCH'])
def update_opinion(id):
    data = request.get_json()
    # Если метод get_or_404 не найдёт указанный ID, 
    # то он выбросит исключение 404:
    opinion = Opinion.query.get_or_404(id)
    opinion.title = data.get('title', opinion.title)
    opinion.text = data.get('text', opinion.text)
    opinion.source = data.get('source', opinion.source)
    opinion.added_by = data.get('added_by', opinion.added_by)
    # Все изменения нужно сохранить в базе данных.
    # Объект opinion добавлять в сессию не нужно.
    # Этот объект получен из БД методом get_or_404() и уже хранится в сессии.
    db.session.commit()  
    # При изменении объекта вернём сам объект и код 200:
    return jsonify({'opinion': opinion.to_dict()}), 200
