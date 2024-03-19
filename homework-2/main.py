import os

from latexgen.latex_elements_generation import generate_table, generate_document, generate_image


def task1(output_dir="artifacts", file_name="output.tex"):
    table = [["1", "2", "3"], ["4", "5", "6"]]
    result = generate_document(nested_code=generate_table(table), title="My Table", author="Me", date="Today")
    with open(f'{output_dir}/{file_name}', 'w') as f:
        f.write(result)


def task2(output_dir="artifacts", file_name="output.tex", image_path="../data/image.png"):
    table = [["1", "2", "3"], ["4", "5", "6"]]
    nested_code = generate_table(table=table) + generate_image(image_path, 100, 100)
    result = generate_document(nested_code=nested_code, title="My Image", author="Me", date="Today")
    print(result)
    with open(f'{output_dir}/{file_name}', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    print("Running tasks...")
    os.makedirs("artifacts", exist_ok=True)
    print(os.listdir("."))
    print(os.listdir("artifacts"))
    task1("artifacts", "task1.tex")
    task2("artifacts", "task2.tex", "input.png")
    os.system("pdflatex -output-directory=artifacts artifacts/task2.tex")
    print("Tasks completed.")
