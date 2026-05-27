from flask import render_template
from app.routes import main


@main.route('/')
def index():
    return 'To-Do List App is running!'
