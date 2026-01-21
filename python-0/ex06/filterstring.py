from ft_filter import ft_filter
import sys


def _check_second_arg(arg):
    if not len(arg):
        return False
    i = 0
    for c in arg:
        if i == 0:
            if not (c.isdigit() or c == '+' or c == '-'):
                print(c)
                print(i)
                print("a")
                return False
        elif not c.isdigit():
            return False
        i += 1
    return (arg[-1].isdigit() and int(arg) >= 0)


def main():
    arg_len = len(sys.argv)
    try:
        assert arg_len == 3, "AssertionError: Wrong number of arguments\n\
Expected 2, got " + str(arg_len - 1)
        assert _check_second_arg(sys.argv[2]), "AssertionError: \
Second argument needs to be a positive integer"
    except AssertionError as error:
        print(error)
        return
    min = int(sys.argv[2])
    print(ft_filter(lambda str: len(str) >= min, sys.argv[1].split()))


if __name__ == "__main__":
    main()
