FROM python:3.10-slim

# Crear entorno de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install kedro

# Comando por defecto
CMD ["kedro", "run"]
