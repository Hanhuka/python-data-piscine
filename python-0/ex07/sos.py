import sys

NESTED_MORSE = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ' ': '/'}


def main():
    try:
        assert len(sys.argv) == 2, "Wrong number of arguments broski 🥀"
        for c in sys.argv[1]:
            assert c.upper() in NESTED_MORSE, \
                "AssertionError: Invalid character"
        for c in sys.argv[1]:
            print(NESTED_MORSE[c.upper()], end=" ")
        print("")
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
