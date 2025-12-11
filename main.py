from fasthtml.common import *
from monsterui.all import *
from components.card import Card
from components.layout import Layout
from components.contact_form import ContactForm
from components.hero import Hero
app = FastHTML(debug=True, hdrs=Theme.blue.headers())

# Home page route
@app.get("/")
def home():
    content = Div(Hero.hero_section())
    return Layout(content, title="My FastHTML App", current_path="/")

# Create room page route
@app.get("/change")
def create_room_page():
    form_styles = """
    form {
        display: flex;
        flex-direction: column;
        place-content: center;
        width: 100%;
        max-width: 400px;
        gap: 1rem;
        font-family: Arial, sans-serif;
        margin: 2rem auto;
    }

    a.back-button, a.back-button:link,
    a.back-button:visited {
        margin-bottom: 0rem;
        text-decoration: none;
        color: #333;
        font-weight: bold;
        background: #f0f0f0;
        padding: 8px 12px;
        border-radius: 6px;
        text-align: center;
        width: fit-content;
    }

    a.back-button:hover {
        background: #e0e0e0;
        color: #111;
    }

    input, textarea {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 6px;
        font-size: 16px;
        font-family: Arial, sans-serif;
    }

    button.b-submit {
        padding: 8px 12px;
        font-weight: bold;
        font-size: 16px;
        font-family: Arial, sans-serif;
        background: #333;
        color: white;
        border-radius: 6px;
        cursor: pointer;
        border: none;
    }
    """

    content = (
        Form(
        A("Back", href="/", cls="back-button"),
        Label("Room Name", fr="name"),
        Input(id="name", name="name", placeholder="New Room Name", required=True),
        Label("Description", fr="description"),
        Textarea(id="description", name="description", rows="8", placeholder="Room Description", required=True),
        Label("Max Participants", fr="max_participants"),
        Input(id="max_participants", name="max_participants", type="number", min="1", max="100", placeholder="10", required=True),
        Div(
            Input(id="is_private", name="is_private", type="checkbox", required=True),
            Label("Private Room", fr="is_private")
        ),
        Label("Password", fr="password"),
        Input(id="password", name="password", type="password", placeholder="Room Password", required=True),
        Label("Re-enter Password", fr="confirm_password"),
        Input(id="confirm_password", name="confirm_password", type="password", placeholder="Confirm Password", required=True),
        Button("Create Room", cls="b-submit", type="submit"),
        hx_post="/rooms", hx_target="#rooms-list", hx_swap="afterbegin"
    )

    )
    return Layout(content, title="Create Room", current_path="/change", extra_styles=form_styles)

# About page route
@app.get("/about")
def about():
    content = Div(
        H1("About Us"),
        P("Welcome to our FastHTML application. We're building modern web applications with Python!"),
        P("This application demonstrates how to use reusable layouts, components, and routing."),
        style="max-width: 600px; margin: 0 auto;"
    )
    return Layout(content, title="About Us", current_path="/about")

# Contact page route
@app.get("/contact")
def contact():
    content = Div(ContactForm.contact_form())
    return Layout(content, title="Tailwind test", current_path="/contact")

    

serve()