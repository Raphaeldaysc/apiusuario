# API de Gestão de Usuários

Bem-vindo à **API de Gestão de Usuários**! Esta API foi desenvolvida para facilitar a manipulação e o gerenciamento de dados de usuários, utilizando Django e Django REST Framework.

## Índice

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Autenticação](#autenticação)
- [Endpoints](#endpoints)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Recursos

- CRUD completo para usuários (Criar, Ler, Atualizar, Deletar)
- Autenticação básica
- Validação de e-mails únicos
- Campos personalizáveis para cada usuário, como biografia, foto de perfil, data de nascimento, telefone e endereço

## Instalação

Para configurar a API em sua máquina local, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/sua-api.git
   cd sua-api
Crie um ambiente virtual e ative-o:

bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
Instale as dependências:

bash
pip install -r requirements.txt
Configure seu banco de dados no arquivo settings.py.

Aplique as migrações:

bash
python manage.py migrate
Crie um superusuário (opcional):

bash
python manage.py createsuperuser
Inicie o servidor:

bash
python manage.py runserver
Uso
Para acessar a API, faça requisições HTTP para os endpoints listados abaixo. A API suporta autenticação básica, portanto, você precisará fornecer um nome de usuário e uma senha válidos.

Autenticação
A API utiliza autenticação básica. Para autenticar, envie suas credenciais (nome de usuário e senha) em cada requisição.

Exemplo de Requisição
bash
curl -X GET http://127.0.0.1:8000/api/v1/usuarios/ \
     -H "Authorization: Basic $(echo -n 'username:password' | base64)"
Endpoints
Usuários
Listar usuários

GET /api/v1/usuarios/
Criar um novo usuário

POST /api/v1/usuarios/
Obter detalhes de um usuário

GET /api/v1/usuarios/{id}/
Atualizar um usuário

PUT /api/v1/usuarios/{id}/
Deletar um usuário

DELETE /api/v1/usuarios/{id}/
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para sugestões de melhorias.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
