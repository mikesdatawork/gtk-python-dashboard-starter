# GTK Python Dashboard Starter

A modular template for building GTK3 desktop applications using Python and PyGObject.

This template provides a solid foundation with:
- Fixed dark sidebar with navigation
- Scrollable content area with multiple pages
- Modern dark theme with CSS styling
- Modular Python structure for easy extension
- Comprehensive documentation and comments

Converted from the C GTK Dashboard Starter template.

## Project Structure

```
gtk-python-dashboard-starter/
├── src/
│   ├── main.py              # Application entry point
│   ├── ui/                  # UI components
│   │   ├── dashboard_window.py
│   │   ├── sidebar.py
│   │   └── content_area.py
│   ├── modules/             # Feature modules
│   └── utils/               # Utility functions
├── resources/
│   ├── css/                 # Stylesheets
│   ├── images/              # Images and icons
│   └── fonts/               # Custom fonts
├── tests/                   # Unit tests
├── reference/               # C template reference
├── requirements.txt         # Python dependencies
├── setup.py                 # Installation script
└── run.sh                   # Launch script
```

## Installation

### System Dependencies (Debian/Ubuntu)

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

### Python Dependencies

```bash
pip3 install -r requirements.txt
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

### Install and run

```bash
pip3 install -e .
dashboard
```

## Development

This template is designed for modular development:

1. Add new pages in `src/ui/`
2. Add feature modules in `src/modules/`
3. Add utilities in `src/utils/`
4. Customize styling in `resources/css/style.css`

## License

Free for personal, educational, and non-commercial use.
Commercial use requires explicit written permission.

## Reference

This Python template is based on the C GTK Dashboard Starter.
The original C source is available in `reference/gtk-dashboard-starter-c/` for comparison.
