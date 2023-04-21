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

    def STMT():
        return IF_STMT() or BLOCK() or ASSIGN() or DECLARE() or WHILE_LOOP()

    def IF_STMT():
        if match('IF') and match('LPAREN') and EXPR() and match('RPAREN') and STMT():
            if match('ELSE'):
                return STMT()
            return True
        return False

    def BLOCK():
        if match('LBRACE'):
            while STMT():
                pass
            return match('RBRACE')
        return False

    def ASSIGN():
        if match('IDENTIFIER') and match('ASSIGN_OP') and (match('INTEGER') or match('IDENTIFIER')):
            return True
        return False

    def DECLARE():
        if match('VAR') and match('IDENTIFIER'):
            if match('ASSIGN_OP') and (match('INTEGER') or match('IDENTIFIER')):
                return True
            return True
        return False

    def WHILE_LOOP():
        if match('WHILE') and match('LPAREN') and EXPR() and match('RPAREN') and STMT():
            return True
        return False

    def EXPR():
        return match('INTEGER') or match('IDENTIFIER') or (match('LPAREN') and EXPR() and match('RPAREN'))

    index = 0
    return STMT()

