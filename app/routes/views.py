from flask import render_template, url_for, request, redirect, Blueprint, jsonify, flash
import requests
import sys #print(..., file=sys.stderr)
from ..models import TodoModel
import json

BASE = "http://127.0.0.1:5000/"
TODOURL = BASE + "todo"
TODOLISTURL = BASE + "todolist"
views = Blueprint('views', __name__)

@views.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = TODOURL
        task_content = request.form.get('content') #form in html input has name of content
        if len(task_content) <= 0:
            flash("Task can't be empty" , "warning")
            return redirect(url_for('views.index'))
        body = {"content": task_content}

        try:
            response = requests.post(url, body)
            new_task = response.json()
            flash("Task added!" , "success")
            return redirect(url_for('views.index'))
        except:
            return "There was an issue adding your task"

    else:
        response = requests.get(TODOLISTURL)
        tasks = response.json()
        return render_template("index.html", tasks =tasks)

@views.route('/delete', methods = ['POST'])
def delete():
    response = json.loads(request.data) #loads body of fetch as dict
    id = response['taskID']
    url = TODOURL + f'/{id}'

    try: 
        requests.delete(url)
        return jsonify({})
    except:
        return "There was a problem with deleting that task"

# NONJS Method
@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id): #Note: reads id variable from int:id
    url = TODOURL + f'/{id}'

    if request.method == 'POST':
        content = request.form.get('content')
        body = {"content":content}

        try:
            response = requests.put(url,body)
            return redirect(url_for('views.index'))
        except:
            return "There was an issue updating your task"

    else:
        response = requests.get(url)
        task_to_update = response.json()
        return render_template("update.html", task=task_to_update)