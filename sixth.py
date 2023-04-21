class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

def parse(tokens):
    def match(expected_token_type):
        nonlocal index
        if index >= len(tokens):
            return False
        if tokens[index].token_type == expected_token_type:
            index += 1
            return True
        return False

    def BLOCK():
        if match('LBRACE') and STMT_LIST() and match('RBRACE'):
            return True
        return False

    def STMT_LIST():
        while STMT():
            if not match('SEMICOLON'):
                break
        return True

    def STMT():
        return BLOCK() or ASSIGN() or IF_STMT() or WHILE_LOOP()

    def ASSIGN():
        if match('IDENTIFIER') and match('ASSIGN_OP') and (match('INTEGER') or match('IDENTIFIER')):
            return True
        return False

    def IF_STMT():
        if match('IF') and match('LPAREN') and BOOL_EXPR() and match('RPAREN') and BLOCK():
            if match('ELSE') and BLOCK():
                return True
            return True
        return False

    def WHILE_LOOP():
        if match('WHILE') and match('LPAREN') and BOOL_EXPR() and match('RPAREN') and BLOCK():
            return True
        return False

    def BOOL_EXPR():
        return match('BOOLEAN') or match('IDENTIFIER') or (match('LPAREN') and BOOL_EXPR() and match('RPAREN')) or (BOOL_EXPR() and match('OR_OP') and BOOL_EXPR()) or (BOOL_EXPR() and match('AND_OP') and BOOL_EXPR())

    index = 0
    return BLOCK()
