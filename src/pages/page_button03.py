"""
Button 03 Page
Example page template
"""

from pages.page_base import BasePage


class Button03Page(BasePage):
    """Button 03 example page"""
    
    def build_content(self):
        """Build page content"""
        
        self.add_title("Page 03")
        
        self.add_paragraph(
            "This is an example page for Button 03."
        )
        
        self.add_paragraph(
            "You can customize this page by editing:\n"
            "src/pages/page_button03.py"
        )
        
        self.add_subtitle("Example Content")
        
        self.add_paragraph(
            "Add your custom content here. You can use:\n\n"
            "• add_title() - For page titles\n"
            "• add_subtitle() - For section headers\n"
            "• add_paragraph() - For text content\n"
            "• add_markup_label() - For formatted text with links\n"
            "• Any GTK widgets you want"
        )
