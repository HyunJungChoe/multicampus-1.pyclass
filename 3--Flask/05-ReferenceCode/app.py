from flask import FLASK, request, flash ,url_for, redirect, render_template
from flask.signals import signals_available
from flask_sqlalchemy import SQLALchemy

app = FLASK(__name__)

app.config['SQLALchemy_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/pythondb'
