from contextlib import contextmanager
from nicegui import ui

def menu() -> None:
    ui.link('WikEq', '/WikEq').classes(replace='text-white')

def content() -> None:
    ui.label('This is the home page.').classes('text-h4 font-bold text-grey-8')

@contextmanager
def frame(navtitle: str):
    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.colors(primary='#6E93D6', secondary='#53B689', accent='#111B1E', positive='#53B689')
    with ui.header().classes('justify-between text-white'):
        ui.label('WikiPy').classes('font-bold')
        ui.label(navtitle)
        with ui.row():
            menu()
    with ui.row().classes('absolute-center'):
        yield

def add_header() -> None:
    menu_items = {
        'WikEQ': '/WikEq',
        'Why?': '/#why',
    }
    with ui.header() \
            .classes('items-center duration-200 p-0 px-4 no-wrap') \
            .style('box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)'):
        with ui.row().classes('lg:hidden'):
            with ui.menu().classes('bg-primary text-white text-lg') as menu:
                for title, target in menu_items.items():
                    ui.menu_item(title, on_click=lambda _, target=target: ui.open(target))
            ui.button(on_click=menu.open).props('flat color=white icon=menu')
        with ui.row().classes('max-lg:hidden'):
            for title, target in menu_items.items():
                ui.link(title, target).classes(replace='text-lg text-white')

def title(content: str) -> ui.markdown:
    return ui.markdown(content).classes('text-4xl sm:text-5xl md:text-6xl font-medium')

def subtitle(content: str) -> ui.markdown:
    return ui.markdown(content).classes('text-xl sm:text-2xl md:text-3xl leading-7')

@contextmanager
def row():
    '''Custom page frame to share the same styling and behavior across all pages'''
    with ui.row().classes('justify-center items-center'):
        yield