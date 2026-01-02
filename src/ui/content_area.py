"""
Content Area Component
Stack container for pages with individual scroll states
Updated: Each page wrapped in its own ScrolledWindow
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from pages.page_home import HomePage
from pages.page_about import AboutPage
from pages.page_button03 import Button03Page
from pages.page_button04 import Button04Page
from pages.page_button05 import Button05Page
from pages.page_button06 import Button06Page
from pages.page_settings import SettingsPage


class ContentArea(Gtk.Box):
    """Content area with page navigation and individual scroll states"""
    
    def __init__(self, navigation_manager):
        """Initialize content area"""
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        self.nav_manager = navigation_manager
        
        # Style class for content area
        self.get_style_context().add_class('content-area')
        
        # Create stack for pages - NO transitions
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.NONE)
        self.pack_start(self.stack, True, True, 0)
        
        # Register stack with navigation manager
        self.nav_manager.set_page_stack(self.stack)
        
        # Register pages
        self.register_pages()
    
    def wrap_page_in_scrolled_window(self, page):
        """
        Wrap a page in its own ScrolledWindow
        This ensures each page maintains its own scroll state
        
        Args:
            page: Page widget to wrap
        
        Returns:
            Gtk.ScrolledWindow containing the page
        """
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(page)
        return scrolled_window
    
    def register_pages(self):
        """Register all application pages with individual scroll states"""
        
        # Create page instances
        home_page = HomePage()
        about_page = AboutPage()
        button03_page = Button03Page()
        button04_page = Button04Page()
        button05_page = Button05Page()
        button06_page = Button06Page()
        settings_page = SettingsPage()
        
        # Wrap each page in its own ScrolledWindow
        home_scrolled = self.wrap_page_in_scrolled_window(home_page)
        about_scrolled = self.wrap_page_in_scrolled_window(about_page)
        button03_scrolled = self.wrap_page_in_scrolled_window(button03_page)
        button04_scrolled = self.wrap_page_in_scrolled_window(button04_page)
        button05_scrolled = self.wrap_page_in_scrolled_window(button05_page)
        button06_scrolled = self.wrap_page_in_scrolled_window(button06_page)
        settings_scrolled = self.wrap_page_in_scrolled_window(settings_page)
        
        # Add wrapped pages to stack
        self.stack.add_named(home_scrolled, "home")
        self.stack.add_named(about_scrolled, "about")
        self.stack.add_named(button03_scrolled, "button03")
        self.stack.add_named(button04_scrolled, "button04")
        self.stack.add_named(button05_scrolled, "button05")
        self.stack.add_named(button06_scrolled, "button06")
        self.stack.add_named(settings_scrolled, "settings")
        
        # Register original pages with navigation manager
        self.nav_manager.register_page("home", home_page)
        self.nav_manager.register_page("about", about_page)
        self.nav_manager.register_page("button03", button03_page)
        self.nav_manager.register_page("button04", button04_page)
        self.nav_manager.register_page("button05", button05_page)
        self.nav_manager.register_page("button06", button06_page)
        self.nav_manager.register_page("settings", settings_page)
    
    def show_page(self, page_id):
        """Show a specific page"""
        self.nav_manager.navigate_to(page_id)
