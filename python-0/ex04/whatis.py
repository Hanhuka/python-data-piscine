import sys


def whatis(argv: any):
    if len(argv) == 1:
        return
    try:
        assert len(argv) <= 2, "AssertionError: more than one \
              argument is provided"
    except AssertionError as error:
        print(error)
    try:
        int(argv[1])
        integer = int(argv[1])
        if integer % 2:
            print("I'm Odd.")
        else:
            print("I'n Even.")
    except ValueError as error:
        print("AssertionError: You must input an int\n", end="")
        print(error)


whatis(sys.argv)
