from interpreter.parser import Parser

parser = Parser()
program = """
BEGIN
END.
""".strip()

parser.parse(program)
