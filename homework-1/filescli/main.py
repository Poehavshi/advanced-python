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
@click.argument("file", type=click.File(), default=stdin, required=False)
def number_lines(file):
    if file == stdin:
        for count, line in enumerate(file, 1):
            print(f"{count:6}  {line}", end="")
        return
    count = 1
    lines: list[str] = file.readlines()
    max_width = len(str(len(lines)))
    for line in lines:
        if line.isspace():
            print(f"{'':>{max_width}}  {line}", end="")
            continue
        print(f"    {count:>{max_width}}  {line}", end="")
        count += 1
    file.close()


@main.command(
    "tail",
    help="output the last N lines, instead of the last 10, if we have input from stdin,"
    "we will output the last 17 lines.",
)
@click.argument("files", type=click.File(), nargs=-1)
@click.option("-n", type=click.INT, default=10)
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


@main.command(
    "wc",
    help="print newline, word, and byte counts for each file,"
    " and a total line if more than one file is specified.",
)
@click.argument("files", type=click.File(), nargs=-1)
def word_count(files):
    total_lines = 0
    total_words = 0
    total_bytes = 0
    for file in files:
        lines = file.readlines()
        num_of_words = 0
        num_of_bytes = 0
        for line in lines:
            total_lines += 1
            num_of_words += len(line.split())
            num_of_bytes += len(line)
        total_words += num_of_words
        total_bytes += num_of_bytes
        print(f" {lines.__len__():>7} {num_of_words:>7} {num_of_bytes:>7} {file.name}")
        file.close()
    if len(files) > 1:
        print(f" {total_lines:>7} {total_words:>7} {total_bytes:>7} total")
    if len(files) == 0:
        lines = stdin.readlines()
        num_of_words = 0
        num_of_bytes = 0
        for line in lines:
            total_lines += 1
            num_of_words += len(line.split())
            num_of_bytes += len(line)
        total_words += num_of_words
        total_bytes += num_of_bytes
        print(f" {lines.__len__():>7} {num_of_words:>7} {num_of_bytes:>7}")


if __name__ == "__main__":
    main()
