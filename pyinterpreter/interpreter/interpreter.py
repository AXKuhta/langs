from .parser import Parser
from .ast import Number, UnOp, BinOp

class NodeVisitor:
    
    def visit(self):
        pass

class Interpreter(NodeVisitor):
    
    def __init__(self):
        self.parser = Parser()

    def visit(self, node):
        if isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, UnOp):
            return self.visit_unop(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)

    def visit_number(self, node):
        return float(node.token.value)

    def visit_unop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.right)
            case "-":
                return -self.visit(node.right)

    def visit_binop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            case _:
                raise ValueError("Invalid operator")

    def eval(self, code):
        tree = self.parser.parse(code)
        return self.visit(tree)
