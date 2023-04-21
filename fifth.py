def if_stmt(tokens):
    if match(tokens, 'IF') and match(tokens, 'LPAREN') and bool_expr(tokens) and match(tokens, 'RPAREN') and block(tokens):
        if match(tokens, 'ELSE'):
            return block(tokens)
        return True
    return False

