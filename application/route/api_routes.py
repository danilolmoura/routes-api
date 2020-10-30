import json
from flask import Blueprint, request
from flask import jsonify

from application.file import file_handler

bp = Blueprint('route', __name__)

@bp.route('/add', methods=['POST'])
def add():
    return jsonify({})


@bp.route('/find', methods=['GET'])
def find():

    return jsonify({})
