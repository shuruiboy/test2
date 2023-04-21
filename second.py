class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

def parse(tokens):
    def match(expected_token_type):
        nonlocal current_token
        if current_token is None or current_token.token_type != expected_token_type:
            return False
        current_token = next_token()
        return True

    def peek():
        return None if current_token_index >= len(tokens) else tokens[current_token_index]

    def next_token():
        nonlocal current_token_index
        current_token_index += 1
        return peek()

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

    current_token_index = 0
    current_token = peek()

    if STMT():
        return current_token is None

    return False
