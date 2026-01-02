#!/usr/bin/env python3
"""
GTK Python Dashboard Starter
Main application entry point - refactored for modularity
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

from ui.dashboard_window import DashboardWindow
from utils.manager_theme import ThemeManager
from modules.manager_navigation import NavigationManager
from config.config_theme import Theme


def main():
    """Main application entry point"""
    
    # Initialize managers
    theme_manager = ThemeManager()
    navigation_manager = NavigationManager()
    
    # Load theme CSS
    theme_manager.load_css(Theme.CSS_FILE)
    
    # Create and show main window
    window = DashboardWindow(navigation_manager)
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    
    # Start GTK main loop
    Gtk.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
