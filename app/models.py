from datetime import datetime
from sqlalchemy import BigInteger, Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import db

class Usuario(db.Model):
    __tablename__ = 'usuario'  
    UsuarioId = Column(BigInteger, primary_key=True)
    Nombre = Column(String(150), nullable=False)
    Estado = Column(Boolean, nullable=False)
    FechaCreacion = Column(DateTime, default=datetime.utcnow)
    establecimientos = relationship('Establecimiento', secondary='establecimientos_x_usuarios', backref='usuarios')

class Establecimiento(db.Model):
    __tablename__ = 'establecimiento' 
    EstablecimientoId = Column(BigInteger, primary_key=True)
    Nombre = Column(String(10), nullable=False)
    Estado = Column(Boolean, nullable=False)

class EstablecimientoXUsuario(db.Model):
    __tablename__ = 'establecimientos_x_usuarios'
    
    UsuarioId = Column(BigInteger, db.ForeignKey('usuario.UsuarioId'), primary_key=True)
    EstablecimientoId = Column(BigInteger, db.ForeignKey('establecimiento.EstablecimientoId'), primary_key=True)
    
    usuario = relationship('Usuario', backref='asignaciones')
    establecimiento = relationship('Establecimiento', backref='asignaciones')
