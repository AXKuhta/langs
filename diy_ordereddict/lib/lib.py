from operator import lt, le, eq, ne, ge, gt

class SpecialHashMap(dict):
	def __init__(self, **args):
		super().__init__(**args)
		self.ploc = PAccessor(self)

	@property
	def iloc(self):
		return [v for k, v in sorted(self.items(), key=lambda x: x[0])]

# Парсер для выборок через ploc
class PAccessor:
	def __init__(self, storage):
		self.storage = storage

	def __getitem__(self, query):
		x_list, b_list = parse_query(query)
		results = {}

		for k, v in self.storage.items():
			a_list = parse_key(k)

			if len(a_list) == len(b_list):
				if all_fit(a_list, x_list, b_list):
					results[k] = v

		return results

def all_fit(a_list, x_list, b_list):
	for a, x, b in zip(a_list, x_list, b_list):
		if not x(a, b):
			return False

	return True

# "1, 5" => [1, 5]
# "value1" => []
def parse_key(key):
	log = [SepToken()]

	def log_append(cls, value):
		if type(log[-1]) is not cls:
			log.append(cls())

		log[-1].value += letter

	# Токенизировать
	for letter in key:
		if letter.isdigit():
			log_append(NumberToken, letter)
		elif letter.isalpha():
			return []
		else:
			log_append(SepToken, letter)

	a_list = []

	# Распарсить поток токенов
	for token in log:
		if type(token) is NumberToken:
			a_list.append(int(token.value))

	return a_list

# ">10, >20" =>
# x_list = [gt, gt]
# b_list = [10, 20]
def parse_query(query):
	log = [SepToken()]

	def log_append(cls, value):
		if type(log[-1]) is not cls:
			log.append(cls())

		log[-1].value += letter

	# Токенизировать
	for letter in query:
		if letter.isdigit():
			log_append(NumberToken, letter)
		elif letter in [">", "<", "="]:
			log_append(OpToken, letter)
		else:
			log_append(SepToken, letter)

	x_list = []
	b_list = []

	# Распрасить поток токенов
	while len(log):
		token = log.pop(0)

		if type(token) is SepToken:
			continue
		elif type(token) is OpToken:
			if token.value not in ["=", "<>", ">", "<", ">=", "<="]:
				raise Exception(f"Unknown operator: {token.value}")

			if len(log) == 0:
				raise Exception(f"Operator {token.value} missing a number")

			value = log.pop(0)

			if type(value) is not NumberToken:
				raise Exception(f"Operator {token.value} missing a number")

			str2op = {
				"=": eq,
				"<>": ne,
				">": gt,
				"<": lt,
				">=": ge,
				"<=": le
			}

			x_list.append(str2op[token.value])
			b_list.append(int(value.value))

		elif type(token) is NumberToken:
			raise Exception(f"Extraneous number: {token.value}")

	return x_list, b_list

class Token:
	def __init__(self):
		self.value = ""

	def __repr__(self):
		return self.value

class NumberToken(Token):
	pass

class OpToken(Token):
	pass

class SepToken(Token):
	pass

