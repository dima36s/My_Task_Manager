from flask import Flask, render_template, request, url_for, redirect
from model import db, Manger


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


app = create_app()


@app.get('/')
def home_page():
    my_list = Manger.query.all()
    return render_template('index.html', my_list=my_list, title='Главная страница')


@app.post('/add')
def add():
    title = request.form.get('title')
    new_todo = Manger(title=title, is_complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home_page'))


@app.get('/update/<int:todo_id>')
def update(todo_id):
    todo = Manger.query.filter_by(id=todo_id).first()
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for('home_page'))


@app.get('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Manger.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home_page'))
