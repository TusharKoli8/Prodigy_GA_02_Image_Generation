import torch
from diffusers import StableDiffusionPipeline

# Use the same model as before
model_id = "runwayml/stable-diffusion-v1-5"

# Load with float16 (only for GPU)
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)

# Move pipeline to GPU
pipe = pipe.to("cuda")

# Your text prompt
prompt = "asthetic sofa placed in the modern living room"

# Generate image (reduce steps if it’s slow)
image = pipe(
    prompt,
    num_inference_steps=25,
    guidance_scale=7.5
).images[0]

# Save image
image.save("generated_image_sd_gpu.png")
print("Saved image as generated_image_sd_gpu.png")