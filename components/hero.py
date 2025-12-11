from fasthtml.common import *

class Hero:
    @staticmethod
    def hero_section():
        return Div(cls="hero min-h-screen", style="background-image: url(https://cdn.pixabay.com/photo/2025/10/27/10/25/alps-9919976_640.jpg);")(
            Div(cls="hero-overlay bg-opacity-60"),
            Div(cls="hero-content text-neutral-content text-center")(
                Div(cls="max-w-md")(
                    H1("Testing out fastHtml and DaisyUi with Tailwind", cls="mb-5 text-7xl font-bold"),
                    P("Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.", cls="mb-5"),
                    Button("Get Started", cls="btn btn-primary")
                )
            )
        )