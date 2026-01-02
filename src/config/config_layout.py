"""
Layout Configuration
Centralized layout dimensions and spacing constants
"""

class Dimensions:
    """Layout dimension constants"""
    
    # Sidebar
    SIDEBAR_WIDTH = 150
    
    # Logo area
    LOGO_AREA_WIDTH = 150
    LOGO_AREA_HEIGHT = 150
    LOGO_IMAGE_SIZE = 145
    
    # Navigation buttons
    NAV_BUTTON_HEIGHT = 28
    NAV_BUTTON_PADDING_V = 6
    NAV_BUTTON_PADDING_H = 10
    
    # Content area
    CONTENT_MARGIN = 40
    CONTENT_SPACING = 15
    
    # Window
    WINDOW_DEFAULT_WIDTH = 1200
    WINDOW_DEFAULT_HEIGHT = 800


class Spacing:
    """Spacing constants"""
    
    NONE = 0
    SMALL = 5
    MEDIUM = 10
    LARGE = 15
    XLARGE = 20


class Layout:
    """Main layout configuration"""
    
    dimensions = Dimensions
    spacing = Spacing
