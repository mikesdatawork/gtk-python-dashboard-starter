"""
Settings Page
Dashboard configuration and technical details
Updated: Reflects new Button03-06 pages
"""

from pages.page_base import BasePage


class SettingsPage(BasePage):
    """Settings page with configuration information"""
    
    def build_content(self):
        """Build settings page content"""
        
        self.add_title("Dashboard Configuration")
        
        self.add_paragraph(
            "Technical details about this dashboard starter template."
        )
        
        self.add_subtitle("Project Structure")
        
        self.add_markup_label(
            "<span font_family='monospace' foreground='#d0d0d0'>"
            "gtk-python-dashboard-starter/\n"
            "├── src/                     # Python source code\n"
            "│   ├── main.py              # Application entry point\n"
            "│   ├── config/              # Configuration modules\n"
            "│   │   ├── config_theme.py\n"
            "│   │   └── config_layout.py\n"
            "│   ├── ui/                  # UI components\n"
            "│   │   ├── dashboard_window.py\n"
            "│   │   ├── sidebar.py\n"
            "│   │   ├── content_area.py\n"
            "│   │   └── components/\n"
            "│   ├── pages/               # Page modules\n"
            "│   │   ├── page_base.py\n"
            "│   │   ├── page_home.py\n"
            "│   │   ├── page_about.py\n"
            "│   │   ├── page_button03.py\n"
            "│   │   ├── page_button04.py\n"
            "│   │   ├── page_button05.py\n"
            "│   │   ├── page_button06.py\n"
            "│   │   └── page_settings.py\n"
            "│   ├── modules/             # Feature modules\n"
            "│   │   └── manager_navigation.py\n"
            "│   └── utils/               # Utility functions\n"
            "│       └── manager_theme.py\n"
            "├── resources/               # Static resources\n"
            "│   ├── css/                 # GTK CSS stylesheets\n"
            "│   └── images/              # Images and icons\n"
            "├── requirements.txt         # Python dependencies\n"
            "├── setup.py                 # Installation script\n"
            "├── run.sh                   # Quick launch script\n"
            "└── README.md                # Documentation"
            "</span>",
            selectable=True
        )
        
        self.add_subtitle("Color Scheme")
        
        self.add_markup_label(
            "<span font_family='monospace' foreground='#d0d0d0'>"
            "Component                   Color Code    Description\n"
            "─────────────────────────────────────────────────────────\n"
            "Window Background           #2d2d2d       Darker gray\n"
            "Sidebar Background          #353535       Dark gray\n"
            "Logo Area Background        #3a3a3a       Medium dark gray\n"
            "Nav Button Active           #0078D7       Windows blue\n"
            "Nav Button Hover            #404040       Medium gray\n"
            "Content Text (main)         #eeeeee       Off-white\n"
            "Content Text (secondary)    #d0d0d0       Light gray\n"
            "Primary Accent              #0078D7       Windows blue\n"
            "Border/Separator            #1a1a1a       Almost black\n"
            "Input Background            #3a3a3a       Medium dark gray"
            "</span>",
            selectable=True
        )
        
        self.add_subtitle("Technical Specifications")
        
        self.add_paragraph(
            "• GTK Version: GTK+ 3.0\n"
            "• Python: 3.8+\n"
            "• Dependencies: PyGObject, pycairo\n"
            "• Architecture: Modular with page-based routing\n"
            "• Sidebar Width: 150px\n"
            "• Logo Area: 150x150px (square)\n"
            "• Navigation Button Height: 28px\n"
            "• Navigation Pages: 7 (Home, About, Button03-06, Settings)\n"
            "• Theme: Custom dark flat theme\n"
            "• License: Free for personal and educational use"
        )
