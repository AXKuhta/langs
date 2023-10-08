
def parse(prefix):
	tokens = prefix.split(" ")[::-1]
	stack = []

	def try_pop(msg_if_fail):
		if len(stack) == 0:
			raise Exception(msg_if_fail)

		return stack.pop()

	for token in tokens:
		if token in ["+", "-", "*", "/"]:
			a = try_pop(f"what {token} what?")
			b = try_pop(f"{a} {token} what?")
			stack.append([a, token, b])
		else:
			stack.append(token)

	return stack

def generate_infix(tree):
	expression = []

	for level in tree:
		if type(level) is list:
			expression.append( f"({generate_infix(level)})" )
		else:
			expression.append( level )

	return " ".join(expression)
