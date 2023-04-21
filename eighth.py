def parse_assign(tokens):
    if tokens[0].type != 'ID':
        return False
    if tokens[1].type != 'ASSIGN':
        return False
    if not parse_expr(tokens[2:]):
        return False
    return True

def parse_expr(tokens):
    if not parse_term(tokens):
        return False
    while tokens[0].type in {'PLUS', 'MINUS'}:
        tokens = tokens[1:]
        if not parse_term(tokens):
            return False
    return True

def parse_term(tokens):
    if not parse_fact(tokens):
        return False
    while tokens[0].type in {'MULT', 'DIV', 'MOD'}:
        tokens = tokens[1:]
        if not parse_fact(tokens):
            return False
    return True

def parse_fact(tokens):
    if tokens[0].type == 'ID':
        return True
    if tokens[0].type == 'INT_LIT':
        return True
    if tokens[0].type == 'FLOAT_LIT':
        return True
    if tokens[0].type == 'LPAREN':
        if not parse_expr(tokens[1:]):
            return False
        if tokens[1].type != 'RPAREN':
            return False
        return True
    return False
