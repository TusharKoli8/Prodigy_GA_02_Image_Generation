# Image Generation with Stable Diffusion

Simple Python script that generates images from text prompts using **Stable Diffusion** (`diffusers` + PyTorch) in VS Code.

## Requirements

- Python 3.8+
- VS Code Python extension
- (Optional) NVIDIA GPU with CUDA

Install dependencies:

--bash
pip install torch diffusers transformers accelerate torchvision

## Usage

1. Activate your venv :

   --bash
   venv\Scripts\activate

   
3. Run:

   --bash
   python stable_diffusion_image.py
   
An image will be saved as `generated_image_sd_gpu.png` .
