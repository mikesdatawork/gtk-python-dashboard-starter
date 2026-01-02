"""
Navigation Manager
Handles page routing and navigation state
"""


class NavigationManager:
    """Manages navigation state and page switching"""
    
    def __init__(self):
        """Initialize navigation manager"""
        self.pages = {}
        self.current_page = None
        self.page_stack = None
        self.callbacks = []
    
    def register_page(self, page_id, page_widget):
        """Register a page with the navigation system"""
        self.pages[page_id] = page_widget
    
    def set_page_stack(self, stack):
        """Set the GTK Stack widget for page switching"""
        self.page_stack = stack
    
    def navigate_to(self, page_id):
        """Navigate to a specific page"""
        if page_id in self.pages and self.page_stack:
            self.current_page = page_id
            self.page_stack.set_visible_child_name(page_id)
            
            for callback in self.callbacks:
                callback(page_id)
            
            return True
        return False
    
    def on_navigate(self, callback):
        """Register a callback for navigation events"""
        self.callbacks.append(callback)
    
    def get_current_page(self):
        """Get current page identifier"""
        return self.current_page
    
    def get_page_widget(self, page_id):
        """Get widget for a specific page"""
        return self.pages.get(page_id)
