# Servicio de Traducción con Docker y Flask

Este proyecto implementa un servicio web de traducción que convierte textos en inglés a español utilizando Flask y el modelo "Helsinki-NLP/opus-mt-en-es" de Hugging Face. La aplicación se despliega fácilmente mediante Docker, lo que garantiza un entorno consistente y simplifica su implementación en diferentes plataformas.

## Características

- **Interfaz Web Intuitiva:** Página HTML que permite ingresar texto en inglés y obtener su traducción al español.
- **API RESTful:** Endpoint `/translate` para procesar solicitudes POST y devolver la traducción en formato JSON.
- **Uso de Modelos de Última Generación:** Emplea el modelo de Hugging Face para ofrecer traducciones de alta calidad.
- **Dockerizado:** Facilita el despliegue y la escalabilidad del servicio.
- **CORS Habilitado:** Permite que la API sea consumida desde otros dominios.

## Requisitos

- [Docker](https://www.docker.com/) (opcional, para despliegue en contenedor)
- [Python 3.8](https://www.python.org/downloads/) o superior (si se ejecuta localmente)
- Conexión a Internet para descargar los modelos de Hugging Face en el primer uso

## Instalación y Uso

## Ejecución con Docker

Esta aplicación se puede ejecutar fácilmente en un contenedor Docker. Sigue estos pasos:

1. **Instalación de Docker:**  
   Asegúrate de tener Docker instalado en tu sistema.
   - En macOS o Windows, descarga e instala [Docker Desktop](https://www.docker.com/products/docker-desktop).
   - En Linux, sigue las [instrucciones oficiales de instalación de Docker](https://docs.docker.com/engine/install/).

2. **Construir la imagen Docker:**  
   Abre una terminal en el directorio del proyecto (donde se encuentra el `Dockerfile`) y ejecuta el siguiente comando para construir la imagen con el tag `flask-transformers-app`:
   ```bash
   docker build -t flask-transformers-app .

3. **Ejecutar el contenedor:**  
Una vez que la imagen se ha construido correctamente, ejecuta el contenedor mapeando el puerto 5555 del contenedor al puerto 5555 de tu máquina:
   ```bash
	docker run -p 5555:5555 flask-transformers-app

4. **Verificar la aplicación:**  
Abre tu navegador web y visita http://localhost:5555 para comprobar que la aplicación se esté ejecutando correctamente.

5. **Llamada al servicio REST**  
Se puede ejecutar el siguiente comando para llamar directamente al servicio en lugar de ingresar a la página web
   ```bash
	curl -X POST "http://localhost:5555/translate" -H "Content-Type: application/json" -d '{"text": "The product is functional, but it does not stand out in any way. It does what it is supposed to do without any issues."}'