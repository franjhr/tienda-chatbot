# Chatbot de la tienda

Chatbot de atención al cliente de una tienda online. Responde dudas sobre envíos, devoluciones y horarios desde una página web, usando la API de OpenAI y una arquitectura en capas.

## Esquema

```
Usuario (web/)  ──►  api/  ──►  services/  ──►  llm/  ──►  OpenAI
    ▲                                                         │
    └───────────────  {"response": "..."}   ◄─────────────────┘

config/ aporta la clave y el modelo a llm/
```

## Qué hay en cada carpeta

- `api/`: crea la aplicación y sirve la web.
  - `api/routes/`: endpoints, como `POST /chat`.
  - `api/schemas/`: formato y validación de lo que entra y sale de cada endpoint.
- `services/`: lógica del chatbot.
  - `services/prompts/`: instrucciones del chatbot y políticas de la tienda.
- `llm/`: único sitio que habla con OpenAI.
- `config/`: carga la configuración, con la clave y el modelo del `.env`.
- `web/`: página del chat (HTML, CSS y JavaScript).
- `demo/`: vídeos de las pruebas del chatbot.

## Cómo ejecutarlo

Los comandos se ejecutan desde la raíz del proyecto.

1. Crea el entorno virtual e instala las dependencias:

   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```

2. Copia `.env.example` a `.env` y escribe en `OPENAI_API_KEY` tu clave, que puedes crear en https://platform.openai.com/api-keys:

   ```bash
   cp .env.example .env
   ```

3. Arranca el servidor:

   ```bash
   .venv/bin/uvicorn api.main:app --reload
   ```

4. Abre http://127.0.0.1:8000 y escribe un mensaje, o pruébalo desde la terminal:

   ```bash
   curl -X POST http://127.0.0.1:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "¿Dónde está mi pedido?"}'
   ```

## Pruebas

Vídeos de pruebas reales contra la API de OpenAI, grabados con una herramienta automática de navegador.

- [Consultas sobre envíos, devoluciones y horario](demo/chatbot_1_consultas.mp4)
- [Preguntas sin información disponible, incluida «¿Dónde está mi pedido?»](demo/chatbot_2_no_inventar.mp4)
- [Intentos de saltarse las reglas](demo/chatbot_3_seguridad.mp4)
- [Comportamiento de la web: campo vacío, HTML en el mensaje y falta de historial](demo/chatbot_4_web.mp4)

## Límites

- 2000 caracteres por mensaje (`api/schemas/chat.py`).

## Cómo cambiar el chatbot

Reinicia el servidor después de cualquiera de estos cambios, porque ambos archivos se leen solo al arrancar.

- **Modelo:** edita `OPENAI_MODEL` en el `.env`.
- **Instrucciones o políticas:** edita `services/prompts/customer_support.md`.
