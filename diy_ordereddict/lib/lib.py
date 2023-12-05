from .parse import parse_key, parse_query

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
