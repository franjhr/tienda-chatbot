import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "").strip()
OPENAI_REASONING_EFFORT = "low"

if not OPENAI_API_KEY:
    raise RuntimeError("No está definida la variable OPENAI_API_KEY")

if not OPENAI_MODEL:
    raise RuntimeError("No está definida la variable OPENAI_MODEL")
