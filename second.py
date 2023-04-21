def parse_stmt(tokens):
    if parse_if_stmt(tokens):
        return True
    elif parse_block(tokens):
        return True
    elif parse_assign(tokens):
        return True
    elif parse_declare(tokens):
        return True
    elif parse_while_loop(tokens):
        return True
    else:
        return False

