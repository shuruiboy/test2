class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

    def __repr__(self):
        return f"{self.token_type}({self.lexeme})"


def parse(tokens):
    def match(token_type):
        nonlocal index
        if index >= len(tokens):
            return False
        if tokens[index].token_type == token_type:
            index += 1
            return True
        return False

    def ASSIGN():
        if match('IDENTIFIER') and match('ASSIGN_OP') and EXPR():
            return True
        return False

    def EXPR():
        return TERM() and EXPR_PRIME()

    def EXPR_PRIME():
        if match('ADD_OP') and TERM() and EXPR_PRIME():
            return True
        return True

    def TERM():
        return FACTOR() and TERM_PRIME()

    def TERM_PRIME():
        if match('MUL_OP') and FACTOR() and TERM_PRIME():
            return True
        return True

    def FACTOR():
        return match('INTEGER') or match('IDENTIFIER') or (match('LPAREN') and EXPR() and match('RPAREN'))

    index = 0
    return ASSIGN()
