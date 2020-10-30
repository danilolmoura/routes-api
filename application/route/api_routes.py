import json
from flask import Blueprint, request
from flask import jsonify

from application.file import file_handler
from graph import graph

FILE_PATH = 'files/input-routes.csv'
bp = Blueprint('route', __name__)

@bp.route('/add', methods=['POST'])
def add():
    data = json.loads(request.data)
    file_handler.add_line(data['initial_position'], data['final_position'], data['weight'])

    return jsonify(True)

@bp.route('/find', methods=['GET'])
def find():
    initial_position = request.args['initial_position']
    final_position = request.args['final_position']
    
    g = graph.create_graph(FILE_PATH)
    best_route_price = graph.get_best_route_price(g, initial_position, final_position)

    return jsonify(best_route_price)
