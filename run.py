from typing import Dict
from nicegui import ui, Tailwind
import WikEq.Wiki
import GuessN.Wiki
import MerMaker.Wiki
import theme
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from nicegui import ui, Tailwind, app


equation_merm = """
graph LR
subgraph <a href='https://www.wikeq.com/EqBaseDimensions/'>Base Dimensions</a>
  L(Length)
	M(Mass)
	T(Time)
end
subgraph <a href='https://www.wikeq.com/EqBaseDimensions/'>SI Base Units</a>
  bu_L(meter)
	bu_M(kilogram)
	bu_T(second)
end
subgraph Equation Variables
	F(Force-N)
  m(mass-kg)
	a(acceleration)
end
subgraph Equation
eq(F = m * a)
end


L-->bu_L--m-->F
M-->bu_M--kg-->a
bu_M--kg-->F
bu_M--kg-->m
T-->bu_T--s^-2-->a
bu_T--s^-2-->F

F--kg*m/s^2-->eq
m--kg-->eq
a--m/s^2-->eq
"""


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
        ui.mermaid(equation_merm).classes('bg-[#e6e6e6] p-4 self-stretch rounded flex flex-col gap-2')

ui.colors(primary='#7d7a7a')
app.add_middleware(SessionMiddleware, secret_key='some_random_string')
ui.run(port=2999)
