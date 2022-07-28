from flask import render_template, url_for, request, redirect, Blueprint, jsonify, flash
import requests
import sys #print(..., file=sys.stderr)
from ..models import TodoModel
import json

BASE = "http://127.0.0.1:5000/"
TODOURL = BASE + "todo"
todoapi = Blueprint('todoapi', __name__)

@todoapi.route('/get_task/<int:id>', methods=['GET'])
def get_task(id):
    url = TODOURL + f'/{id}'
    response = requests.get(url)
    task = response.json()
    return task, 201


