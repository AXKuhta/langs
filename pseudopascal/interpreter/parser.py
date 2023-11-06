from .token import Token, TokenType
from .lexer import Lexer
from .ast import UnOp, BinOp, Number

class Parser:
    def __init__(self):
        self._current_token = None
        self._lexer = Lexer()

    def seeing(self, type_, value=None):
        token = self._current_token

        if value is not None:
            return token and token.type_ == type_ and token.value == value
        else:
            return token and token.type_ == type_
    
    def check_token(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise SyntaxError("invalid token order")

    def factor(self):
        token = self._current_token
        if token.type_ == TokenType.NUMBER:
            self.check_token(TokenType.NUMBER)
            return Number(token)
        if token.type_ == TokenType.LPAREN:
            self.check_token(TokenType.LPAREN)
            result = self.expr()
            self.check_token(TokenType.RPAREN)
            return result
        if token.type_ == TokenType.OPERATOR and token.value in ["-", "+"]:
            self.check_token(TokenType.OPERATOR)
            return UnOp(token, self.factor())
        raise SyntaxError("Invalid factor")

    def term(self):
        result = self.factor()
        while self.seeing(TokenType.OPERATOR):
            if self._current_token.value not in ["*", "/"]:
                break
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.factor())            
        return result

    def expr(self):
        result = self.term()
        while self.seeing(TokenType.OPERATOR):
            if self._current_token.value not in ["+", "-"]:
                break
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.term())            
        return result

    def assignment(self):
        identifier = self._current_token.value
        self.check_token(TokenType.IDENTIFIER)
        self.check_token(TokenType.ASSIGN)
        ex = self.expr()
        print(identifier, "=", ex)

    def statement(self):
        if self.seeing(TokenType.KEYWORD, "END") or self.seeing(TokenType.SEMI):
            print("Empty statement")
            return

        return self.assignment()

    def statement_list(self):
        self.statement()

        while self.seeing(TokenType.SEMI):
            self.check_token(TokenType.SEMI)
            self.statement()

    def complex_statement(self):
        self.check_token(TokenType.KEYWORD)
        self.statement_list()
        self.check_token(TokenType.KEYWORD)

    def program(self):
        self.complex_statement()
        self.check_token(TokenType.DOT)

    def parse(self, code):
        self._lexer.init(code)
        self._current_token = self._lexer.next()
        return self.program()
