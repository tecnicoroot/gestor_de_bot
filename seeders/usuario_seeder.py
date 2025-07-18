import bcrypt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import sessionmaker
from models.models import StatusUser, User
from database.db import SessionLocal  # supondo que você tem um `engine`


def seed_usuarios():
    session = SessionLocal()
    try:
        if not session.query(User).filter_by(username="admin").first():
            user_admin = User(
                username="admin",
                password=bcrypt.hashpw(b"123", bcrypt.gensalt()),
                status=StatusUser.ACTIVE
            )
            session.add(user_admin)
            print("Usuário admin criado.")
        else:
            print("Usuário admin já existe.")

        # Adicione outros usuários aqui se quiser...

        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro ao executar seeder: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_usuarios()