from fasthtml.common import *
from monsterui.all import Button

def Card(title: str, description: str, image_url: str, link_url: str):
    return Div(
        Script("""
function handleClick(event) {
    event.preventDefault();
    alert('Button clicked!');
}
        """),
        Img(src=image_url, alt=title, style="width:100%; height: 200px; object-fit: cover; border-radius: 8px;"),
        H2(title, style="margin: 0.5rem 0;"),
        P(description, style="color: #555;"),
        A("Learn More", href=link_url, onclick="handleClick(event)", style="""
padding: 8px 12px;
                font-weight: bold;
                font-size: 16px;
                font-family: Arial, sans-serif;
                background: #333;
                color: white;
                border-radius: 6px;
                cursor: pointer;
                border: none;
                text-decoration: none;
          width: 100%;
                text-align: center;
"""),
        Button("Click Me", onclick="handleClick(event)", style="""
                margin-top: 10px;
                padding: 8px 12px;
                font-weight: bold;
                font-size: 16px;
                font-family: Arial, sans-serif;
                background: #007BFF;
                color: white;
                border-radius: 6px;
                cursor: pointer;
                border: none;
            """),
        cls="card",
        style="""
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 0.5rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            width: 100%;
        """
    )