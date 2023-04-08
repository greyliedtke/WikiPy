from typing import Dict

from nicegui import ui, Tailwind

import WikEq.Wiki
import GuessN.Wiki
import theme


@ui.page("/")
def WikEq():
    theme.add_header()
    with theme.row():
        theme.title("*WikPy*")
        theme.subtitle("A wiki for things..")

    with theme.row():
        with ui.card():
            ui.markdown("### WikEQ")
            ui.markdown("A large reference for equations and dimensions")
            ui.link("WikEq", "/WikEq")

    with theme.row():
        with ui.card():
            ui.markdown("### Python")

ui.run(port=2999)