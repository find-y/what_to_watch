# what_to_watch/opinions_app/api_views.py

from flask import jsonify, request

from . import app, db
from .models import Opinion
from .views import random_opinion


@app.route('/api/opinions/<int:id>/', methods=['GET'])
def get_opinion(id):
    opinion = Opinion.query.get_or_404(id)
    return jsonify({'opinion': opinion.to_dict()}), 200


@app.route('/api/opinions/<int:id>/', methods=['PATCH'])
def update_opinion(id):
    data = request.get_json()
    if (
        'text' in data and 
        Opinion.query.filter_by(text=data['text']).first() is not None
    ):
        # При неуникальном значении поля text
        # возвращаем сообщение об ошибке в формате JSON
        # и статус-код 400:
        return jsonify({'error':
                        'Такое мнение уже есть в базе данных'}), 400
    opinion = Opinion.query.get_or_404(id)
    opinion.title = data.get('title', opinion.title)
    opinion.text = data.get('text', opinion.text)
    opinion.source = data.get('source', opinion.source)
    opinion.added_by = data.get('added_by', opinion.added_by)
    db.session.commit()  
    return jsonify({'opinion': opinion.to_dict()}), 201


@app.route('/api/opinions/<int:id>/', methods=['DELETE'])
def delete_opinion(id):
    opinion = Opinion.query.get_or_404(id)
    db.session.delete(opinion)
    db.session.commit()
    return '', 204


@app.route('/api/opinions/', methods=['GET'])
def get_opinions():
    opinions = Opinion.query.all()  
    opinions_list = [opinion.to_dict() for opinion in opinions]
    return jsonify({'opinions': opinions_list}), 200


@app.route('/api/opinions/', methods=['POST'])
def add_opinion():
    data = request.get_json()
    if 'title' not in data or 'text' not in data:
        return jsonify({'error':
                        'В запросе отсутствуют обязательные поля'}), 400
    # Если в базе данных уже есть объект 
    # с таким же значением поля text...
    if Opinion.query.filter_by(text=data['text']).first() is not None:
        # ...возвращаем сообщение об ошибке в формате JSON 
        # и статус-код 400:
        return jsonify({'error': 
                        'Такое мнение уже есть в базе данных'}), 400
    opinion = Opinion()
    opinion.from_dict(data)
    db.session.add(opinion)
    db.session.commit()
    return jsonify({'opinion': opinion.to_dict()}), 201 


@app.route('/api/get-random-opinion/', methods=['GET'])
def get_random_opinion():
    opinion = random_opinion()
    return jsonify({'opinion': opinion.to_dict()}), 200
