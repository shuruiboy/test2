def stmt_list(tokens):
    if not tokens:
        return False
    
    while tokens and stmt(tokens):
        if tokens[0].value != ';':
            return False
        tokens.pop(0)
    
    return True
