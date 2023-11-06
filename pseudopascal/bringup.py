from interpreter.parser import Parser
from interpreter import Interpreter

parser = Parser()
program = """
BEGIN
	a = 5 + 5;
	b = 1 + a
	;;;;;;;;;;;;;;
	b = b + 5;
	BEGIN
		c = a + 4
	END
END.
""".strip()

# print(
# 	parser.parse(program)
# )

interp = Interpreter()
print(interp.eval(program))
