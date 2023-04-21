def block(tokens):
    if tokens[0].value != '{':
        return False

    if not stmt_list(tokens[1:]):
        return False

    if tokens[1+len(stmt_list(tokens[1:]))].value != '}':
        return False

    return True

