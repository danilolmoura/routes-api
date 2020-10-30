import json
from flask import Blueprint, request
from flask import jsonify

bp = Blueprint('routes', __name__, url_prefix='/routes')


@bp.route('', methods=['GET'])
def list():
    return jsonify({})


@bp.route('create', methods=['POST'])
def create(character_id):
    return jsonify({})


@bp.route('find', methods=['GET'])
def find(character_id):
    return jsonify({})
