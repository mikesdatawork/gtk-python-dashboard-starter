"""
Settings Page
Dashboard configuration and technical details
Updated: Accurate tree structure after cleanup
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from pages.page_base import BasePage
from config.config_themes import get_all_themes, get_theme
from ui.components.component_theme_selector import ThemeSelectorWidget
from modules.manager_theme_applicator import ThemeApplicator


class SettingsPage(BasePage):
    """Settings page with theme selector and configuration information"""
    
    def __init__(self):
        """Initialize settings page"""
        self.theme_applicator = ThemeApplicator()
        self.current_theme_id = 'default'
        super().__init__()
    
    def build_content(self):
        """Build settings page content"""
        
        self.add_title("Dashboard Configuration")
        
        self.add_paragraph(
            "Customize your dashboard appearance and view technical details."
        )
        
        # Theme selector section
        self.add_subtitle("Theme")
        
        # Create theme selector widget
        themes = get_all_themes()
        theme_selector = ThemeSelectorWidget(
            themes,
            current_theme=self.current_theme_id,
            on_theme_changed=self.on_theme_changed
        )
        self.pack_start(theme_selector, False, False, 10)
        
        # Technical specs section
        self.add_subtitle("Technical Specifications")
        
        self.add_paragraph(
            "• GTK Version: GTK+ 3.0\n"
            "• Python: 3.8+\n"
            "• Dependencies: PyGObject, pycairo, Pillow\n"
            "• Architecture: Modular with page-based routing\n"
            "• Sidebar Width: 150px\n"
            "• Logo Area: 150x150px (square)\n"
            "• Navigation Button Height: 28px\n"
            "• Navigation Pages: 7 (Home, About, Button03-06, Settings)\n"
            "• Themes: 7 popular dark themes available\n"
            "• License: Free for personal and educational use"
        )
        
        # Project structure section
        self.add_subtitle("Project Structure")
        
        self.add_markup_label(
            "<span font_family='monospace' foreground='#d0d0d0'>"
            "gtk-python-dashboard-starter/\n"
            "├── src/                     # Application source code\n"
            "│   ├── main.py              # Entry point\n"
            "│   ├── config/              # Configuration modules\n"
            "│   │   ├── __init__.py\n"
            "│   │   ├── config_theme.py  # Theme colors/fonts\n"
            "│   │   ├── config_layout.py # Layout dimensions\n"
            "│   │   └── config_themes.py # Theme definitions\n"
            "│   ├── ui/                  # UI components\n"
            "│   │   ├── __init__.py\n"
            "│   │   ├── dashboard_window.py\n"
            "│   │   ├── sidebar.py\n"
            "│   │   ├── content_area.py\n"
            "│   │   └── components/      # UI widgets\n"
            "│   │       ├── __init__.py\n"
            "│   │       └── component_theme_selector.py\n"
            "│   ├── pages/               # Page modules\n"
            "│   │   ├── __init__.py\n"
            "│   │   ├── page_base.py     # Base page class\n"
            "│   │   ├── page_home.py\n"
            "│   │   ├── page_about.py\n"
            "│   │   ├── page_button03.py\n"
            "│   │   ├── page_button04.py\n"
            "│   │   ├── page_button05.py\n"
            "│   │   ├── page_button06.py\n"
            "│   │   └── page_settings.py\n"
            "│   ├── modules/             # Feature modules\n"
            "│   │   ├── __init__.py\n"
            "│   │   ├── manager_navigation.py\n"
            "│   │   └── manager_theme_applicator.py\n"
            "│   └── utils/               # Utility functions\n"
            "│       ├── __init__.py\n"
            "│       └── manager_theme.py # CSS loader\n"
            "├── resources/               # Static resources\n"
            "│   ├── css/                 # Stylesheets\n"
            "│   │   └── style.css\n"
            "│   ├── fonts/               # Custom fonts\n"
            "│   └── images/              # Images and icons\n"
            "│       └── logo.png\n"
            "├── docs/                    # Documentation\n"
            "├── tests/                   # Test files\n"
            "├── README.md                # Project documentation\n"
            "├── requirements.txt         # Python dependencies\n"
            "├── setup.py                 # Installation script\n"
            "└── run.sh                   # Quick launch script"
            "</span>",
            selectable=True
        )
    
    def on_theme_changed(self, theme_id):
        """
        Handle theme change
        
        Args:
            theme_id: Selected theme identifier
        """
        self.current_theme_id = theme_id
        theme_def = get_theme(theme_id)
        
        # Apply theme
        self.theme_applicator.apply_theme(theme_def)
        
        print(f"Theme changed to: {theme_def.name}")
