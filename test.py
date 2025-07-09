from database.db import SessionLocal, engine
from models.models import Base
from models.dao.user_dao import UserDAO

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Criar sessão
db = SessionLocal()
dao = UserDAO(db)

# Exemplo de uso
if dao.create("admin", "senha123"):
    print("Usuário 'admin' criado com sucesso.")

if dao.autenticar("admin", "senha123"):
    print("Autenticação bem-sucedida!")

#dao.redefinir_senha("admin", "nova123")

#if dao.autenticar("admin", "nova123"):
#    print("Senha redefinida com sucesso!")

print("Usuários cadastrados:")
for user in dao.list_users():
    print(f"ID: {user.id}, Username: {user.username}, Criado em: {user.created_at}")
