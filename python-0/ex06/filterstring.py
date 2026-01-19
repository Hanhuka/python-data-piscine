from ft_filter import ft_filter
import sys

def check_second_arg(arg):
    if not len(arg):
        return False
    i = 0
    for c in arg:
        if i == 0 and not (c.isdigit() or c == '+' or c == '-'):
            return False
        elif not c.isdigit():
            return False
        i += 1
    return (arg[-1].isdigit() and int(arg) >= 0)

def main():
    arg_len = len(sys.argv)
    try:
        assert arg_len == 3, "Wrong number of arguments"
        assert check_second_arg(sys.argv[2]), "Second argument needs to be a number"
    except AssertionError as error:
        print(error)
    min = int(sys.argv[2])
    min_length = lambda str: len(str) >= min
    print(ft_filter(min_length, sys.argv[1].split()))

if __name__ == "__main__":
    main()
