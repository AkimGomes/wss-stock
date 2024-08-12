FROM python:3.10

ENV PYTHONUNBUFFERED 1

# Instalar o Poetry
RUN pip install --upgrade pip
RUN pip install poetry
ENV PATH="${PATH}:/root/.poetry/bin"

# Definir o diretório de trabalho
WORKDIR /usr/src/app
COPY . .

# Instalar as dependências
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Expor a porta que a aplicação vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]