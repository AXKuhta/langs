from interpreter import Interpreter
import sys

if len(sys.argv) < 2:
	print("Usage: python3 pseudopas.py file.pas");
	exit()

with open(sys.argv[1]) as f:
	source = f.read()

interp = Interpreter()
print(interp.eval(source))
