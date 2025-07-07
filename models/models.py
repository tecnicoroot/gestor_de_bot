from sqlalchemy import (
    Column, Integer, String, LargeBinary, DateTime, Enum as SqlEnum, 
    func, Boolean, ForeignKey, Table, CHAR
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

# Enum de status
class StatusUsuario(enum.Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"
    SUSPENSO = "suspenso"

# Tabela associativa N:N
usuario_robo_associacao = Table(
    'usuario_robo',
    Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('robo_id', Integer, ForeignKey('robos.id'), primary_key=True)
)

# Classe Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
    status = Column(SqlEnum(StatusUsuario), default=StatusUsuario.ATIVO, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relacionamento N:N com Robo
    robos = relationship('Robo', secondary=usuario_robo_associacao, back_populates='usuarios')


# Classe Robo
class Robo(Base):
    __tablename__ = 'robos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_origin = Column(Integer, nullable=False)
    robot = Column(String(100), unique=True, nullable=False)
    description = Column(String(2000))
    activated = Column(Boolean, nullable=False)
    interval = Column(Integer)
    action = Column(CHAR(1))
    screen = Column(CHAR(1))
    executable_path = Column(String(200))
    time_limit = Column(Integer)
    activation_file = Column(String(200))
    executable_name = Column(String(45))
    workbook = Column(String(200))
    spreadsheet_repository = Column(String(200))
    notified = Column(String(1000))
    activated_program1 = Column(String(45))
    activated_program2 = Column(String(45))
    robot_sequence = Column(Integer)
    robot_user = Column(String(45))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relacionamento N:N com Usuario
    usuarios = relationship('Usuario', secondary=usuario_robo_associacao, back_populates='robos')
