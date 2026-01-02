"""
Main Dashboard Window
Main application window - refactored
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ui.sidebar import Sidebar
from ui.content_area import ContentArea
from config.config_layout import Layout


class DashboardWindow(Gtk.Window):
    """Main application window"""
    
    def __init__(self, navigation_manager):
        """Initialize window"""
        super().__init__(title="Dashboard")
        
        self.nav_manager = navigation_manager
        
        self.set_default_size(
            Layout.dimensions.WINDOW_DEFAULT_WIDTH,
            Layout.dimensions.WINDOW_DEFAULT_HEIGHT
        )
        self.set_position(Gtk.WindowPosition.CENTER)
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(main_box)
        
        self.sidebar = Sidebar(self.nav_manager)
        self.sidebar.connect("page-changed", self.on_page_changed)
        main_box.pack_start(self.sidebar, False, False, 0)
        
        self.content_area = ContentArea(self.nav_manager)
        main_box.pack_start(self.content_area, True, True, 0)
    
    def on_page_changed(self, sidebar, page_name):
        """Handle page change"""
        self.content_area.show_page(page_name)
