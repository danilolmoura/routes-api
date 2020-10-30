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

    initial_position = data['initial_position']
    final_position = data['final_position']
    weight = data['weight']

    if not isinstance(initial_position, str):
        return 'Invalid initial_position format, expected string', 400

    if not isinstance(final_position, str):
        return 'Invalid final_position format, expected string', 400

    if not isinstance(weight, int) or weight < 1:
        return 'Invalid weight format, expected int bigger than 0', 400

    file_handler.add_line(initial_position, final_position, weight)

    return jsonify(True)

@bp.route('/find', methods=['GET'])
def find():
    initial_position = request.args['initial_position']
    final_position = request.args['final_position']
    
    g = graph.create_graph(FILE_PATH)
    if not g.nodes.get(initial_position, False):
        return 'Initial position does not exist: {}'.format(initial_position), 400
    if not g.nodes.get(final_position, False):
        return 'Final position does not exist: {}'.format(final_position), 400

    best_route_price = graph.get_best_route_price(g, initial_position, final_position)

    if best_route_price == float('inf'):
        return "It is not possible to go from {} to {}".format(initial_position, final_position)

    return jsonify(best_route_price)
