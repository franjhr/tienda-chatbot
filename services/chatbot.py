import logging
from pathlib import Path

from llm.openai_client import LLMError, generate_response

logger = logging.getLogger(__name__)

PROMPT_PATH = Path(__file__).parent / "prompts" / "customer_support.md"
INSTRUCTIONS = PROMPT_PATH.read_text(encoding="utf-8")

if not INSTRUCTIONS.strip():
    raise RuntimeError(f"El prompt está vacío: {PROMPT_PATH}")


class ChatbotUnavailable(Exception):
    pass


def respond(message: str) -> str:
    try:
        return generate_response(INSTRUCTIONS, message)
    except LLMError as error:
        logger.exception("No se ha podido generar la respuesta")
        raise ChatbotUnavailable from error
