# AI Comic Strip Generator

An advanced Python-based system that generates comic strips from story prompts using state-of-the-art AI models. The system combines GPT-2 for story processing and Stable Diffusion for image generation to create visually appealing comics with consistent character appearances and various artistic styles.

## Features

### Story Processing
- Automatic scene breakdown from text prompts
- Character consistency maintenance
- Dialog extraction and processing
- Natural language understanding using GPT-2

### Image Generation
- AI-powered image creation using Stable Diffusion
- Multiple artistic styles (Manga, Western, Cartoon, Realistic)
- Consistent character appearance across panels
- High-quality panel generation

### Layout and Styling
- Multiple panel layouts (Grid, Diagonal, Dynamic)
- Customizable panel sizes and spacing
- Speech bubble integration
- Font and text styling options

## Project Structure

```
├── comic_generator.py   # Core generation engine
├── style_config.py      # Style and layout configurations
├── demo.py              # Demonstration scripts
├── requirements.txt     # Project dependencies
└── Demo File Outputs/   # Example outputs
    ├── sample_comics/   # Various style examples
    ├── layout_demos/    # Layout demonstrations
    └── character_demos/ # Character consistency examples
```

## Installation

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Example

```python
from comic_generator import ComicGenerator
from style_config import StylePresets

# Initialize the generator
generator = ComicGenerator()

# Create a comic strip
story = "A cat chases a mouse through a kitchen. The mouse hides in a cookie jar. The cat knocks over the jar. Cookies and mouse scatter everywhere."

comic = generator.create_comic_strip(
    story_prompt=story,
    num_panels=4,
    style="cartoon style, vibrant colors"
)

# Save the comic
generator.save_comic(comic, "my_comic.png")
```

### Style Customization

```python
from style_config import StylePresets

# Available preset styles
manga_style = StylePresets.get_manga_style()
western_style = StylePresets.get_western_style()
cartoon_style = StylePresets.get_cartoon_style()
```

### Running Demos

The project includes comprehensive demonstrations:

```bash
python demo.py
```

This will generate:
- Sample comics in different styles
- Layout demonstrations
- Character consistency examples

## Example Outputs

The `Demo File Outputs` directory contains example outputs:
- `sample_comics/`: Different style examples
- `layout_demos/`: Panel layout demonstrations
- `character_demos/`: Character consistency examples

## Requirements

- Python 3.8+
- CUDA-compatible GPU (recommended for faster generation)
- Required packages listed in `requirements.txt`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for providing the transformer models
- Stability AI for the Stable Diffusion model
- The open-source AI community