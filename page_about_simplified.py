"""
About Page
GTK information, platforms, and adoption
Updated: Removed GTK Resources section
"""

from pages.page_base import BasePage


class AboutPage(BasePage):
    """About page with GTK information"""
    
    def build_content(self):
        """Build about page content"""
        
        # Page title
        self.add_title("About GTK")
        
        # GTK overview
        self.add_paragraph(
            "GTK (formerly GIMP Toolkit) is a free and open-source cross-platform widget toolkit "
            "for creating graphical user interfaces. Originally developed for the GIMP image editor, "
            "GTK has evolved into one of the most popular GUI toolkits for Linux desktop applications."
        )
        
        # Platform support section
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
        
        # Popularity section
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
