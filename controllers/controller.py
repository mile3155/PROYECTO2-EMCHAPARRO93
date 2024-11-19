##Proyecto 2 - Edna Milena Chaparro Perez

from models.heladeria import Heladeria
from models.producto import Producto
from models.ingrediente import Ingrediente
from flask import jsonify, Blueprint
from models.producto import Producto

user_blueprint = Blueprint('producto_bp', __name__, url_prefix="/productos")

@user_blueprint.route('/')
def index():
    productos = Producto.query.all()
    return jsonify({"productos": productos[0].name}), 201

@user_blueprint.route('/update')
def update():
    return "Menu Heladeria",200