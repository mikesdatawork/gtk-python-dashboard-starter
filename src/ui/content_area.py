"""
Content area component
Scrollable area that displays different pages
Updated: no transitions, left-aligned text
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class ContentArea(Gtk.ScrolledWindow):
    """Scrollable content area with multiple pages"""
    
    def __init__(self):
        """Initialize the content area"""
        super().__init__()
        
        # Scrolled window properties
        self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.get_style_context().add_class('content-area')
        
        # Create stack for pages - NO transitions
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.NONE)
        self.add(self.stack)
        
        # Create default pages
        self.create_pages()
    
    def create_pages(self):
        """Create the default pages with left-aligned text"""
        # Home page
        home_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        home_page.set_margin_start(40)
        home_page.set_margin_end(40)
        home_page.set_margin_top(40)
        
        home_title = Gtk.Label(label="Welcome to Dashboard")
        home_title.get_style_context().add_class('page-title')
        home_title.set_xalign(0)  # Left align
        home_page.pack_start(home_title, False, False, 0)
        
        home_content = Gtk.Label(
            label="This is a Python GTK3 dashboard starter template.\n"
                  "Use the sidebar to navigate between pages."
        )
        home_content.set_line_wrap(True)
        home_content.set_xalign(0)  # Left align
        home_page.pack_start(home_content, False, False, 0)
        
        self.stack.add_named(home_page, "home")
        
        # Settings page
        settings_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        settings_page.set_margin_start(40)
        settings_page.set_margin_end(40)
        settings_page.set_margin_top(40)
        
        settings_title = Gtk.Label(label="Settings")
        settings_title.get_style_context().add_class('page-title')
        settings_title.set_xalign(0)  # Left align
        settings_page.pack_start(settings_title, False, False, 0)
        
        settings_content = Gtk.Label(label="Settings page content goes here.")
        settings_content.set_xalign(0)  # Left align
        settings_page.pack_start(settings_content, False, False, 0)
        
        self.stack.add_named(settings_page, "settings")
        
        # About page
        about_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        about_page.set_margin_start(40)
        about_page.set_margin_end(40)
        about_page.set_margin_top(40)
        
        about_title = Gtk.Label(label="About")
        about_title.get_style_context().add_class('page-title')
        about_title.set_xalign(0)  # Left align
        about_page.pack_start(about_title, False, False, 0)
        
        about_content = Gtk.Label(
            label="GTK Python Dashboard Starter\nVersion 1.0\n\n"
                  "A modular template for building GTK3 applications in Python."
        )
        about_content.set_line_wrap(True)
        about_content.set_xalign(0)  # Left align
        about_page.pack_start(about_content, False, False, 0)
        
        self.stack.add_named(about_page, "about")
    
    def show_page(self, page_name):
        """Show a specific page"""
        self.stack.set_visible_child_name(page_name)
