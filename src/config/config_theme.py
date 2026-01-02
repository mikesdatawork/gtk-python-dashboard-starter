"""
Theme Configuration
Centralized color scheme and styling constants
"""

# Color Scheme
class Colors:
    """Application color palette"""
    
    # Background colors
    WINDOW_BG = "#2d2d2d"           # Darker gray
    SIDEBAR_BG = "#353535"          # Dark gray
    LOGO_AREA_BG = "#3a3a3a"        # Medium dark gray
    CONTENT_BG = "#2d2d2d"          # Darker gray
    INPUT_BG = "#3a3a3a"            # Medium dark gray
    
    # Button colors
    NAV_BUTTON_ACTIVE = "#0078D7"   # Windows blue
    NAV_BUTTON_HOVER = "#404040"    # Medium gray
    BUTTON_BG = "#404040"           # Medium gray
    BUTTON_HOVER = "#4a4a4a"        # Lighter gray
    
    # Text colors
    TEXT_PRIMARY = "#eeeeee"        # Off-white
    TEXT_SECONDARY = "#d0d0d0"      # Light gray
    TEXT_DISABLED = "#808080"       # Medium gray
    
    # Accent colors
    PRIMARY_ACCENT = "#0078D7"      # Windows blue
    PRIMARY_ACCENT_HOVER = "#1084E3"  # Lighter blue
    SUCCESS = "#27ae60"             # Green
    WARNING = "#f39c12"             # Orange
    ERROR = "#cc3333"               # Red
    INFO = "#0078D7"                # Blue
    
    # Border colors
    BORDER_DARK = "#1a1a1a"         # Almost black
    BORDER_MEDIUM = "#555555"       # Medium gray
    
    # Link colors
    LINK = "#0078D7"                # Windows blue
    LINK_HOVER = "#1084E3"          # Lighter blue
    LINK_VISITED = "#0078D7"        # Same as link


class Fonts:
    """Font configuration"""
    
    FAMILY = "Ubuntu, Cantarell, sans-serif"
    FAMILY_MONO = "monospace"
    
    SIZE_DEFAULT = "11pt"
    SIZE_SMALL = "9pt"
    SIZE_MEDIUM = "14pt"
    SIZE_LARGE = "18pt"
    SIZE_LOGO = "13pt"


class Theme:
    """Main theme configuration"""
    
    colors = Colors
    fonts = Fonts
    
    # CSS file path
    CSS_FILE = "resources/css/style.css"
