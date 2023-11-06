from interpreter.parser import Parser

parser = Parser()
program = """
BEGIN
	a = 5 + 5;
	b = 1 + b
	;;;;;;;;;;;;;;
	b = b + 5;
	BEGIN
		c = a + 4
	END
END.
""".strip()

print(
	parser.parse(program)
)