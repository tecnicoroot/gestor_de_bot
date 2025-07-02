from database.db import SessionLocal, engine
from models.models import Base
from models.dao.user_dao import UsuarioDAO

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Criar sessão
db = SessionLocal()
dao = UsuarioDAO(db)

# Exemplo de uso
if dao.criar("admin", "senha123"):
    print("Usuário 'admin' criado com sucesso.")

if dao.autenticar("admin", "senha123"):
    print("Autenticação bem-sucedida!")

#dao.redefinir_senha("admin", "nova123")

#if dao.autenticar("admin", "nova123"):
#    print("Senha redefinida com sucesso!")

print("Usuários cadastrados:")
for user in dao.listar_usuarios():
    print(f"ID: {user.id}, Username: {user.username}, Criado em: {user.created_at}")
