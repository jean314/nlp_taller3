from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS
from transformers import MarianMTModel, MarianTokenizer
from transformers import pipeline
from threading import Thread

# Crear la app de Flask
app = Flask(__name__)
# Habilitar CORS para todas las rutas
CORS(app)

# Cargar el modelo
#translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Servicio de Traducción</title>
<script>
async function sendTranslation() {
    const text = document.getElementById("inputText").value;
    const response = await fetch("http://localhost:5555/translate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });
    const data = await response.json();
    document.getElementById("translationResult").innerText = `Traducción: ${data.translation}`;
}
</script>
</head>
<body>
<div style="max-width: 600px; margin: 0 auto; text-align: center;">
    <h1>Servicio de Traducción</h1>
    <textarea id="inputText" rows="4" cols="50" placeholder="Escribe un texto en inglés para traducirlo al español..."></textarea>
    <br><br>
    <button onclick="sendTranslation()">Obtener Traducción</button>
    <p id="translationResult" style="margin-top: 20px; font-size: 18px; font-weight: bold;"></p>
</div>
</body>
</html>
"""

# Ruta para servir el HTML
@app.route("/")
def home():
    return html_content

model_name = "Helsinki-NLP/opus-mt-en-es"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Endpoint principal para traducción
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    # Verificar que se haya enviado el texto
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No se proporcionó texto para traducir"}), 400

    # Preparar la entrada para el modelo
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    
    return jsonify({"translation": translated_text})


# Función para ejecutar Flask en un hilo
def run_flask():
    app.run(host="0.0.0.0", port=5555)

# Crear un hilo para ejecutar Flask
thread = Thread(target=run_flask)
thread.start()
