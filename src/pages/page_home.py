"""
Home Page
Dashboard starter template introduction page
"""

from pages.page_base import BasePage


class HomePage(BasePage):
    """Home page content"""
    
    def build_content(self):
        """Build home page content"""
        
        self.add_title("GTK Python Dashboard Starter")
        
        self.add_paragraph(
            "A modular template for rapid dashboard development using Python and GTK3."
        )
        
        self.add_paragraph(
            "This starter template provides a solid foundation with:\n\n"
            "• Clean dark theme with modern flat design\n"
            "• Modular Python code structure for easy extension\n"
            "• Fixed sidebar navigation with customizable pages\n"
            "• GTK3 widgets and styling (no web dependencies)\n"
            "• Virtual environment support\n"
            "• Ready for rapid prototyping and development",
            spacing_after=10
        )
        
        self.add_paragraph(
            "Get started by customizing the sidebar navigation, adding new pages, "
            "or modifying the dark theme colors to match your project."
        )
