from dataclasses import dataclass
from typing import List, Tuple, Dict
from enum import Enum

class PanelLayout(Enum):
    GRID = "grid"
    DIAGONAL = "diagonal"
    DYNAMIC = "dynamic"

class ArtStyle(Enum):
    MANGA = "manga style, black and white, detailed linework"
    WESTERN = "western comic book style, vibrant colors, bold outlines"
    CARTOON = "cartoon style, simple shapes, bright colors"
    REALISTIC = "realistic style, detailed shading, natural colors"

@dataclass
class FontConfig:
    name: str
    size: int
    color: str
    bubble_style: str = "round"  # round, square, thought

@dataclass
class StyleConfig:
    art_style: ArtStyle
    panel_layout: PanelLayout
    panel_size: Tuple[int, int]
    panel_spacing: int
    background_color: str
    border_color: str
    border_width: int
    font: FontConfig

class StylePresets:
    @staticmethod
    def get_manga_style() -> StyleConfig:
        return StyleConfig(
            art_style=ArtStyle.MANGA,
            panel_layout=PanelLayout.GRID,
            panel_size=(512, 512),
            panel_spacing=10,
            background_color="white",
            border_color="black",
            border_width=2,
            font=FontConfig(
                name="CC Wild Words",
                size=14,
                color="black",
                bubble_style="round"
            )
        )

    @staticmethod
    def get_western_style() -> StyleConfig:
        return StyleConfig(
            art_style=ArtStyle.WESTERN,
            panel_layout=PanelLayout.DYNAMIC,
            panel_size=(600, 400),
            panel_spacing=15,
            background_color="white",
            border_color="black",
            border_width=3,
            font=FontConfig(
                name="Comic Sans MS",
                size=16,
                color="black",
                bubble_style="square"
            )
        )

    @staticmethod
    def get_cartoon_style() -> StyleConfig:
        return StyleConfig(
            art_style=ArtStyle.CARTOON,
            panel_layout=PanelLayout.GRID,
            panel_size=(400, 400),
            panel_spacing=12,
            background_color="white",
            border_color="black",
            border_width=2,
            font=FontConfig(
                name="Arial Rounded MT Bold",
                size=14,
                color="black",
                bubble_style="round"
            )
        )

class LayoutManager:
    @staticmethod
    def calculate_grid_layout(num_panels: int, panel_size: Tuple[int, int], spacing: int) -> List[Tuple[int, int]]:
        """Calculate positions for a grid layout"""
        positions = []
        max_cols = min(num_panels, 3)  # Maximum 3 panels per row
        rows = (num_panels + max_cols - 1) // max_cols

        for i in range(num_panels):
            row = i // max_cols
            col = i % max_cols
            x = col * (panel_size[0] + spacing)
            y = row * (panel_size[1] + spacing)
            positions.append((x, y))

        return positions

    @staticmethod
    def calculate_dynamic_layout(num_panels: int, panel_size: Tuple[int, int], spacing: int) -> List[Dict]:
        """Calculate positions and sizes for a dynamic layout"""
        layouts = []
        base_width, base_height = panel_size

        if num_panels == 1:
            layouts.append({"pos": (0, 0), "size": panel_size})
        elif num_panels == 2:
            layouts.extend([
                {"pos": (0, 0), "size": (base_width, base_height)},
                {"pos": (base_width + spacing, 0), "size": (base_width, base_height)}
            ])
        elif num_panels == 3:
            layouts.extend([
                {"pos": (0, 0), "size": (base_width, base_height)},
                {"pos": (base_width + spacing, 0), "size": (base_width, base_height // 2)},
                {"pos": (base_width + spacing, base_height // 2 + spacing), "size": (base_width, base_height // 2)}
            ])
        else:
            # Default to grid layout for more than 3 panels
            positions = LayoutManager.calculate_grid_layout(num_panels, panel_size, spacing)
            layouts.extend([{"pos": pos, "size": panel_size} for pos in positions])

        return layouts