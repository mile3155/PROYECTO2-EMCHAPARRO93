##Proyecto 2 - Edna Milena Chaparro Perez

import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,template_folder="views")
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root:@localhost:3306/' + os.path.join(basedir, 'proyecto2.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

import mysql.connector
cnx = mysql.connector.connect(user='root', password='psw', host='127.0.0.1', database='db')

##@app.route('/')
##def index():
##    productos = {'nombre': 'Samurai de fresas', 'precio': 7500}
##    return render_template('index.html', productos=productos)

if __name__=='__main__':
    app.run(debug=True)





