import json
from flask import Blueprint, request
from flask import jsonify

from application.file import file_handler

bp = Blueprint('route', __name__)

@bp.route('/add', methods=['POST'])
def add():
    data = json.loads(request.data)
    file_handler.add_line(data['initial_position'], data['final_position'], data['weight'])

    return jsonify(True)

@bp.route('/find', methods=['GET'])
def find():

    return jsonify({})
