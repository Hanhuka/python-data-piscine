# import os
from time import sleep


def _progress_bar(percentage: int, total):
    bar_size = int(total * percentage / 100)
    str = ""
    i = 0
    while i < bar_size:
        str += "█"
        i += 1
    while i < total:
        str += " "
        i += 1
    return str


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    term_size = 100
    # term_size = os.get_terminal_size().columns
    size = len(lst)
    i = 0
    while i <= size:
        percentage = int(i * (100 / (len(lst))))
        decrease = (2 * len(str(size))) + 9
        bar_size = term_size - decrease
        print_percentage = (" " * (3 - len(str(percentage)))) + \
            str(percentage) + "%|"
        print_amount = "| " + (" " * (len(str(size)) - len(str(i)))) \
        + str(i) + "/" + str(size)
        bar = print_percentage + _progress_bar(percentage, bar_size) + print_amount, "\r"
        print(print_percentage + _progress_bar(percentage, bar_size)
              + print_amount, "\r", end='')
        i += 1
        yield bar
    return lst
