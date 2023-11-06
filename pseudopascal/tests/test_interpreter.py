import pytest
from interpreter import Interpreter


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    interpreter = Interpreter()

    def test_empty_program(self, interpreter):
        interpreter.eval("BEGIN\nEND.")
        assert interpreter.variables == {}

    def test_empty_statements(self, interpreter):
        interpreter.eval("BEGIN\n;;;;;;;;;;;;;;\nEND.")
        assert interpreter.variables == {}

    def test_assignment(self, interpreter):
        interpreter.eval("BEGIN\nx := 5\nEND.")
        assert interpreter.variables == {
            "x": 5,
        }
    
    def test_assignment_chain(self, interpreter):
        interpreter.eval("BEGIN\nx := 5;\ny := x;\nz := y\nEND.")
        assert interpreter.variables == {
            "x": 5,
            "y": 5,
            "z": 5
        }

    def test_precedence(self, interpreter):
        interpreter.eval("BEGIN\nx := 2+2*2*2\nEND.")
        assert interpreter.variables == {
            "x": 2+2*2*2
        }

    def test_pos(self, interpreter):
        interpreter.eval("BEGIN\nx := +++2\nEND.")
        assert interpreter.variables == {
            "x": +++2
        }

    def test_neg(self, interpreter):
        interpreter.eval("BEGIN\nx := ---2\nEND.")
        assert interpreter.variables == {
            "x": ---2
        }

    def test_neg_expr(self, interpreter):
        interpreter.eval("BEGIN\nx := -(2*8)+100\nEND.")
        assert interpreter.variables == {
            "x": -(2*8)+100
        }

    def test_all_math(self, interpreter):
        interpreter.eval("BEGIN\nx := 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1))\nEND.")
        assert interpreter.variables == {
            "x": 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1))
        }

    def test_complex_statement(self, interpreter):
        program =   """
                    BEGIN
                        a := 5 + 5;
                        b := 1 + a
                        ;;;;;;;;;;;;;;
                        b := b + 5;
                        BEGIN
                            c := a + 4*-1
                        END
                    END.
                    """.strip()

        interpreter.eval(program)
        assert interpreter.variables == {
            "a": 10,
            "b": 16,
            "c": 6
        }

    def test_repr_not_crashing(self, interpreter):
        program =   """
                    BEGIN
                        a := 5 + 5;
                        b := 1 + a
                        ;;;;;;;;;;;;;;
                        b := b + 5;
                        BEGIN
                            c := a + 4*-1
                        END
                    END.
                    """.strip()

        print( interpreter.eval(program) )

    def test_undefined_variable(self, interpreter):
        with pytest.raises(NameError):
            interpreter.eval("BEGIN\nx := 5 + a\nEND.")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN\nx := 2&3\nEND.")

    def test_invalid_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN\nx := +*3\nEND.")

    def test_invalid_token_order(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN\nBEGIN\nEND.")
