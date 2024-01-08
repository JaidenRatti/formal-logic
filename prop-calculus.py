from sympy import symbols, And, Not
from sympy.parsing.sympy_parser import parse_expr
from sympy.logic.boolalg import truth_table, to_dnf, to_cnf, eliminate_implications
from sympy.logic.inference import satisfiable


def make_array(symbol_objects, truth_table, og):
    header = "|".join(str(symbol) for symbol in symbol_objects) + "|" + og
    separator = "+".join(["-" * len(col) for col in header.split("|")])

    print(header)
    print(separator)

    for row, result in truth_table:
        row_values = "|".join(str(val) for val in row + [result])
        print(row_values)


def sat(logic):
    if type(satisfiable(logic)) == bool:
        print("Not satisfiable")
    else:
        print("\nSatisfiable")
        print(satisfiable(logic))

def forms(logic):
    print("\nRemove implications: ")
    print(eliminate_implications(logic))

    print("\nConjunctive Normal Form: ")
    print(to_cnf(logic))

    print("\nDisjunctive Normal Form: ")
    print(to_dnf(logic))

def taut(premises):
    conc = premises[-1]
    conj = And(*premises[:-1])
    neg_conc = Not(conc)
    final = And(conj, neg_conc)
    return not(satisfiable(final))
    #cs245 :)

def main():
    app = []
    premises = int(input("How many premises? "))
    x = 1
    while premises > -1:
        if (premises != 0):
            prop = input("Premise " + str(x) + ": ")
        else:
            prop = input("Conclusion: ")
        syms = list(set([char for char in prop if char.isalpha()]))
        logic = parse_expr(prop)
        table = list(truth_table(logic, syms))
        make_array(syms, table, prop)
        sat(logic)
        forms(logic)
        app.append(logic)
        premises -= 1
        x += 1
    
    print("Tautology? " + str(taut(app)))

main()
