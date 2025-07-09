from sqlalchemy import (
    Column, Integer, String, LargeBinary, DateTime, Enum as SqlEnum, 
    func, Boolean, ForeignKey, Table, CHAR
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

# Enum de status
class StatusUser(enum.Enum):
    ACTIVE = "ativo"
    INACTIVE = "inativo"
    SUSPENDED = "suspenso"

# Tabela associativa N:N
user_robot_association = Table(
    'user_robot',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('robot_id', Integer, ForeignKey('robots.id'), primary_key=True)
)

# Classe Usuario
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
    status = Column(SqlEnum(StatusUser), default=StatusUser.ACTIVE, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relacionamento N:N com Robo
    robots = relationship('Robot', secondary=user_robot_association, back_populates='users')


# Classe Robo
class Robot(Base):
    __tablename__ = 'robots'
    
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

    # Relacionamento N:N com User
    users = relationship('User', secondary=user_robot_association, back_populates='robots')
