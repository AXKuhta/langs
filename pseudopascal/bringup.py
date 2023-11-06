from interpreter.parser import Parser

parser = Parser()
program = """
BEGIN
	a = 5 + 5
	;;;;;;;;;;;;;;
END.
""".strip()

parser.parse(program)
