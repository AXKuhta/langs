from .token import Token

class Node:
    def __repr__(self):
        return str(self)

    pass

class Number(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Number ({self.token})"

class Variable(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Variable ({self.token})"

class Assignment(Node):
    def __init__(self, lhs: Node, rhs: Node):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"Assignment({self.lhs}, {self.rhs})"

class StatementList(Node):
    def __init__(self, stmts:list):
        self.stmts = stmts 

    def __str__(self):
        return f"StatementList({self.stmts})"

class UnOp(Node):
    def __init__(self, op: Token, right: Node):
        self.op = op
        self.right = right

    def __str__(self):
        return f"UnOp{self.op.value} ({self.right})"

class BinOp(Node):
    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOp{self.op.value} ({self.left}, {self.right})"

