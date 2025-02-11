from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image
import os

class ImageCaptioning:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def generate_caption(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"The image at {image_path} does not exist.")
        
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        
        with torch.no_grad():
            out = self.model.generate(**inputs)
        
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption

# Example usage:
# image_captioning = ImageCaptioning()
# caption = image_captioning.generate_caption("path_to_image.jpg")
# print(caption)