def predict_sentiment(text):
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"  # Bug volontaire

    def predict_sentiment(text):
    """
    Analyse le texte donné et retourne un sentiment :
    - "positive" si le texte contient 'happy' ou 'good'
    - "negative" si le texte contient 'sad' ou 'bad'
    - "neutral" sinon
    """
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"

