"""
Home Page
Dashboard starter template introduction page
Updated: Added Linux desktop application information
"""

from pages.page_base import BasePage


class HomePage(BasePage):
    """Home page content"""
    
    def build_content(self):
        """Build home page content"""
        
        # Page title
        self.add_title("GTK Python Dashboard Starter Template")
        
        self.add_paragraph(
            "A modular template for rapid dashboard development using Python and GTK3."
        )
        
        # Linux Desktop Application section
        self.add_subtitle("Linux Desktop Application Template")
        
        self.add_paragraph(
            "This template is designed specifically for native Linux desktop applications. "
            "Built with GTK3, it runs natively across all major Linux distributions including:"
        )
        
        self.add_paragraph(
            "• Ubuntu, Debian, Linux Mint\n"
            "• Fedora, CentOS, Red Hat Enterprise Linux\n"
            "• Arch Linux, Manjaro, EndeavourOS\n"
            "• openSUSE, SUSE Linux Enterprise\n"
            "• Pop!_OS, Elementary OS, Zorin OS\n"
            "• MX Linux, Solus, Gentoo\n"
            "• And virtually any Linux distribution with GTK3 support",
            spacing_after=10
        )
        
        # Features section
        self.add_subtitle("Template Features")
        
        self.add_paragraph(
            "This starter template provides a solid foundation with:\n\n"
            "• Clean dark theme with modern flat design\n"
            "• Modular Python code structure for easy extension\n"
            "• Fixed sidebar navigation with customizable pages\n"
            "• GTK3 widgets and styling (no web dependencies)\n"
            "• Virtual environment support\n"
            "• 7 popular dark themes included\n"
            "• Ready for rapid prototyping and development",
            spacing_after=10
        )
        
        # Getting started
        self.add_paragraph(
            "Get started by customizing the sidebar navigation, adding new pages, "
            "or selecting a different dark theme to match your project."
        )
