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

### Ejecución con Docker

1. **Construir la imagen Docker:**

   ```bash
   docker build -t servicio-traduccion .
