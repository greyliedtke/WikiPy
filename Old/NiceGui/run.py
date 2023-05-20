from typing import Dict
from nicegui import ui, Tailwind
import NG.Wiki
import GuessN.Wiki
import MerMaker.Wiki
import theme
import ref

@ui.page("/")
def WikEq():
    theme.add_header()
    with theme.row():
        theme.title("*WikPy*")
        theme.subtitle("A wiki for things..")

    with theme.row():
        with theme.cc():
            ui.markdown("### WikEQ")
            ui.markdown("A symbolic solving and dimension referencing equation wiki.")
            ui.link("WikEq", "/WikEq")

    with theme.cc():
        ui.mermaid(ref.equation_merm).classes('bg-[#e6e6e6] p-4 self-stretch rounded flex flex-col gap-2')

ui.colors(primary='#7d7a7a')
ui.run(port=2999)
