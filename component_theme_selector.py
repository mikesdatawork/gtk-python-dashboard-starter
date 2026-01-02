"""
Theme Selector Widget
Visual theme selector similar to Linux Mint
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import cairo


class ThemeColorButton(Gtk.DrawingArea):
    """
    Custom widget that displays a colored circle for theme selection
    Similar to Linux Mint's theme selector
    """
    
    def __init__(self, theme_id, theme_def, callback):
        """
        Initialize theme color button
        
        Args:
            theme_id: Theme identifier
            theme_def: ThemeDefinition instance
            callback: Function to call when clicked
        """
        super().__init__()
        
        self.theme_id = theme_id
        self.theme_def = theme_def
        self.callback = callback
        self.is_selected = False
        
        # Set size
        self.set_size_request(50, 50)
        
        # Connect signals
        self.connect('draw', self.on_draw)
        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.connect('button-press-event', self.on_clicked)
        
        # Tooltip
        self.set_tooltip_text(theme_def.name)
    
    def on_draw(self, widget, cr):
        """Draw the colored circle"""
        allocation = widget.get_allocation()
        width = allocation.width
        height = allocation.height
        
        # Center point
        cx = width / 2
        cy = height / 2
        
        # Circle radius
        radius = min(width, height) / 2 - 4
        
        # Parse accent color
        color = Gdk.RGBA()
        color.parse(self.theme_def.accent_color)
        
        # Draw circle
        cr.arc(cx, cy, radius, 0, 2 * 3.14159)
        cr.set_source_rgb(color.red, color.green, color.blue)
        cr.fill()
        
        # Draw selection ring if selected
        if self.is_selected:
            cr.arc(cx, cy, radius + 2, 0, 2 * 3.14159)
            cr.set_source_rgb(1, 1, 1)
            cr.set_line_width(2)
            cr.stroke()
        
        return False
    
    def on_clicked(self, widget, event):
        """Handle click event"""
        if self.callback:
            self.callback(self.theme_id)
        return True
    
    def set_selected(self, selected):
        """Set selection state"""
        self.is_selected = selected
        self.queue_draw()


class ThemeSelectorWidget(Gtk.Box):
    """
    Theme selector widget with color circles
    Similar to Linux Mint's theme chooser
    """
    
    def __init__(self, themes_dict, current_theme='default', on_theme_changed=None):
        """
        Initialize theme selector
        
        Args:
            themes_dict: Dictionary of theme_id -> ThemeDefinition
            current_theme: Currently selected theme ID
            on_theme_changed: Callback when theme changes
        """
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        
        self.themes_dict = themes_dict
        self.current_theme = current_theme
        self.on_theme_changed = on_theme_changed
        self.color_buttons = {}
        
        # Create color buttons for each theme
        for theme_id, theme_def in themes_dict.items():
            button = ThemeColorButton(theme_id, theme_def, self.theme_clicked)
            button.set_selected(theme_id == current_theme)
            self.pack_start(button, False, False, 0)
            self.color_buttons[theme_id] = button
    
    def theme_clicked(self, theme_id):
        """Handle theme selection"""
        # Update selection state
        for tid, button in self.color_buttons.items():
            button.set_selected(tid == theme_id)
        
        self.current_theme = theme_id
        
        # Trigger callback
        if self.on_theme_changed:
            self.on_theme_changed(theme_id)
    
    def get_selected_theme(self):
        """Get currently selected theme ID"""
        return self.current_theme
