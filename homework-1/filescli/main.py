from sys import stdin

import click


@click.group()
def main():
    pass


@main.command(
    "nl",
    help="The nl utility reads lines from the named file,"
    "applies a configurable line numbering filter operation, "
    "and writes the result to the standard output.  "
    "If file is a single dash (`-`) or absent, nl reads from the standard input.",
)
@click.argument("file", type=click.File(), default="-", required=False)
def number_lines(file):
    if file.name == "-":
        file = stdin
    for i, line in enumerate(file):
        print(f"\t{i+1}	{line}", end="")
    file.close()


# specify multiple files as arguments
@main.command("tail")
@click.argument("files", type=click.File(), nargs=-1)
@click.option(
    "-n",
    type=click.INT,
    default=10,
    help="output the last N lines, instead of the last 10, if we have input from stdin,"
    "we will output the last 17 lines.",
)
def tail(files, n):
    need_to_print_file_name = len(files) > 1
    for file in files:
        print(f"==> {file.name} <==") if need_to_print_file_name else None
        lines = file.readlines()
        for line in lines[-n:]:
            print(line, end="")
        file.close()
    if len(files) == 0:
        n = 17 if n == 10 else n
        lines = stdin.readlines()
        for line in lines[-n:]:
            print(line, end="")


if __name__ == "__main__":
    main()
