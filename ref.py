"""
python file to reference equations and things
"""

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
