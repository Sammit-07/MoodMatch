from fastapi import APIRouter
from Backend.app.services.mood_analyzer import detect_mood
from Backend.app.services.recommender import get_recommendations

router = APIRouter()

@router.post("/chat")
def chat(message: dict):
    text = message.get("text", "")

    mood = detect_mood(text)
    suggestions = get_recommendations(mood)

    return {
        "input": text,
        "mood": mood,
        "recommendations": suggestions
    }