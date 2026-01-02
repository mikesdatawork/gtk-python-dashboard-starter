"""
About Page
GTK information, platforms, and resources
"""

from pages.page_base import BasePage


class AboutPage(BasePage):
    """About page with GTK information"""
    
    def build_content(self):
        """Build about page content"""
        
        self.add_title("About GTK")
        
        self.add_paragraph(
            "GTK (formerly GIMP Toolkit) is a free and open-source cross-platform widget toolkit "
            "for creating graphical user interfaces. Originally developed for the GIMP image editor, "
            "GTK has evolved into one of the most popular GUI toolkits for Linux desktop applications."
        )
        
        self.add_subtitle("Platform Support")
        
        self.add_paragraph(
            "GTK applications run natively on:\n\n"
            "• Linux (primary platform)\n"
            "• BSD variants (FreeBSD, OpenBSD, NetBSD)\n"
            "• Windows (via MinGW or MSYS2)\n"
            "• macOS (via Homebrew or MacPorts)\n\n"
            "PyGObject provides Python bindings for GTK, enabling rapid development "
            "with Python's simplicity and GTK's native performance."
        )
        
        self.add_subtitle("Adoption & Ecosystem")
        
        self.add_paragraph(
            "GTK powers many popular Linux desktop applications including:\n\n"
            "• GNOME Desktop Environment\n"
            "• GIMP (GNU Image Manipulation Program)\n"
            "• Inkscape (Vector Graphics Editor)\n"
            "• Transmission (BitTorrent Client)\n"
            "• Audacity (Audio Editor)\n"
            "• FileZilla (FTP Client)\n"
            "• Many file managers, media players, and system utilities"
        )
        
        self.add_subtitle("GTK Resources & Documentation")
        
        self.add_markup_label(
            "<span font_family='monospace' foreground='#d0d0d0'>"
            "Resource                        Description\n"
            "──────────────────────────────────────────────────────────────\n"
            "</span>"
            "<span font_family='monospace'>"
            "<a href='https://docs.gtk.org'>GTK Documentation</a>              Official GTK reference\n"
            "<a href='https://pygobject.readthedocs.io'>PyGObject Docs</a>                 Python bindings guide\n"
            "<a href='https://developer.gnome.org'>GNOME Developer</a>                Developer resources\n"
            "<a href='https://github.com/valpackett/awesome-gtk'>Awesome GTK</a>                    Curated app collection\n"
            "<a href='https://gitlab.gnome.org/GNOME/gtk'>GTK Source Code</a>                Official repository\n"
            "<a href='https://www.gtk.org'>GTK Official Site</a>              Main project website\n"
            "<a href='https://discourse.gnome.org'>GNOME Discourse</a>                Community forum\n"
            "<a href='https://github.com/Rapptz/gTK-Examples'>GTK Examples</a>                   Code examples repo\n"
            "</span>",
            selectable=True
        )
