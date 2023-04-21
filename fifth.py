def parse(tokens):
    index = 0

    def match(token_type):
        nonlocal index
        if index >= len(tokens):
            return False
        if tokens[index].token_type == token_type:
            index += 1
            return True
        return False

    def BOOL_EXPR():
        return match('BOOL_OPERATOR') or match('INTEGER')

    def BLOCK():
        return match('LBRACE') and STMT_LIST() and match('RBRACE')

    def IF_STMT():
        return match('IF') and match('LPAREN') and BOOL_EXPR() and match('RPAREN') and BLOCK() and (match('ELSE') and BLOCK() or True)

    def STMT_LIST():
        return STMT() and (match('SEMICOLON') and STMT_LIST() or True)

    def STMT():
        return IF_STMT() or BLOCK() or ASSIGN() or DECLARE() or WHILE_LOOP()

    def ASSIGN():
        return match('IDENTIFIER') and match('ASSIGN_OP') and (match('INTEGER') or match('IDENTIFIER'))

    def DECLARE():
        return match('VAR') and match('IDENTIFIER') and (match('ASSIGN_OP') and (match('INTEGER') or match('IDENTIFIER')) or True)

    def WHILE_LOOP():
        return match('WHILE') and match('LPAREN') and BOOL_EXPR() and match('RPAREN') and BLOCK()

    return STMT_LIST() and index == len(tokens)
