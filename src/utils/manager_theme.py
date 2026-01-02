"""
Theme Manager
Handles CSS loading and theme management
FIXED: Correct path calculation for CSS file
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import os


class ThemeManager:
    """Manages application theme and CSS"""
    
    def __init__(self):
        """Initialize theme manager"""
        self.css_provider = None
    
    def load_css(self, css_path):
        """
        Load CSS file for the application
        
        Args:
            css_path: Path to CSS file relative to project root
        """
        self.css_provider = Gtk.CssProvider()
        
        # Calculate correct path
        if not os.path.isabs(css_path):
            # Get project root (go up 3 levels from src/utils/manager_theme.py)
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            css_file = os.path.join(base_dir, css_path)
        else:
            css_file = css_path
        
        # Load CSS file
        if os.path.exists(css_file):
            try:
                self.css_provider.load_from_path(css_file)
                
                # Apply to screen
                screen = Gdk.Screen.get_default()
                style_context = Gtk.StyleContext()
                style_context.add_provider_for_screen(
                    screen,
                    self.css_provider,
                    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
                )
                print(f"✓ Loaded CSS: {css_file}")
                return True
            except Exception as e:
                print(f"✗ Error loading CSS: {e}")
                return False
        else:
            print(f"✗ CSS file not found: {css_file}")
            return False
    
    def reload_css(self, css_path):
        """Reload CSS file (useful for development)"""
        return self.load_css(css_path)
