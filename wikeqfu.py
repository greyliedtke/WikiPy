"""
script for helping make wikeq funcs
"""

def solved_eqt(eq_vars, a):
    md_t = ""
    for v in eq_vars:
        if v == a['Symbol'].values[0]:pass
        else:
            md_t += f"{v} = 1 \n"
    md_t += f"{a['Solved'].values[0]}"
    return md_t