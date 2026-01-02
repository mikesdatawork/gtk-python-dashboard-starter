"""
Main dashboard window
Replicates the C GTK template's dashboard window structure
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

from ui.sidebar import Sidebar
from ui.content_area import ContentArea


class DashboardWindow(Gtk.Window):
    """Main application window with sidebar and content area"""
    
    def __init__(self):
        """Initialize the dashboard window"""
        super().__init__(title="Dashboard")
        
        # Window properties
        self.set_default_size(1200, 800)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        # Main container - horizontal box for sidebar + content
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(main_box)
        
        # Create sidebar
        self.sidebar = Sidebar()
        self.sidebar.connect("page-changed", self.on_page_changed)
        main_box.pack_start(self.sidebar, False, False, 0)
        
        # Create content area
        self.content_area = ContentArea()
        main_box.pack_start(self.content_area, True, True, 0)
    
    def on_page_changed(self, sidebar, page_name):
        """Handle sidebar navigation"""
        self.content_area.show_page(page_name)
