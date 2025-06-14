from comic_generator import ComicGenerator
from style_config import StylePresets, ArtStyle, PanelLayout
import os

def generate_sample_comics():
    # Initialize generator
    generator = ComicGenerator()
    
    # Sample stories for demonstration
    stories = [
        {
            "title": "Cat and Mouse",
            "prompt": "A cat chases a mouse through a kitchen. The mouse hides in a cookie jar. The cat knocks over the jar. Cookies and mouse scatter everywhere.",
            "style": StylePresets.get_cartoon_style()
        },
        {
            "title": "Superhero",
            "prompt": "A superhero discovers their powers. They accidentally break a window. They practice controlling their strength. Finally they save someone from danger.",
            "style": StylePresets.get_western_style()
        },
        {
            "title": "School Day",
            "prompt": "A student rushes to catch the bus. They make it just in time. They realize they forgot their homework. Their friend helps them out.",
            "style": StylePresets.get_manga_style()
        }
    ]
    
    # Create output directory
    os.makedirs("sample_comics", exist_ok=True)
    
    # Generate comics with different styles
    for story in stories:
        print(f"Generating {story['title']}...")
        
        # Create comic strip
        comic = generator.create_comic_strip(
            story_prompt=story['prompt'],
            num_panels=4,
            style=story['style'].art_style.value
        )
        
        # Save comic
        filename = f"sample_comics/{story['title'].lower().replace(' ', '_')}.png"
        generator.save_comic(comic, filename)
        print(f"Saved {filename}")

def demonstrate_layouts():
    """Demonstrate different panel layouts"""
    generator = ComicGenerator()
    story = "A character walks through four seasons. Spring flowers bloom. Summer sun shines. Autumn leaves fall. Winter snow covers everything."
    
    layouts = [
        (PanelLayout.GRID, "grid_layout"),
        (PanelLayout.DIAGONAL, "diagonal_layout"),
        (PanelLayout.DYNAMIC, "dynamic_layout")
    ]
    
    os.makedirs("layout_demos", exist_ok=True)
    
    for layout, name in layouts:
        style_config = StylePresets.get_cartoon_style()
        style_config.panel_layout = layout
        
        comic = generator.create_comic_strip(
            story_prompt=story,
            num_panels=4,
            style=style_config.art_style.value
        )
        
        filename = f"layout_demos/{name}.png"
        generator.save_comic(comic, filename)
        print(f"Generated {name} demonstration")

def demonstrate_character_consistency():
    """Demonstrate character consistency across panels"""
    generator = ComicGenerator()
    
    character_desc = "A young woman with long black hair, wearing a red dress"
    story = f"{character_desc} walks through different environments. She's in a garden. She's in a library. She's in a cafe. She's in a park."
    
    style_config = StylePresets.get_western_style()
    comic = generator.create_comic_strip(
        story_prompt=story,
        num_panels=4,
        style=f"{style_config.art_style.value}, consistent character appearance, {character_desc}"
    )
    
    os.makedirs("character_demos", exist_ok=True)
    generator.save_comic(comic, "character_demos/character_consistency.png")
    print("Generated character consistency demonstration")

def main():
    print("Comic Strip Generator Demo")
    print("=========================\n")
    
    print("1. Generating sample comics with different styles...")
    generate_sample_comics()
    
    print("\n2. Demonstrating different panel layouts...")
    demonstrate_layouts()
    
    print("\n3. Demonstrating character consistency...")
    demonstrate_character_consistency()
    
    print("\nDemo completed! Check the output directories for results.")

if __name__ == "__main__":
    main()