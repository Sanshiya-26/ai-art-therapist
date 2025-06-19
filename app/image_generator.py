from diffusers import StableDiffusionPipeline
import torch
import os

# Load the model once (global)
model_id = "prompthero/openjourney"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
pipe = pipe.to("cpu")  # or "cuda" if you have a GPU

def generate_image(prompt: str):
    print(f"Generating image for: {prompt}")
    
    # Generate image using Stable Diffusion
    image = pipe(prompt).images[0]
    
    # Save the image
    output_path = "static/output.png"
    os.makedirs("static", exist_ok=True)
    image.save(output_path)

    return output_path
