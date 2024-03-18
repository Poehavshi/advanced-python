from latexgen.latex_elements_generation import generate_table


def test_latex_table():
    table = [
        ["Name", "Age"],
        ["Alice", "20"],
        ["Bob", "21"],
    ]
    assert generate_table(table=table) == (
        '\\begin{tabular}{|c|c|}\n'
        '\\hline\n'
        'Name & Age\\\\\n'
        '\\hline\n'
        'Alice & 20\\\\\n'
        '\\hline\n'
        'Bob & 21\\\\\n'
        '\\hline\n'
        '\\end{tabular}'
    )
