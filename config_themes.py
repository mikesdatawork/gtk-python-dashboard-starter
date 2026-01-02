"""
Theme Definitions
Popular dark themes for dashboard
"""


class ThemeDefinition:
    """Single theme definition"""
    
    def __init__(self, name, accent_color, sidebar_bg, window_bg, hover_color):
        self.name = name
        self.accent_color = accent_color
        self.sidebar_bg = sidebar_bg
        self.window_bg = window_bg
        self.hover_color = hover_color


# Theme collection - popular dark themes only
DARK_THEMES = {
    'default': ThemeDefinition(
        name='Default Blue',
        accent_color='#0078D7',      # Windows blue
        sidebar_bg='#353535',
        window_bg='#2d2d2d',
        hover_color='#404040'
    ),
    'arc': ThemeDefinition(
        name='Arc Dark',
        accent_color='#5294e2',      # Arc blue
        sidebar_bg='#2f343f',
        window_bg='#383c4a',
        hover_color='#404552'
    ),
    'adapta': ThemeDefinition(
        name='Adapta',
        accent_color='#00bcd4',      # Cyan
        sidebar_bg='#222d32',
        window_bg='#263238',
        hover_color='#2e3c43'
    ),
    'materia': ThemeDefinition(
        name='Materia',
        accent_color='#8ab4f8',      # Light blue
        sidebar_bg='#1e1e1e',
        window_bg='#212121',
        hover_color='#292929'
    ),
    'dracula': ThemeDefinition(
        name='Dracula',
        accent_color='#bd93f9',      # Purple
        sidebar_bg='#282a36',
        window_bg='#1e1f29',
        hover_color='#383a4a'
    ),
    'nord': ThemeDefinition(
        name='Nord',
        accent_color='#88c0d0',      # Nord blue
        sidebar_bg='#2e3440',
        window_bg='#3b4252',
        hover_color='#434c5e'
    ),
    'gruvbox': ThemeDefinition(
        name='Gruvbox',
        accent_color='#fe8019',      # Orange
        sidebar_bg='#282828',
        window_bg='#1d2021',
        hover_color='#3c3836'
    ),
    'solarized': ThemeDefinition(
        name='Solarized Dark',
        accent_color='#268bd2',      # Blue
        sidebar_bg='#002b36',
        window_bg='#073642',
        hover_color='#094452'
    ),
    'monokai': ThemeDefinition(
        name='Monokai',
        accent_color='#f92672',      # Pink
        sidebar_bg='#272822',
        window_bg='#1e1f1c',
        hover_color='#3e3d32'
    ),
    'onedark': ThemeDefinition(
        name='One Dark',
        accent_color='#61afef',      # Blue
        sidebar_bg='#282c34',
        window_bg='#21252b',
        hover_color='#2c313c'
    )
}


def get_theme(theme_id):
    """Get theme by ID"""
    return DARK_THEMES.get(theme_id, DARK_THEMES['default'])


def get_all_themes():
    """Get all available themes"""
    return DARK_THEMES
