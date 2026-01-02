"""
Content area component
Scrollable area that displays different pages
Updated: Clickable links on About page
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
        """Create the default pages with detailed content"""
        
        # ========================================
        # HOME PAGE
        # ========================================
        home_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        home_page.set_margin_start(40)
        home_page.set_margin_end(40)
        home_page.set_margin_top(40)
        home_page.set_margin_bottom(40)
        
        home_title = Gtk.Label(label="GTK Python Dashboard Starter")
        home_title.get_style_context().add_class('page-title')
        home_title.set_xalign(0)
        home_page.pack_start(home_title, False, False, 0)
        
        home_content1 = Gtk.Label(
            label="A modular template for rapid dashboard development using Python and GTK3."
        )
        home_content1.set_line_wrap(True)
        home_content1.set_xalign(0)
        home_page.pack_start(home_content1, False, False, 0)
        
        home_content2 = Gtk.Label(
            label="This starter template provides a solid foundation with:\n\n"
                  "• Clean dark theme with modern flat design\n"
                  "• Modular Python code structure for easy extension\n"
                  "• Fixed sidebar navigation with customizable pages\n"
                  "• GTK3 widgets and styling (no web dependencies)\n"
                  "• Virtual environment support\n"
                  "• Ready for rapid prototyping and development"
        )
        home_content2.set_line_wrap(True)
        home_content2.set_xalign(0)
        home_page.pack_start(home_content2, False, False, 10)
        
        home_content3 = Gtk.Label(
            label="Get started by customizing the sidebar navigation, adding new pages, "
                  "or modifying the dark theme colors to match your project."
        )
        home_content3.set_line_wrap(True)
        home_content3.set_xalign(0)
        home_page.pack_start(home_content3, False, False, 0)
        
        self.stack.add_named(home_page, "home")
        
        # ========================================
        # ABOUT PAGE
        # ========================================
        about_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        about_page.set_margin_start(40)
        about_page.set_margin_end(40)
        about_page.set_margin_top(40)
        about_page.set_margin_bottom(40)
        
        about_title = Gtk.Label(label="About GTK")
        about_title.get_style_context().add_class('page-title')
        about_title.set_xalign(0)
        about_page.pack_start(about_title, False, False, 0)
        
        about_content1 = Gtk.Label(
            label="GTK (formerly GIMP Toolkit) is a free and open-source cross-platform widget toolkit "
                  "for creating graphical user interfaces. Originally developed for the GIMP image editor, "
                  "GTK has evolved into one of the most popular GUI toolkits for Linux desktop applications."
        )
        about_content1.set_line_wrap(True)
        about_content1.set_xalign(0)
        about_page.pack_start(about_content1, False, False, 0)
        
        # Platform support section
        platform_label = Gtk.Label(label="Platform Support")
        platform_label.get_style_context().add_class('page-subtitle')
        platform_label.set_xalign(0)
        about_page.pack_start(platform_label, False, False, 5)
        
        platform_content = Gtk.Label(
            label="GTK applications run natively on:\n\n"
                  "• Linux (primary platform)\n"
                  "• BSD variants (FreeBSD, OpenBSD, NetBSD)\n"
                  "• Windows (via MinGW or MSYS2)\n"
                  "• macOS (via Homebrew or MacPorts)\n\n"
                  "PyGObject provides Python bindings for GTK, enabling rapid development "
                  "with Python's simplicity and GTK's native performance."
        )
        platform_content.set_line_wrap(True)
        platform_content.set_xalign(0)
        about_page.pack_start(platform_content, False, False, 0)
        
        # Popularity section
        popularity_label = Gtk.Label(label="Adoption & Ecosystem")
        popularity_label.get_style_context().add_class('page-subtitle')
        popularity_label.set_xalign(0)
        about_page.pack_start(popularity_label, False, False, 5)
        
        popularity_content = Gtk.Label(
            label="GTK powers many popular Linux desktop applications including:\n\n"
                  "• GNOME Desktop Environment\n"
                  "• GIMP (GNU Image Manipulation Program)\n"
                  "• Inkscape (Vector Graphics Editor)\n"
                  "• Transmission (BitTorrent Client)\n"
                  "• Audacity (Audio Editor)\n"
                  "• FileZilla (FTP Client)\n"
                  "• Many file managers, media players, and system utilities"
        )
        popularity_content.set_line_wrap(True)
        popularity_content.set_xalign(0)
        about_page.pack_start(popularity_content, False, False, 0)
        
        # Resources section with CLICKABLE links
        resources_label = Gtk.Label(label="Example Applications & Resources")
        resources_label.get_style_context().add_class('page-subtitle')
        resources_label.set_xalign(0)
        about_page.pack_start(resources_label, False, False, 5)
        
        resources_intro = Gtk.Label(label="Explore curated collections of GTK applications:")
        resources_intro.set_xalign(0)
        about_page.pack_start(resources_intro, False, False, 0)
        
        # Create clickable links using markup
        resources_content = Gtk.Label()
        resources_content.set_markup(
            "\n• <a href='https://github.com/valpackett/awesome-gtk'>Awesome GTK</a>\n"
            "• <a href='https://docs.gtk.org'>GTK Documentation</a>\n"
            "• <a href='https://pygobject.readthedocs.io'>PyGObject Documentation</a>\n"
            "• <a href='https://developer.gnome.org'>GNOME Developer Center</a>"
        )
        resources_content.set_line_wrap(True)
        resources_content.set_xalign(0)
        about_page.pack_start(resources_content, False, False, 0)
        
        self.stack.add_named(about_page, "about")
        
        # ========================================
        # SETTINGS PAGE
        # ========================================
        settings_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        settings_page.set_margin_start(40)
        settings_page.set_margin_end(40)
        settings_page.set_margin_top(40)
        settings_page.set_margin_bottom(40)
        
        settings_title = Gtk.Label(label="Dashboard Configuration")
        settings_title.get_style_context().add_class('page-title')
        settings_title.set_xalign(0)
        settings_page.pack_start(settings_title, False, False, 0)
        
        settings_intro = Gtk.Label(
            label="Technical details about this dashboard starter template."
        )
        settings_intro.set_line_wrap(True)
        settings_intro.set_xalign(0)
        settings_page.pack_start(settings_intro, False, False, 0)
        
        # Project structure section
        structure_label = Gtk.Label(label="Project Structure")
        structure_label.get_style_context().add_class('page-subtitle')
        structure_label.set_xalign(0)
        settings_page.pack_start(structure_label, False, False, 5)
        
        structure_content = Gtk.Label()
        structure_content.set_markup(
            "<span font_family='monospace'>"
            "gtk-python-dashboard-starter/\n"
            "├── src/                     # Python source code\n"
            "│   ├── main.py              # Application entry point\n"
            "│   ├── ui/                  # UI components\n"
            "│   │   ├── dashboard_window.py\n"
            "│   │   ├── sidebar.py\n"
            "│   │   └── content_area.py\n"
            "│   ├── modules/             # Feature modules\n"
            "│   └── utils/               # Utility functions\n"
            "├── resources/               # Static resources\n"
            "│   ├── css/                 # GTK CSS stylesheets\n"
            "│   └── images/              # Images and icons\n"
            "├── requirements.txt         # Python dependencies\n"
            "├── setup.py                 # Installation script\n"
            "├── run.sh                   # Quick launch script\n"
            "└── README.md                # Documentation"
            "</span>"
        )
        structure_content.set_line_wrap(False)
        structure_content.set_xalign(0)
        structure_content.set_selectable(True)  # Allow copying
        settings_page.pack_start(structure_content, False, False, 0)
        
        # Color scheme section
        colors_label = Gtk.Label(label="Color Scheme")
        colors_label.get_style_context().add_class('page-subtitle')
        colors_label.set_xalign(0)
        settings_page.pack_start(colors_label, False, False, 5)
        
        colors_content = Gtk.Label()
        colors_content.set_markup(
            "<span font_family='monospace'>"
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
            "</span>"
        )
        colors_content.set_line_wrap(False)
        colors_content.set_xalign(0)
        colors_content.set_selectable(True)  # Allow copying
        settings_page.pack_start(colors_content, False, False, 0)
        
        # Technical specs section
        specs_label = Gtk.Label(label="Technical Specifications")
        specs_label.get_style_context().add_class('page-subtitle')
        specs_label.set_xalign(0)
        settings_page.pack_start(specs_label, False, False, 5)
        
        specs_content = Gtk.Label(
            label="• GTK Version: GTK+ 3.0\n"
                  "• Python: 3.8+\n"
                  "• Dependencies: PyGObject, pycairo\n"
                  "• Sidebar Width: 150px\n"
                  "• Logo Area: 150x150px (square)\n"
                  "• Navigation Button Height: 28px\n"
                  "• Theme: Custom dark flat theme\n"
                  "• License: Free for personal and educational use"
        )
        specs_content.set_line_wrap(True)
        specs_content.set_xalign(0)
        settings_page.pack_start(specs_content, False, False, 0)
        
        self.stack.add_named(settings_page, "settings")
    
    def show_page(self, page_name):
        """Show a specific page"""
        self.stack.set_visible_child_name(page_name)
