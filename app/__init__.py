from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_restful import Api

db = SQLAlchemy()
api = Api()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'KEY' #encrypt session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # from .models import TodoModel, UserModel
    from .todo_resource import TodoResource, TodoListResource #Resource

    db.init_app(app)
    api.add_resource(TodoResource, "/todo", "/todo/<int:task_id>") #Resource
    api.add_resource(TodoListResource, "/todolist") #Resource

    api.init_app(app)
    

    from .routes.views import views #blueprint1
    # from .routes.todoapi import todoapi #blueprint2

    app.register_blueprint(views, url_prefix="/") #blueprint1
    # app.register_blueprint(todoapi, url_prefix="/api") #blueprint2

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)
        print('Created Database')

    #db.drop_all()
    # db.create_all()


