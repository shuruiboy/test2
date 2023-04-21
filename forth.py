def while_loop(tokens):
    if len(tokens) < 5 or tokens[0].value != 'while' or tokens[1].value != '(':
        return False
    
    i = 2
    while i < len(tokens):
        if tokens[i].value == ')':
            block_result = block(tokens[i+1:])
            return block_result
        i += 1
    
    return False
