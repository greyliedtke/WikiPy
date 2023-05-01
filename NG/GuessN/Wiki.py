from nicegui import ui
from WikEq.DF.dfs import df_eq, df_eqv, df_eqd
import theme
import random
import WikEq.page_equations, WikEq.page_dimensions
from GuessN.guesser import number_guesser

# initial variables
guesses = 0
correct_a = random.randint(0,100)
mino, maxo = 0, 100

@ui.page('/GuessInt')
def WikEq():
    # init game

    
    with theme.frame('WikEq'):
        ui.label(correct_a)
    
    with ui.expansion('Instructions'):
        ui.markdown('''### Int Guesser''')
        ui.markdown('''-guess a number between 0 and 100
        - you will be prompted whether guess is greater or less
        - try to guess in least possible tries
        ''')
    
    with ui.row():
        with ui.card():
            with ui.row():
                with ui.column():
                    t_guess = ui.input('Guess', value=5)
                    for t in range(10):
                        ui.button(t)
                with ui.column():
                    s_guess = ui.input('Guess', value=0)
                    for s in range(10):
                        ui.button(s)
                with ui.column():
                    ui.button('Guess', on_click=lambda: page_update())
                    

        with ui.card():
            slider = ui.slider(min=mino, max=maxo, value=50)
            ming = ui.label(f'guess between {mino} and {maxo}')
            gg = ui.label(f'guesses: {guesses}')


        def page_update():
            current_guess = 50
            current_guess, correct_a, mino, maxo = number_guesser(current_guess, correct_a, mino, maxo)
            gg.text = f'guesses: {90}'








