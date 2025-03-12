# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Actualiza pip e instala las dependencias
RUN pip install --upgrade pip
# Si usas requirements.txt, descomenta las siguientes líneas:
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# Si prefieres instalar directamente, usa:
RUN apt-get update && apt-get install -y espeak

RUN pip install flask flask-cors transformers torch sentencepiece googletrans gtts

# Copia el código de la aplicación
COPY app.py .

# Expone el puerto que utilizará la aplicación
EXPOSE 5555

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
