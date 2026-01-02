"""
Base Page Class
Abstract base class for all application pages
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class BasePage(Gtk.Box):
    """
    Base class for all dashboard pages
    
    All pages should inherit from this class and implement build_content()
    """
    
    def __init__(self, spacing=15, margin=40):
        """
        Initialize base page
        
        Args:
            spacing: Vertical spacing between elements
            margin: Margin around page content
        """
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=spacing)
        
        # Set margins
        self.set_margin_start(margin)
        self.set_margin_end(margin)
        self.set_margin_top(margin)
        self.set_margin_bottom(margin)
        
        # Build page content
        self.build_content()
    
    def build_content(self):
        """
        Build page content - override this in subclasses
        
        This method should create and pack all page widgets
        """
        raise NotImplementedError("Subclasses must implement build_content()")
    
    def add_title(self, text):
        """Add a page title"""
        title = Gtk.Label(label=text)
        title.get_style_context().add_class('page-title')
        title.set_xalign(0)
        self.pack_start(title, False, False, 0)
        return title
    
    def add_subtitle(self, text):
        """Add a page subtitle"""
        subtitle = Gtk.Label(label=text)
        subtitle.get_style_context().add_class('page-subtitle')
        subtitle.set_xalign(0)
        self.pack_start(subtitle, False, False, 5)
        return subtitle
    
    def add_paragraph(self, text, wrap=True, spacing_after=0):
        """Add a paragraph of text"""
        paragraph = Gtk.Label(label=text)
        paragraph.set_line_wrap(wrap)
        paragraph.set_xalign(0)
        self.pack_start(paragraph, False, False, spacing_after)
        return paragraph
    
    def add_markup_label(self, markup, wrap=False, selectable=False, spacing_after=0):
        """Add a label with markup support"""
        label = Gtk.Label()
        label.set_markup(markup)
        label.set_line_wrap(wrap)
        label.set_xalign(0)
        label.set_selectable(selectable)
        self.pack_start(label, False, False, spacing_after)
        return label
