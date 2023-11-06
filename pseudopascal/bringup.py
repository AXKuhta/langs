from interpreter.parser import Parser

parser = Parser()
program = """
BEGIN
	a = 5 + 5;
	b = 1 + b
	;;;;;;;;;;;;;;
END.
""".strip()

print(
	parser.parse(program)
)