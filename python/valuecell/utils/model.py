import os

from agno.models.deepseek import DeepSeek
from agno.models.google import Gemini


def get_model(env_key: str):
    model_id = os.getenv(env_key)
    if os.getenv("GOOGLE_API_KEY"):
        return Gemini(id=model_id or "gemini-2.5-flash")
    base_url = os.getenv("DEEPSEEK_API_BASE") or "https://api.deepseek.com"
    return DeepSeek(id=model_id or "deepseek-chat", base_url=base_url)
