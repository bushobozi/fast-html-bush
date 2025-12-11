from fasthtml.common import *

class Hero:
    @staticmethod
    def hero_section():
        return Div(cls="text-center")(
            H1("Home Page", cls="text-7xl py-25")
        )