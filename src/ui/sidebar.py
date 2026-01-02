"""
Sidebar Component
Fixed sidebar with logo and navigation
Updated: Settings button at bottom with spacer
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GObject
import os

from config.config_layout import Layout


class Sidebar(Gtk.Box):
    """Fixed sidebar with logo and navigation buttons"""
    
    __gsignals__ = {
        'page-changed': (GObject.SignalFlags.RUN_FIRST, None, (str,))
    }
    
    def __init__(self, navigation_manager):
        """Initialize sidebar"""
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        self.nav_manager = navigation_manager
        
        self.set_size_request(Layout.dimensions.SIDEBAR_WIDTH, -1)
        self.get_style_context().add_class('sidebar')
        
        self.active_button = None
        
        self.build_logo_area()
        self.build_navigation()
        
        if "home" in self.nav_buttons:
            self.set_active_button(self.nav_buttons["home"])
            self.nav_manager.navigate_to("home")
    
    def build_logo_area(self):
        """Build logo area"""
        
        logo_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        logo_box.set_size_request(
            Layout.dimensions.LOGO_AREA_WIDTH,
            Layout.dimensions.LOGO_AREA_HEIGHT
        )
        logo_box.get_style_context().add_class('logo-area')
        
        logo_path = self.get_logo_path()
        if os.path.exists(logo_path):
            try:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                    logo_path,
                    Layout.dimensions.LOGO_IMAGE_SIZE,
                    Layout.dimensions.LOGO_IMAGE_SIZE,
                    True
                )
                logo_image = Gtk.Image.new_from_pixbuf(pixbuf)
                logo_box.pack_start(logo_image, True, True, 0)
            except Exception as e:
                print(f"Could not load logo: {e}")
                self.add_fallback_logo(logo_box)
        else:
            self.add_fallback_logo(logo_box)
        
        self.pack_start(logo_box, False, False, 0)
    
    def get_logo_path(self):
        """Get path to logo image"""
        return os.path.join(
            os.path.dirname(__file__), '..', '..',
            'resources', 'images', 'logo.png'
        )
    
    def add_fallback_logo(self, container):
        """Add fallback logo text"""
        logo_label = Gtk.Label(label="DASHBOARD")
        logo_label.get_style_context().add_class('logo-text')
        logo_label.set_xalign(0.5)
        container.pack_start(logo_label, True, True, 0)
    
    def build_navigation(self):
        """Build navigation area with Settings at bottom"""
        
        # Top navigation container
        nav_box_top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        # Main navigation items (not including Settings)
        nav_items = [
            ("Home", "home"),
            ("About", "about"),
            ("Button03", "button03"),
            ("Button04", "button04"),
            ("Button05", "button05"),
            ("Button06", "button06")
        ]
        
        self.nav_buttons = {}
        for label, page_id in nav_items:
            button = self.create_nav_button(label, page_id)
            nav_box_top.pack_start(button, False, False, 0)
            self.nav_buttons[page_id] = button
        
        # Add top navigation
        self.pack_start(nav_box_top, False, False, 0)
        
        # Add expanding spacer to push Settings to bottom
        spacer = Gtk.Box()
        self.pack_start(spacer, True, True, 0)
        
        # Bottom navigation container for Settings
        nav_box_bottom = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        settings_button = self.create_nav_button("Settings", "settings")
        nav_box_bottom.pack_start(settings_button, False, False, 0)
        self.nav_buttons["settings"] = settings_button
        
        # Add bottom navigation
        self.pack_start(nav_box_bottom, False, False, 0)
    
    def create_nav_button(self, label, page_id):
        """Create navigation button"""
        button = Gtk.Button(label=label)
        button.get_style_context().add_class('nav-button')
        button.set_relief(Gtk.ReliefStyle.NONE)
        button.connect("clicked", self.on_nav_clicked, page_id)
        
        button_label = button.get_child()
        button_label.set_xalign(0)
        
        return button
    
    def set_active_button(self, button):
        """Set button as active"""
        if self.active_button:
            self.active_button.get_style_context().remove_class('active')
        
        button.get_style_context().add_class('active')
        self.active_button = button
    
    def on_nav_clicked(self, button, page_id):
        """Handle navigation click"""
        self.set_active_button(button)
        self.nav_manager.navigate_to(page_id)
        self.emit('page-changed', page_id)
