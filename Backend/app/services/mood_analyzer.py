def detect_mood(text: str) -> str:
    text = text.lower()

    # HAPPY
    if any(word in text for word in ["happy", "fun", "excited", "great", "good", "awesome"]):
        return "happy"

    # SAD
    if any(word in text for word in ["sad", "lonely", "cry", "depressed", "upset"]):
        return "sad"

    # STRESSED
    if any(word in text for word in ["stressed", "tired", "pressure", "anxious", "overwhelmed"]):
        return "stressed"

    # BORED
    if any(word in text for word in ["bored", "nothing to do", "free time"]):
        return "bored"

    # DEFAULT
    return "neutral"