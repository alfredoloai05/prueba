from datetime import datetime
from sqlalchemy import BigInteger, Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    UsuarioId = Column(BigInteger, primary_key=True)
    Nombre = Column(String(150), nullable=False)
    Estado = Column(Boolean, nullable=False)
    FechaCreacion = Column(DateTime, default=datetime.utcnow)
    establecimientos = relationship('Establecimiento', secondary='EstablecimientoXUsuario')

class Establecimiento(db.Model):
    __tablename__ = 'Establecimiento'
    EstablecimientoId = Column(BigInteger, primary_key=True)
    Nombre = Column(String(10), nullable=False)
    Estado = Column(Boolean, nullable=False)

class EstablecimientoXUsuario(db.Model):
    __tablename__ = 'EstablecimientoXUsuario'
    EstablecimientoId = Column(BigInteger, db.ForeignKey('Establecimiento.EstablecimientoId'), primary_key=True)
    UsuarioId = Column(BigInteger, db.ForeignKey('Usuario.UsuarioId'), primary_key=True)
