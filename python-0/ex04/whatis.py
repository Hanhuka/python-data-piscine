import sys

def whatis(argv: any):
	if len(argv) == 1:
		return
	if len(argv) > 2:
		print("AssertionError: more than one argument is provided")
		return 
	try:
		integer = int(argv[1])
	except:
		print("AssertionError: argument is not an integer")
		return
	if integer % 2:
		print("I'm Odd.")
	else:
		print("I'n Even.")

whatis(sys.argv)