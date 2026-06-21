from openai import OpenAI, RateLimitError, APIError, APITimeoutError
from app.core.config import settings
from app.services.fallback_processor import fallback_process

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def process_text(text: str) -> dict:
    """
    Hybrid AI processor:
    - Uses OpenAI if available
    - Falls back to local processing if any failure occurs
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Return ONLY JSON with summary and key_points."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            timeout=10
        )

        content = response.choices[0].message.content

        return {
            "summary": content,
            "key_points": [],
            "mode": "ai"
        }

    except (RateLimitError, APIError, APITimeoutError, Exception):
        # fallback mode
        return fallback_process(text)