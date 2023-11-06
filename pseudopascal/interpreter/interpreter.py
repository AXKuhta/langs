from .parser import Parser
from .ast import *

class NodeVisitor:
    
    def visit(self):
        pass

class Interpreter(NodeVisitor):
    
    def __init__(self):
        self.parser = Parser()
        self.variables = {}

    def visit(self, node):
        if isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, UnOp):
            return self.visit_unop(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, StatementList):
            return self.visit_statementlist(node)
        elif isinstance(node, Assignment):
            return self.visit_assignment(node)
        elif isinstance(node, Variable):
            return self.visit_variable(node)
        elif node is None:
            pass

        else:
            raise Exception(f"Internal AST traversal error: unknown node type: {node}")

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

    def visit_statementlist(self, node):
        for stmt in node.stmts:
            self.visit(stmt)

    def visit_assignment(self, node):
        identifier = node.lhs.token.value
        self.variables[identifier] = self.visit(node.rhs)
    
    def visit_variable(self, node):
        identifier = node.token.value
        if identifier not in self.variables:
            raise NameError(f"Undefined variable: {identifier}")

        return self.variables[identifier]

    def eval(self, code):
        tree = self.parser.parse(code)
        self.visit(tree)
        return tree
