from flask import Blueprint, request, jsonify
from app.models import Usuario, Establecimiento, EstablecimientoXUsuario
from app.database import db

bp = Blueprint('api', __name__)

@bp.route('/')
def index():
    return 'API FUNCIONANDO'

# Crear usuario
@bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        Nombre=data['Nombre'],
        Estado=data['Estado']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'UsuarioId': nuevo_usuario.UsuarioId}), 201

# Leer usuarios
@bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'UsuarioId': usuario.UsuarioId,
        'Nombre': usuario.Nombre,
        'Estado': usuario.Estado,
        'FechaCreacion': usuario.FechaCreacion
    } for usuario in usuarios])

# Actualizar usuario
@bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    data = request.json
    usuario = Usuario.query.get_or_404(usuario_id)
    usuario.Nombre = data['Nombre']
    usuario.Estado = data['Estado']
    db.session.commit()
    return jsonify({'message': 'Usuario actualizado'})

# Eliminar usuario
@bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado'})

# Asignar establecimientos a un usuario
@bp.route('/usuarios/<int:usuario_id>/establecimientos', methods=['POST'])
def assign_establecimientos(usuario_id):
    data = request.json
    usuario = Usuario.query.get_or_404(usuario_id)
    establecimientos = Establecimiento.query.filter(Establecimiento.EstablecimientoId.in_(data['Establecimientos'])).all()
    usuario.establecimientos = establecimientos
    db.session.commit()
    return jsonify({'message': 'Establecimientos asignados'})

# Obtener establecimientos de un usuario
@bp.route('/usuarios/<int:usuario_id>/establecimientos', methods=['GET'])
def get_establecimientos(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)
    establecimientos = usuario.establecimientos
    return jsonify([{
        'EstablecimientoId': e.EstablecimientoId,
        'Nombre': e.Nombre,
        'Estado': e.Estado
    } for e in establecimientos])

# Crear establecimiento
@bp.route('/establecimientos', methods=['POST'])
def create_establecimiento():
    data = request.json
    nuevo_establecimiento = Establecimiento(
        Nombre=data['Nombre'],
        Estado=data['Estado']
    )
    db.session.add(nuevo_establecimiento)
    db.session.commit()
    return jsonify({'EstablecimientoId': nuevo_establecimiento.EstablecimientoId}), 201

# Leer establecimientos
@bp.route('/establecimientos', methods=['GET'])
def get_establecimientos_list():
    establecimientos = Establecimiento.query.all()
    return jsonify([{
        'EstablecimientoId': e.EstablecimientoId,
        'Nombre': e.Nombre,
        'Estado': e.Estado,
        'FechaCreacion': e.FechaCreacion
    } for e in establecimientos])

# Actualizar establecimiento
@bp.route('/establecimientos/<int:establecimiento_id>', methods=['PUT'])
def update_establecimiento(establecimiento_id):
    data = request.json
    establecimiento = Establecimiento.query.get_or_404(establecimiento_id)
    establecimiento.Nombre = data['Nombre']
    establecimiento.Estado = data['Estado']
    db.session.commit()
    return jsonify({'message': 'Establecimiento actualizado'})

# Eliminar establecimiento
@bp.route('/establecimientos/<int:establecimiento_id>', methods=['DELETE'])
def delete_establecimiento(establecimiento_id):
    establecimiento = Establecimiento.query.get_or_404(establecimiento_id)
    db.session.delete(establecimiento)
    db.session.commit()
    return jsonify({'message': 'Establecimiento eliminado'})
