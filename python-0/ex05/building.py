import sys


def main():
	arg_len = len(sys.argv)
	print(arg_len)
	try:
		assert arg_len <= 2, "Assertion Error: too many arguments (max 1)"
	except AssertionError as error:
		print(error)
		return
	if arg_len == 1:
		print("Type bro ;)")
		text = input()
	else:
		text = sys.argv[1]
	print(sum(1 for c in text if c.isupper()), " upper letters")
	print(sum(1 for c in text if c.islower()), " lower letters")
	print(sum(1 for c in text if not(c.isalpha() or c.isspace())), " punctuation")
	print(sum(1 for c in text if c.isspace()), " space")
	print(sum(1 for c in text if c.isdigit()), "digits")
	return
	



if __name__ == "__main__":
	main()