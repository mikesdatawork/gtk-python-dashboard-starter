# GTK Python Dashboard Starter

![Dashboard Screenshot](resources/images/dashboard.png)

A modular template for building GTK3 desktop applications using Python and PyGObject. This starter provides a clean foundation for rapid dashboard development on Linux systems.

## Features

- **Modern Dark Theme** - Flat design with custom CSS styling
- **Fixed Sidebar Navigation** - 150px wide sidebar with customizable buttons
- **Square Logo Area** - 150x150px perfectly sized for branding
- **Modular Python Structure** - Organized codebase for easy extension
- **Page-Based Routing** - Navigation manager for clean page switching
- **Example Pages** - Button03-06 serve as templates for new pages
- **No Web Dependencies** - Pure GTK3, no browser or web server needed
- **Virtual Environment Support** - Isolated Python dependencies
- **Ready to Customize** - Add pages, change colors, extend functionality

## Project Structure

```
gtk-python-dashboard-starter/
├── src/                     # Python source code
│   ├── main.py              # Application entry point
│   ├── config/              # Configuration modules
│   │   ├── config_theme.py  # Color scheme, fonts
│   │   └── config_layout.py # Dimensions, spacing
│   ├── ui/                  # UI components
│   │   ├── dashboard_window.py
│   │   ├── sidebar.py
│   │   ├── content_area.py
│   │   └── components/
│   ├── pages/               # Page modules
│   │   ├── page_base.py     # Base class for all pages
│   │   ├── page_home.py     # Home page
│   │   ├── page_about.py    # About GTK page
│   │   ├── page_button03.py # Example page template
│   │   ├── page_button04.py # Example page template
│   │   ├── page_button05.py # Example page template
│   │   ├── page_button06.py # Example page template
│   │   └── page_settings.py # Settings/config page
│   ├── modules/             # Feature modules
│   │   └── manager_navigation.py
│   └── utils/               # Utility functions
│       └── manager_theme.py
├── resources/               # Static resources
│   ├── css/                 # GTK CSS stylesheets
│   │   └── style.css
│   └── images/              # Images and icons
│       ├── logo.png
│       └── dashboard.png
├── requirements.txt         # Python dependencies
├── setup.py                 # Installation script
├── run.sh                   # Quick launch script
└── README.md                # This file
```

## Installation

### System Dependencies (Debian/Ubuntu)

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

### Python Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

### Quick Start

```bash
./run.sh
```

### Or run directly

```bash
python3 src/main.py
```

### With virtual environment

```bash
source venv/bin/activate
python3 src/main.py
```

## Customization

### Add New Pages

1. Create a new page module in `src/pages/`:

```python
# src/pages/page_mypage.py
from pages.page_base import BasePage

class MyPage(BasePage):
    def build_content(self):
        self.add_title("My Custom Page")
        self.add_paragraph("Your content here")
```

2. Register the page in `src/ui/content_area.py`:

```python
from pages.page_mypage import MyPage

# In register_pages():
mypage = MyPage()
self.stack.add_named(mypage, "mypage")
self.nav_manager.register_page("mypage", mypage)
```

3. Add navigation button in `src/ui/sidebar.py`:

```python
# In nav_items list:
("My Page", "mypage"),
```

### Modify Sidebar Navigation

Edit `src/ui/sidebar.py` to change button labels, add new navigation items, or change button order.

### Change Colors

Edit `src/config/config_theme.py` to customize the color scheme. Key colors:
- Window Background: `#2d2d2d`
- Sidebar: `#353535`
- Active Button: `#0078D7`
- Text: `#eeeeee`

Or edit `resources/css/style.css` directly for fine-grained control.

### Replace Logo

Replace `resources/images/logo.png` with your own 150x150px image.

### Adjust Dimensions

Edit `src/config/config_layout.py` to change sidebar width, button height, margins, etc.

## Navigation Pages

The template includes 7 navigation pages:

1. **Home** - Introduction to the dashboard starter
2. **About** - GTK information, platforms, resources
3. **Button03** - Example page template
4. **Button04** - Example page template
5. **Button05** - Example page template
6. **Button06** - Example page template
7. **Settings** - Configuration and technical details (bottom of sidebar)

Example pages (Button03-06) serve as templates for creating your own custom pages.

## Color Scheme

| Component | Color Code | Description |
|-----------|------------|-------------|
| Window Background | #2d2d2d | Darker gray |
| Sidebar Background | #353535 | Dark gray |
| Logo Area | #3a3a3a | Medium dark gray |
| Active Button | #0078D7 | Windows blue |
| Button Hover | #404040 | Medium gray |
| Text (main) | #eeeeee | Off-white |
| Text (secondary) | #d0d0d0 | Light gray |
| Primary Accent | #0078D7 | Windows blue |
| Borders | #1a1a1a | Almost black |

## Technical Specifications

- **GTK Version**: GTK+ 3.0
- **Python**: 3.8+
- **Dependencies**: PyGObject, pycairo
- **Architecture**: Modular with page-based routing
- **Sidebar Width**: 150px
- **Logo Area**: 150x150px (square)
- **Navigation Button Height**: 28px
- **Navigation Pages**: 7 (Home, About, Button03-06, Settings)
- **Theme**: Custom dark flat theme
- **Naming Convention**: `config_*`, `page_*`, `manager_*`

## Modular Architecture

This template follows a modular design pattern:

- **config/** - Centralized configuration (theme, layout)
- **pages/** - Individual page modules (inherit from BasePage)
- **modules/** - Feature managers (navigation, etc.)
- **utils/** - Utility functions (theme loading, etc.)
- **ui/** - UI components (window, sidebar, content area)

Each page is a separate module, making it easy to add, remove, or modify pages without affecting others.

## GTK Resources

- [GTK Documentation](https://docs.gtk.org)
- [PyGObject Documentation](https://pygobject.readthedocs.io)
- [GNOME Developer Center](https://developer.gnome.org)
- [Awesome GTK Apps](https://github.com/valpackett/awesome-gtk)

## License

Free for personal, educational, and non-commercial use.

Commercial use requires explicit written permission from the author.

## Contributing

Issues and pull requests welcome. Please ensure code follows the existing style and structure.

## About

This template was created to provide a solid foundation for Python GTK3 desktop applications. It emphasizes clean code structure, modern design, modularity, and ease of customization.
