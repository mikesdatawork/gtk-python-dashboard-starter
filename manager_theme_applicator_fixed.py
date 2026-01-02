"""
Theme Applicator
Fixed: Home button has both top AND bottom borders
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class ThemeApplicator:
    """Applies theme colors to the application"""
    
    def __init__(self):
        """Initialize theme applicator"""
        self.css_provider = Gtk.CssProvider()
        self.current_theme = None
    
    def apply_theme(self, theme_def):
        """
        Apply a theme by generating and loading CSS
        
        Args:
            theme_def: ThemeDefinition instance
        """
        self.current_theme = theme_def
        
        # Generate CSS with theme colors
        css_content = self.generate_css(theme_def)
        
        # Load CSS
        try:
            self.css_provider.load_from_data(css_content.encode())
            
            # Apply to screen
            screen = Gdk.Screen.get_default()
            style_context = Gtk.StyleContext()
            style_context.add_provider_for_screen(
                screen,
                self.css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )
            
            print(f"✓ Applied theme: {theme_def.name}")
            return True
            
        except Exception as e:
            print(f"✗ Error applying theme: {e}")
            return False
    
    def generate_css(self, theme_def):
        """
        Generate CSS content with theme colors
        
        Args:
            theme_def: ThemeDefinition instance
        
        Returns:
            str: CSS content
        """
        css = f"""
/* Dynamic theme: {theme_def.name} */

/* Window background */
window {{
    background-color: {theme_def.window_bg};
}}

/* Window titlebar controls */
headerbar {{
    background-color: {theme_def.sidebar_bg};
    background-image: none;
    border-bottom: 1px solid #1a1a1a;
    color: #eeeeee;
}}

headerbar button {{
    background-color: transparent;
    background-image: none;
    border: none;
    color: #d0d0d0;
}}

headerbar button:hover {{
    background-color: {theme_def.hover_color};
}}

headerbar button:active {{
    background-color: {theme_def.accent_color};
}}

/* Sidebar */
.sidebar {{
    background-color: {theme_def.sidebar_bg};
    border-right: 1px solid #1a1a1a;
}}

/* Logo area - no border */
.logo-area {{
    background-color: {theme_def.sidebar_bg};
}}

.logo-text {{
    color: #eeeeee;
    font-size: 13pt;
    font-weight: normal;
}}

/* Navigation buttons */
.nav-button {{
    background-color: transparent;
    background-image: none;
    border: none;
    border-bottom: 1px solid #1a1a1a;
    border-radius: 0;
    padding: 6px 10px;
    margin: 0;
    color: #d0d0d0;
    font-size: 10pt;
    font-weight: normal;
    box-shadow: none;
    min-height: 28px;
}}

.nav-button label {{
    padding-left: 5px;
}}

.nav-button:hover {{
    background-color: {theme_def.hover_color};
    border-color: #1a1a1a;
}}

.nav-button.active {{
    background-color: {theme_def.accent_color};
    color: #ffffff;
    font-weight: bold;
    border-color: #1a1a1a;
}}

.nav-button.active label {{
    font-weight: bold;
}}

.nav-button:focus {{
    outline: none;
    box-shadow: none;
}}

/* Navigation button at top (Home) - add top border, KEEP bottom border */
.nav-button-top {{
    border-top: 1px solid #1a1a1a;
    border-bottom: 1px solid #1a1a1a;
}}

/* Navigation button at bottom (Settings) - top border only, no bottom */
.nav-button-bottom {{
    border-bottom: none;
    border-top: 1px solid #1a1a1a;
}}

/* Content area */
.content-area {{
    background-color: {theme_def.window_bg};
}}

/* Page styling */
.page-title {{
    font-size: 18pt;
    font-weight: bold;
    color: #eeeeee;
    margin-bottom: 10px;
}}

.page-subtitle {{
    font-size: 14pt;
    font-weight: bold;
    color: #eeeeee;
    margin-top: 15px;
    margin-bottom: 5px;
}}

/* Links */
a {{
    color: {theme_def.accent_color};
    text-decoration: none;
}}

a:hover {{
    color: {theme_def.accent_color};
    text-decoration: none;
}}

/* Labels */
label {{
    color: #d0d0d0;
}}

/* Scrollbar styling */
scrollbar {{
    background-color: {theme_def.window_bg};
}}

scrollbar slider {{
    background-color: #555555;
    border-radius: 4px;
}}

scrollbar slider:hover {{
    background-color: #666666;
}}
"""
        return css
