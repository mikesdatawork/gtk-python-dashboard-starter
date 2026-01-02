#!/usr/bin/env python3
"""
GTK Python Dashboard Starter
Main application entry point - applies default theme on startup
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

from ui.dashboard_window import DashboardWindow
from modules.manager_navigation import NavigationManager
from modules.manager_theme_applicator import ThemeApplicator
from config.config_themes import get_theme


def main():
    """Main application entry point"""
    
    # Initialize managers
    navigation_manager = NavigationManager()
    theme_applicator = ThemeApplicator()
    
    # Apply default theme immediately for consistent startup
    default_theme = get_theme('default')
    theme_applicator.apply_theme(default_theme)
    
    # Create and show main window
    window = DashboardWindow(navigation_manager)
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    
    # Start GTK main loop
    Gtk.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
