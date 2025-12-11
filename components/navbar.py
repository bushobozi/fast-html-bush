from fasthtml.common import *

# Shared Navbar Links
nav_links_array = [
    {"text": "Home", "href": "/"},
    # {"text": "Create Room", "href": "/change"},
    # {"text": "About Us", "href": "/about"},
    {"text": "Contact", "href": "/contact"},
]

NAV_BAR_STYLE = """
a.nav-item, a.nav-item:link,
a.nav-item:visited {
    margin-right: 1.5rem;
    text-decoration: none;
    color: #333;
    font-weight: 500;
    padding: 8px 12px;
    border-radius: 6px;
    font-family: Arial, sans-serif;
}
a.nav-item.active, a.nav-item.active:link,
a.nav-item.active:visited {
    border-radius: 12px;
    color: #333;
    font-weight: bold;
    background: #f0f0f0;
}
"""

class Navbar:
    @staticmethod
    def NavLink(text: str, href: str, is_active: bool = False):
        return A(
            text, 
            href=href, 
            cls="nav-item" + (" active" if is_active else ""),
           
        )
    
    @staticmethod
    def Navbar(links: list, current_path: str = "/"):
        nav_links = [
            Navbar.NavLink(
                link['text'], 
                link['href'], 
                is_active=(link['href'] == current_path)
            ) 
            for link in links
        ]
        return Nav(
            *nav_links,
            style="""
                display: flex;
                justify-content: start;
                align-items: center;
                padding: 1rem;
                width: 100%;
                border-bottom: 1px solid #ddd;
            """
        )