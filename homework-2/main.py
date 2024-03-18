from latexgen.latex_elements_generation import generate_table, generate_document, generate_image


def task1(output_dir="artifacts", file_name="output.tex"):
    table = [["1", "2", "3"], ["4", "5", "6"]]
    result = generate_document(nested_code=generate_table(table), title="My Table", author="Me", date="Today")
    with open(f'{output_dir}/{file_name}', 'w') as f:
        f.write(result)


def task2(output_dir="artifacts", file_name="output.tex", image_path="../data/image.png"):
    result = generate_document(nested_code=generate_image(image_path, 100, 100), title="My Image", author="Me", date="Today")
    with open(f'{output_dir}/{file_name}', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    task1("artifacts", "task2.tex")
    task2("artifacts", "task2.tex", "../data/input.png")
