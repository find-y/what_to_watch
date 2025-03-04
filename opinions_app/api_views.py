from flask import jsonify

from . import app
from .models import Opinion


def opinion_to_dict(opinion):
    return dict(
        id = opinion.id,
        title = opinion.title,
        text = opinion.text,
        source = opinion.source,
        timestamp = opinion.timestamp,
        added_by = opinion.added_by
    )


# Явно разрешить метод GET
@app.route('/api/opinions/<int:id>/', methods=['GET'])  
def get_opinion(id):
    # Получить объект по id или выбросить ошибку
    opinion = Opinion.query.get_or_404(id)
    data = opinion_to_dict(opinion)  
    return jsonify({'opinion': data}), 200
