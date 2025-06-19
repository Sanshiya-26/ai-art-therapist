from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.emotion import detect_emotion
from app.prompt_builder import build_prompt
from app.image_generator import generate_image

router = APIRouter()


@router.post("/analyze/")
def analyze_text(input: dict = Body(...)):
    try:
        text = input.get("text")
        mode = input.get("mode", "reflect")

        if not text:
            return JSONResponse(status_code=400, content={"error": "Missing 'text' in input."})

        # Detect emotion from text
        emotion, score = detect_emotion(text)
        print("Detected emotion:", emotion)

        # Build prompt based on emotion and mode
        prompt = build_prompt(emotion, mode)
        print("Prompt generated:", prompt)

        # Generate image and get path
        image_path = generate_image(prompt)
        print("Image generated at:", image_path)

        return {
            "emotion": emotion,
            "confidence": score,
            "prompt": prompt,
            "image_path": image_path
        }

    except Exception as e:
        print("Error in /analyze/:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})
