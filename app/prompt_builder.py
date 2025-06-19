def build_prompt(emotion, mode="reflect"):
    mood_map = {
        "admiration": "a warm glowing painting of appreciation",
        "amusement": "vibrant splashes of color evoking laughter",
        "anger": "bold red and black strokes in chaotic shapes",
        "annoyance": "repetitive textures with harsh strokes",
        "approval": "a balanced and structured composition",
        "caring": "soft pastels and gentle curves forming a heart",
        "confusion": "abstract swirls and overlapping shapes",
        "curiosity": "vivid details and unusual contrasts",
        "desire": "intense and vibrant tones with smooth transitions",
        "disappointment": "dim colors fading into grey",
        "disapproval": "dark, broken shapes and sharp shadows",
        "disgust": "distorted textures in muddled greens and browns",
        "embarrassment": "clashing colors and blushing tones",
        "excitement": "explosive vibrant colors and dynamic lines",
        "fear": "cold misty hues with jagged lines",
        "gratitude": "golden light spreading across a calm canvas",
        "grief": "deep blues fading into black shadows",
        "joy": "bright and colorful abstract painting full of light",
        "love": "soft glowing colors interwoven like threads",
        "nervousness": "a chaotic abstract in pale blue and grey",
        "optimism": "gentle sunrise tones with upward motion",
        "pride": "strong bold strokes rising from the center",
        "realization": "light breaking through a cloudy shape",
        "relief": "cool gradients with soothing textures",
        "remorse": "heavy shadows and receding shapes",
        "sadness": "a painting with soft, dark blues and grays",
        "surprise": "sudden splashes of unexpected color",
        "neutral": "balanced geometric forms with muted tones",
        "calm": "serene landscape with smooth lines and gentle tones"
    }

    if mode == "reflect":
        return f"A digital painting that represents {mood_map.get(emotion, 'an emotion')}"
    elif mode == "positive":
        return f"A digital painting that transforms {emotion} into peace and hope"
