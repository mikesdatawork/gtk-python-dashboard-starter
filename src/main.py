#!/usr/bin/env python3
"""
GTK Python Dashboard Starter
Main application entry point
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys
import os

from ui.dashboard_window import DashboardWindow


def main():
    """Main application entry point"""
    # Load CSS
    css_provider = Gtk.CssProvider()
    css_file = os.path.join(os.path.dirname(__file__), '..', 'resources', 'css', 'style.css')
    
    if os.path.exists(css_file):
        css_provider.load_from_path(css_file)
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen,
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    
    # Create and show main window
    window = DashboardWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    
    Gtk.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
