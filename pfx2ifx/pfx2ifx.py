from lib import parse, generate_infix
import sys

#if __name__ == "__main__":

if len(sys.argv) != 2:
	print("Usage: python3 pfx2ifx.py \"+ - 13 4 55\"")
	exit()

print(
	generate_infix(
		parse(sys.argv[1])
	)
)
