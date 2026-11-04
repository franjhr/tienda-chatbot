from openai import OpenAI, OpenAIError

from config.settings import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_REASONING_EFFORT

client = OpenAI(api_key=OPENAI_API_KEY, timeout=15, max_retries=1)


class LLMError(Exception):
    pass


def generate_response(instructions: str, message: str) -> str:
    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=instructions,
            input=message,
            reasoning={"effort": OPENAI_REASONING_EFFORT},
        )
    except OpenAIError as error:
        raise LLMError("Fallo al llamar a OpenAI") from error

    text = response.output_text.strip()
    if not text:
        raise LLMError("OpenAI ha devuelto una respuesta sin texto")
    return text
