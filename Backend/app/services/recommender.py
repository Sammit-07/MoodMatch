def get_recommendations(mood: str):
    recommendations = {
        "happy": [
            "3 Idiots",
            "Zindagi Na Milegi Dobara",
            "The Intern"
        ],
        "sad": [
            "Taare Zameen Par",
            "The Pursuit of Happyness",
            "Schindler's List"
        ],
        "stressed": [
            "Friends",
            "Brooklyn Nine-Nine",
            "The Office"
        ],
        "bored": [
            "Stranger Things",
            "Money Heist",
            "Breaking Bad"
        ],
        "neutral": [
            "Inception",
            "Interstellar",
            "The Dark Knight"
        ]
    }

    return recommendations.get(mood, recommendations["neutral"])