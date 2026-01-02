"""
Sidebar component
Fixed-height dark sidebar with navigation buttons
Updated: Settings button at bottom of list
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GObject
import os


class Sidebar(Gtk.Box):
    """Fixed sidebar with logo and navigation buttons"""
    
    # Define signal for page changes
    __gsignals__ = {
        'page-changed': (GObject.SignalFlags.RUN_FIRST, None, (str,))
    }
    
    def __init__(self):
        """Initialize the sidebar"""
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        # Set sidebar properties
        self.set_size_request(150, -1)
        self.get_style_context().add_class('sidebar')
        
        # Track active button
        self.active_button = None
        
        # Logo area - 70px height, 150px width
        logo_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        logo_box.set_size_request(-1, 70)
        logo_box.get_style_context().add_class('logo-area')
        
        # Try to load logo - scale to fill most of the area
        logo_path = os.path.join(os.path.dirname(__file__), '..', '..', 
                                 'resources', 'images', 'logo.png')
        if os.path.exists(logo_path):
            try:
                # Scale to 140x65 to fill more of the 150x70 area
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                    logo_path, 140, 65, True
                )
                logo_image = Gtk.Image.new_from_pixbuf(pixbuf)
                logo_box.pack_start(logo_image, True, True, 2)
            except Exception as e:
                print(f"Could not load logo: {e}")
                logo_label = Gtk.Label(label="DASHBOARD")
                logo_label.get_style_context().add_class('logo-text')
                logo_label.set_xalign(0.5)  # Center horizontally
                logo_box.pack_start(logo_label, True, True, 0)
        else:
            logo_label = Gtk.Label(label="DASHBOARD")
            logo_label.get_style_context().add_class('logo-text')
            logo_label.set_xalign(0.5)  # Center horizontally
            logo_box.pack_start(logo_label, True, True, 0)
        
        self.pack_start(logo_box, False, False, 0)
        
        # Navigation buttons - no spacing, no margins
        nav_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        nav_box.set_margin_top(0)
        nav_box.set_margin_start(0)
        nav_box.set_margin_end(0)
        
        # Define navigation items - Settings moved to bottom
        nav_items = [
            ("Home", "home"),
            ("About", "about"),
            ("Settings", "settings")
        ]
        
        self.nav_buttons = {}
        for label, page_id in nav_items:
            button = Gtk.Button(label=label)
            button.get_style_context().add_class('nav-button')
            button.set_relief(Gtk.ReliefStyle.NONE)  # Remove button relief
            button.connect("clicked", self.on_nav_clicked, page_id)
            
            # Left-align button label
            button_label = button.get_child()
            button_label.set_xalign(0)  # Left align
            
            nav_box.pack_start(button, False, False, 0)
            self.nav_buttons[page_id] = button
        
        # Set first button as active by default
        if "home" in self.nav_buttons:
            self.set_active_button(self.nav_buttons["home"])
        
        self.pack_start(nav_box, False, False, 0)
    
    def set_active_button(self, button):
        """Set a button as active and remove active state from others"""
        # Remove active class from previous button
        if self.active_button:
            self.active_button.get_style_context().remove_class('active')
        
        # Add active class to new button
        button.get_style_context().add_class('active')
        self.active_button = button
    
    def on_nav_clicked(self, button, page_id):
        """Handle navigation button click"""
        self.set_active_button(button)
        self.emit('page-changed', page_id)
