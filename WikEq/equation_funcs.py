"""
script for helping with equation functions
"""

# ------------
from sympy import symbols, solve


def equation_v_detect(eqn_text: str):
    """
    input equation and return variables
    """
    # function to automatically identify symbols in equation
    split_eq = eqn_text.split(" ")

    # decide what is deemed a variable from equation
    # need to account for: numbers, wildcard,
    exp_arr = ["(", ")", "**", "*", "/", "+", "-", "=", '']

    # protected constants... figure this out...
    const_p = ['π', 'kB', 'G']

    var_a = []
    # loop through broken up equation
    for s in split_eq:
        if s in exp_arr:
            # print('skip for eval')
            continue
        elif s in const_p:
            if s == 'π':
                var_a.append({'s': s, 'const': 'PI', 'dim': '3.14159'})
            elif s == 'R':
                var_a.append(
                    {'s': s, 'const': 'Universal Gas Constant', 'dim': '8.314 J⋅K−1⋅mol−1'})
            elif s == 'G':
                var_a.append(
                    {'s': s, 'const': 'Gravitational Constant', 'dim': '6.674 E-11 N*m2*kg–2'})

        # try to evaluate to remove numbers
        else:
            try:
                eval(s)
            # add to symbol list if invalid...
            except:
                # account for duplicates. Add if not number
                if s not in var_a:
                    var_a.append(s)

    return var_a




# Solving for all variables -----------------------------------------------------------------------------------------
def symbol_solve(eq, eq_vars):

    # create dictionary of symbols... workaround for protected vars
    eq_split = eq.split("=")
    eqn_0 = eq_split[1] + " - " + eq_split[0]
    syms = {}

    # signify variables with "_v_"
    for v in eq_vars:
        syms['_'+v+'_'] = symbols('_'+v+'_')
        eqn_0 = eqn_0.replace(' '+v+' ', '_'+v+'_')

    # evaluate eq with dictionary of var symbols
    e_s = eval(str(eqn_0), syms)

    # loop through everything and add new term to self.eq_vars..
    solved_key = {}
    for v in syms:

        # ignore builtin dictionary from symbols...
        if v == '__builtins__':
            continue

        # take only first term of solved system... decide here...
        sym_solve = solve(e_s, v)[0]

        # formatting solved text
        solved_symbolic = str(sym_solve)
        for vv in syms:
            solved_symbolic = solved_symbolic.replace(vv, vv[1:-1])

        v = str(v)[1:-1]
        solved_text = v + " = " + solved_symbolic
        solved_key[v] = solved_text

    return solved_key