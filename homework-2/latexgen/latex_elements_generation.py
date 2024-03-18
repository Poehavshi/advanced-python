

def generate_table(table: list[list[str]]) -> str:
    """
    Generate a latex code from a 2D list of strings.
    """
    number_of_columns = len(table[0])
    begin_table_code = r"\begin{tabular}{|" + "c|" * number_of_columns + r"}"
    hline_code = r"\hline"
    end_table_code = r"\end{tabular}"
    rows = [f"{' & '.join(row)}\\\\" + '\n' + hline_code + '\n' for row in table]
    latex_code = begin_table_code + '\n' + hline_code + '\n' + ''.join(rows) + end_table_code
    return latex_code


def generate_image(image_path: str, width: int, height: int) -> str:
    """
    Generate a latex code for an image.
    """
    width = str(width) + "px"
    height = str(height) + "px"
    latex_code = r"""\begin{figure}
\centering
\includegraphics[width=%s,height=%s]{%s}
\end{figure}
""" % (width, height, image_path)
    return latex_code


def generate_document(nested_code: str, title: str, author: str, date: str) -> str:
    """
    Generate a latex document from a nested code.
    """
    document = r"""\documentclass{article}
\usepackage{graphicx}
\usepackage[utf8]{inputenc}
\title{%s}
\author{%s}
\date{%s}
\begin{document}
\maketitle
%s
\end{document}
""" % (title, author, date, nested_code)
    return document
