def parse_assign(tokens):
    if tokens[0].token_type == 'IDENTIFIER' and tokens[1].lexeme == '=':
        tokens.pop(0)
        tokens.pop(0)
        return parse_expr(tokens)
    return False

def parse_expr(tokens):
    if parse_term(tokens):
        while tokens[0].lexeme in ['+', '-']:
            tokens.pop(0)
            if not parse_term(tokens):
                return False
        return True
    return False

def parse_term(tokens):
    if parse_fact(tokens):
        while tokens[0].lexeme in ['*', '/', '%']:
            tokens.pop(0)
            if not parse_fact(tokens):
                return False
        return True
    return False

def parse_fact(tokens):
    if tokens[0].token_type in ['IDENTIFIER', 'INTEGER', 'FLOAT']:
        tokens.pop(0)
        return True
    elif tokens[0].lexeme == '(':
        tokens.pop(0)
        if not parse_expr(tokens):
            return False
        if tokens[0].lexeme != ')':
            return False
        tokens.pop(0)
        return True
    return False
