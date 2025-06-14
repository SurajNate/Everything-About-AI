import os
import torch
from PIL import Image, ImageDraw, ImageFont
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from diffusers import StableDiffusionPipeline
from dotenv import load_dotenv
import numpy as np

class ComicGenerator:
    def __init__(self, model_id="CompVis/stable-diffusion-v1-4"):
        load_dotenv()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        ).to(self.device)
        
        # Initialize story processing pipeline
        self.story_processor = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        
    def process_story(self, prompt):
        """Break down story into scenes and extract key elements"""
        tokens = self.tokenizer(prompt, return_tensors="pt")
        output = self.story_processor.generate(
            **tokens,
            max_length=200,
            num_return_sequences=1,
            no_repeat_ngram_size=2
        )
        scenes = self.tokenizer.decode(output[0]).split('.')
        return [scene.strip() for scene in scenes if scene.strip()]
    
    def generate_panel(self, scene_description, style_prompt="comic book style", size=(512, 512)):
        """Generate a single comic panel from scene description"""
        prompt = f"{scene_description}, {style_prompt}"
        image = self.pipe(prompt).images[0]
        return image.resize(size)
    
    def add_speech_bubble(self, image, text, position=(50, 50)):
        """Add speech bubble with text to panel"""
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        
        # Calculate text size
        text_bbox = draw.textbbox(position, text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Draw bubble
        padding = 10
        bubble_bbox = (
            position[0] - padding,
            position[1] - padding,
            position[0] + text_width + padding,
            position[1] + text_height + padding
        )
        draw.rectangle(bubble_bbox, fill="white", outline="black")
        draw.text(position, text, fill="black", font=font)
        
        return image
    
    def create_comic_strip(self, story_prompt, num_panels=4, style="comic book style"):
        """Create complete comic strip from story prompt"""
        # Process story into scenes
        scenes = self.process_story(story_prompt)
        
        # Generate panels
        panels = []
        for i, scene in enumerate(scenes[:num_panels]):
            panel = self.generate_panel(scene, style)
            panels.append(panel)
        
        # Combine panels into strip
        total_width = sum(panel.width for panel in panels)
        max_height = max(panel.height for panel in panels)
        
        comic_strip = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        
        for panel in panels:
            comic_strip.paste(panel, (x_offset, 0))
            x_offset += panel.width
        
        return comic_strip

    def save_comic(self, comic_strip, filename):
        """Save comic strip to file"""
        comic_strip.save(filename)

if __name__ == "__main__":
    # Example usage
    generator = ComicGenerator()
    story = "A cat chases a mouse through a kitchen. The mouse hides in a cookie jar. The cat knocks over the jar. Cookies and mouse scatter everywhere."
    
    comic = generator.create_comic_strip(
        story_prompt=story,
        num_panels=4,
        style="cartoon style, vibrant colors"
    )
    
    generator.save_comic(comic, "example_comic.png")