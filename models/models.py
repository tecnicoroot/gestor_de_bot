from sqlalchemy import (
    Column, Integer, String, LargeBinary,
    DateTime, Enum as SqlEnum, func
)
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

# Enum Python para status do usuário
class StatusUsuario(enum.Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"
    SUSPENSO = "suspenso"

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(LargeBinary, nullable=False)
    status = Column(SqlEnum(StatusUsuario), default=StatusUsuario.ATIVO, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
