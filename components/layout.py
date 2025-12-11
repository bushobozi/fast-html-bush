from fasthtml.common import *
from components.navbar import Navbar, NAV_BAR_STYLE, nav_links_array

LAYOUT_STYLE = """
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    font-size: 14px;
}

.container {
    margin: 0 auto;
    padding: 20px;
    width: 80%;
}

@media (max-width: 768px) {
    .container {
        width: 98%;
        padding: 10px;
    }
}
@media (min-width: 1200px) {
    .container {
        width: 100%;
    }
}
"""

def Layout(content, title="FastHTML Application", current_path="/", include_navbar=True, extra_styles=""):
    """
    Reusable layout component for all pages.

    Args:
        content: The main content to display (can be any FT component or list of components)
        title: Page title (default: "FastHTML Application")
        current_path: Current route path for navbar highlighting (default: "/")
        include_navbar: Whether to include the navbar (default: True)
        extra_styles: Additional CSS styles to inject (default: "")
    """
    head_content = [
        Title(title),
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Style(NAV_BAR_STYLE + LAYOUT_STYLE + extra_styles),
        # cdn
        Link(href="https://cdn.jsdelivr.net/npm/daisyui@5", rel="stylesheet", type="text/css"),
        Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4")
    ]

    body_content = []
    if include_navbar:
        body_content.append(Navbar.Navbar(nav_links_array, current_path=current_path))

    body_content.append(
        Div(content, cls="containe-r")
    )

    return Html(
        Head(*head_content),
        Body(*body_content)
    )