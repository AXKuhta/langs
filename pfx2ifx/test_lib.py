from lib import parse, generate_infix
import pytest

def test_parse():
	tree = parse("+ + 10 20 30")

	assert tree[0][0][0] == "10"
	assert tree[0][0][1] == "+"
	assert tree[0][0][2] == "20"
	assert tree[0][1] == "+"
	assert tree[0][2] == "30"

def test_parse_exception():
	with pytest.raises(Exception):
		parse("- - 1 2")

def test_generate_infix():
	assert generate_infix([[["10", "+", "20"], "+", "30"]]) == "((10 + 20) + 30)"
