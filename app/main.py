from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from app.routes import router
import os

app = FastAPI()
app.include_router(router)

# Mount the static directory (optional but useful)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "AI Art Therapist is running!"}

@app.get("/image")
def get_image():
    image_path = "static/output.png"
    abs_path = os.path.abspath(image_path)

    if not os.path.exists(abs_path):
        return JSONResponse(
            status_code=404,
            content={"error": f"Image not found at {abs_path}"}
        )

    return FileResponse(abs_path, media_type="image/png")
