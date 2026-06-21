def fallback_process(text: str) -> dict:
    """
    Lightweight offline processor used when AI is unavailable.
    """

    # ساده‌سازی متن
    words = text.split()

    # crude summary (extract first 30 words)
    summary = " ".join(words[:30]) + "..." if len(words) > 30 else text

    # key points heuristic
    sentences = text.split(".")
    key_points = [s.strip() for s in sentences if len(s.strip()) > 20][:3]

    return {
        "summary": summary,
        "key_points": key_points if key_points else ["No key points extracted"],
        "mode": "fallback"
    }