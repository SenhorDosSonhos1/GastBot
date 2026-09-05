# GastBot

Um chatbot financeiro que permite registrar gastos através de mensagens no WhatsApp.

## Sobre

A ideia do GastBot surgiu da inspiração em aplicações de controle financeiro
e da necessidade de ter uma ferramenta que facilite o registro de gastos.
A proposta é permitir que o usuário envie uma mensagem pelo WhatsApp
descrevendo uma despesa, para que a aplicação interprete essas informações,
registre o gasto e retorne uma confirmação.

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Alembic
- Docker
- Docker Compose
- Poetry
- Pytest
- Ruff
- Taskipy

## Próximos passos

- [ ] Integração com WhatsApp
- [ ] Integração com Twilio
- [ ] Integração com LLM
- [ ] Interpretação automática das mensagens
- [ ] Consultas de gastos pelo WhatsApp

## Como executar

### Pré-requisitos

Antes de executar o projeto, tenha instalado:

- Docker
- Docker Compose
- Poetry

### Configuração

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias:

```env
POSTGRES_DB=your_database
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
DATABASE_URL=postgresql+psycopg://your_user:your_password@localhost:5432/your_database
```

> A `DATABASE_URL` acima é utilizada quando comandos como o Alembic são executados diretamente pela máquina host. A API, quando executada dentro do Docker, utiliza `db` como host do PostgreSQL através do Docker Compose.

### Instalação das dependências

Instale as dependências do projeto utilizando o Poetry:

```bash
poetry install
```

### Executando com Docker

Suba a aplicação e o PostgreSQL utilizando:

```bash
docker compose up --build
```

A API estará disponível em:

```text
http://localhost:8000
```

A documentação interativa da API pode ser acessada em:

```text
http://localhost:8000/docs
```

### Executando os testes

Os testes podem ser executados com:

```bash
poetry run pytest
```

### Migrações

Para criar uma nova migration utilizando o Alembic:

```bash
poetry run alembic revision --autogenerate -m "nome_da_migration"
```

Para aplicar as migrations ao banco:

```bash
poetry run alembic upgrade head
```

> Como o Alembic é executado diretamente pela máquina host, a `DATABASE_URL` utilizada por ele deve apontar para `localhost:5432`.