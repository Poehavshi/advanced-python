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
        print(f"{i+1} {line}", end="")
    file.close()


if __name__ == "__main__":
    main()
