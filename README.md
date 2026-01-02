# GTK Python Dashboard Starter Template

A modular template for rapid dashboard development using Python and GTK3, designed specifically for native Linux desktop applications.

## Overview

This template provides a production-ready foundation for building Linux desktop applications with GTK3. It features a clean dark theme, modular architecture, and 7 professional theme options.

## Linux Distribution Support

Built with GTK3, this template runs natively across all major Linux distributions including:
- Ubuntu, Debian, Linux Mint
- Fedora, CentOS, Red Hat Enterprise Linux
- Arch Linux, Manjaro, EndeavourOS
- openSUSE, SUSE Linux Enterprise
- Pop!_OS, Elementary OS, Zorin OS
- MX Linux, Solus, Gentoo
- Any Linux distribution with GTK3 support

## Features

- **Clean Dark Theme** - Modern flat design with 7 theme variations
- **Modular Architecture** - Easy to extend with new pages and features
- **Theme Selector** - Switch between 7 professional dark themes
- **Fixed Sidebar** - 150px sidebar with logo and navigation
- **Page-Based Routing** - Independent pages with individual scroll states
- **GTK3 Native** - No web dependencies, pure GTK widgets
- **Virtual Environment** - Isolated Python environment
- **Production Ready** - Clean codebase, well-documented

## Themes

Seven professional dark themes included:
1. **Default Blue** (#0078D7) - Windows-style blue accent
2. **Adapta** (#00bcd4) - Cyan accent
3. **Materia** (#8ab4f8) - Light blue accent
4. **Dracula** (#bd93f9) - Purple accent
5. **Nord** (#88c0d0) - Nordic blue accent
6. **Gruvbox** (#fe8019) - Orange warmth accent
7. **Monokai** (#f92672) - Pink highlight accent

## Project Structure

```
gtk-python-dashboard-starter/
├── src/                     # Application source code
│   ├── main.py              # Entry point
│   ├── config/              # Configuration modules
│   │   ├── config_theme.py  # Theme colors/fonts
│   │   ├── config_layout.py # Layout dimensions
│   │   └── config_themes.py # Theme definitions
│   ├── ui/                  # UI components
│   │   ├── dashboard_window.py
│   │   ├── sidebar.py
│   │   ├── content_area.py
│   │   └── components/      # UI widgets
│   │       └── component_theme_selector.py
│   ├── pages/               # Page modules
│   │   ├── page_base.py     # Base page class
│   │   ├── page_home.py
│   │   ├── page_about.py
│   │   ├── page_button03.py
│   │   ├── page_button04.py
│   │   ├── page_button05.py
│   │   ├── page_button06.py
│   │   └── page_settings.py
│   ├── modules/             # Feature modules
│   │   ├── manager_navigation.py
│   │   └── manager_theme_applicator.py
│   └── utils/               # Utility functions
│       └── manager_theme.py # CSS loader
├── resources/               # Static resources
│   ├── css/                 # Stylesheets
│   │   └── style.css
│   ├── fonts/               # Custom fonts
│   └── images/              # Images and icons
│       └── logo.png
├── docs/                    # Documentation
├── tests/                   # Test files
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── setup.py                 # Installation script
└── run.sh                   # Quick launch script
```

## Installation

### Prerequisites
- Python 3.8 or higher
- GTK+ 3.0
- pip (Python package manager)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/mikesdatawork/gtk-python-dashboard-starter.git
   cd gtk-python-dashboard-starter
   ```

2. **Run the application**
   ```bash
   ./run.sh
   ```
   
   The `run.sh` script will:
   - Create a virtual environment (if needed)
   - Install dependencies
   - Launch the application

### Manual Installation

If you prefer to set up manually:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python3 src/main.py
```

## Usage

### Adding New Pages

1. Create a new page module in `src/pages/`:
   ```python
   from pages.page_base import BasePage
   
   class MyNewPage(BasePage):
       def build_content(self):
           self.add_title("My New Page")
           self.add_paragraph("Page content here...")
   ```

2. Register the page in `src/ui/content_area.py`:
   ```python
   from pages.my_new_page import MyNewPage
   
   # In register_pages():
   my_page = MyNewPage()
   self.register_page("mypage", my_page)
   ```

3. Add navigation button in `src/ui/sidebar.py`:
   ```python
   nav_items = [
       ("My Page", "mypage"),
       # ... other items
   ]
   ```

### Customizing Themes

Themes are defined in `src/config/config_themes.py`. Each theme includes:
- Accent color
- Sidebar background
- Window background
- Hover color

To add a new theme, add an entry to the `DARK_THEMES` dictionary.

### Modifying Layout

Layout dimensions are centralized in `src/config/config_layout.py`:
- Sidebar width
- Logo dimensions
- Button heights
- Spacing values

## Technical Specifications

- **GTK Version**: GTK+ 3.0
- **Python**: 3.8+
- **Dependencies**: PyGObject, pycairo, Pillow
- **Architecture**: Modular with page-based routing
- **Sidebar**: 150px fixed width
- **Logo**: 150x150px square
- **Navigation Buttons**: 28px height
- **Pages**: 7 navigation pages
- **Themes**: 7 dark themes

## Development

### Running Tests
```bash
pytest tests/
```

### Code Structure
- **config/** - Centralized configuration (themes, colors, layout)
- **ui/** - User interface components (window, sidebar, content area)
- **pages/** - Individual page modules inheriting from BasePage
- **modules/** - Feature modules (navigation, theme application)
- **utils/** - Utility functions (CSS loading, etc.)

## License

Free for personal and educational use.

## Contributing

This is a template project. Fork it and customize for your needs.

## Repository

https://github.com/mikesdatawork/gtk-python-dashboard-starter

## Author

mikesdatawork

---

**Note**: This template is designed as a starting point. Customize the pages, themes, and functionality to match your project requirements.
